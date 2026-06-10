#!/usr/bin/env python3
"""
Site Analytics Weekly Report
Gera relatório semanal de performance para sites afiliados.
Uso: python3 weekly-report.py --site guiaculinaria.com.br
"""

import json
import sys
import requests
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# Config
TOKEN_FILE = '/root/.openclaw/workspace/.gtm-token.json'
WP_COOKIE = '/tmp/gc_fresh.txt'
WP_USER = 'Davi'
WP_PASS = '9429rMTOqC$g0dcpfE6R*L3c'
REPORTS_DIR = '/root/.openclaw/workspace/skills/site-analytics/reports'

def get_sc_data(site_url, start, end, dimensions=['page'], limit=200):
    """Busca dados do Search Console."""
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE,
            scopes=['https://www.googleapis.com/auth/webmasters.readonly'])
        creds.refresh(Request())
        
        headers = {'Authorization': f'Bearer {creds.token}', 'Content-Type': 'application/json'}
        url = f'https://searchconsole.googleapis.com/webmasters/v3/sites/{site_url}/searchAnalytics/query'
        
        resp = requests.post(url, headers=headers, json={
            'startDate': start, 'endDate': end,
            'dimensions': dimensions, 'rowLimit': limit
        })
        
        if resp.status_code == 200:
            return resp.json().get('rows', [])
        return []
    except Exception as e:
        print(f"SC Error: {e}")
        return []

def get_wp_data(endpoint, params=''):
    """Busca dados do WordPress via REST API."""
    try:
        import subprocess
        result = subprocess.run(
            ['curl', '-s', '-b', WP_COOKIE,
             f'https://{endpoint}/wp-json/wp/v2/{params}'],
            capture_output=True, text=True, timeout=15
        )
        return json.loads(result.stdout) if result.stdout else []
    except:
        return []

def get_affiliate_clicks():
    """Busca cliques de afiliado do GCAM Monitor."""
    try:
        import subprocess
        result = subprocess.run(
            ['curl', '-s', '-b', WP_COOKIE,
             'https://guiaculinaria.com.br/wp-admin/admin.php?page=gcam-monitor'],
            capture_output=True, text=True, timeout=15
        )
        html = result.stdout
        # Parse table rows
        import re
        rows = re.findall(r'<tr><td>(\d+)</td><td>(amazon|mercadolivre)</td><td>(\d+)</td>', html)
        total = sum(int(r[2]) for r in rows)
        return {'total': total, 'rows': rows}
    except:
        return {'total': 0, 'rows': []}

def generate_report(site_config, site_name):
    """Gera relatório completo."""
    today = datetime.now()
    today_str = today.strftime('%Y-%m-%d')
    
    # Calculate periods
    start_7d = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    start_14d = (today - timedelta(days=14)).strftime('%Y-%m-%d')
    start_28d = (today - timedelta(days=28)).strftime('%Y-%m-%d')
    start_56d = (today - timedelta(days=56)).strftime('%Y-%m-%d')
    start_90d = (today - timedelta(days=90)).strftime('%Y-%m-%d')
    
    sc_url = site_config.get('sc_url', f'sc-domain:{site_name}')
    
    # Get data
    data_7d = get_sc_data(sc_url, start_7d, today_str)
    data_14d = get_sc_data(sc_url, start_14d, (today - timedelta(days=8)).strftime('%Y-%m-%d'))
    data_28d = get_sc_data(sc_url, start_28d, today_str)
    data_56d = get_sc_data(sc_url, start_56d, (today - timedelta(days=29)).strftime('%Y-%m-%d'))
    data_90d = get_sc_data(sc_url, start_90d, today_str)
    
    # Calculate totals
    def total(rows): return sum(r.get('clicks', 0) for r in rows)
    def impressions(rows): return sum(r.get('impressions', 0) for r in rows)
    
    tw1, tw2 = total(data_7d), total(data_14d)
    tm1, tm2 = total(data_28d), total(data_56d)
    tm3a, tm3b = total(data_90d), total(get_sc_data(sc_url, start_56d, (today - timedelta(days=91)).strftime('%Y-%m-%d')))
    
    # Get affiliate data
    aff_data = get_affiliate_clicks()
    
    # Get top pages needing attention
    needs_seo = [r for r in data_7d if r.get('clicks', 0) > 5 and r.get('position', 0) > 10]
    
    # Build report
    report = {
        'generated': today_str,
        'site': site_name,
        'traffic': {
            '7_days': {'clicks': tw1, 'prev': tw2, 'var': f'{((tw1-tw2)/tw2*100):+.1f}%' if tw2 > 0 else 'N/A'},
            '28_days': {'clicks': tm1, 'prev': tm2, 'var': f'{((tm1-tm2)/tm2*100):+.1f}%' if tm2 > 0 else 'N/A'},
            '90_days': {'clicks': tm3a, 'prev': tm3b, 'var': f'{((tm3a-tm3b)/tm3b*100):+.1f}%' if tm3b > 0 else 'N/A'},
        },
        'top_pages': [(r.get('keys', [''])[0], r.get('clicks', 0), r.get('position', 0), r.get('ctr', 0)) 
                       for r in sorted(data_7d, key=lambda x: x.get('clicks', 0), reverse=True)[:20]],
        'affiliate': aff_data,
        'needs_seo': [(r.get('keys', [''])[0], r.get('clicks', 0), r.get('position', 0)) for r in needs_seo],
    }
    
    # Save report
    import os
    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(f'{REPORTS_DIR}/report-{today_str}.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    return report

def format_telegram_message(report, site_name):
    """Formata mensagem para Telegram."""
    msg = f"📊 *RELATÓRIO SEMANAL - {site_name}*\n"
    msg += f"📅 {report['generated']}\n\n"
    
    # Traffic summary
    t = report['traffic']
    msg += "🔍 *TRÁFEGO*\n"
    msg += f"• 7 dias: {t['7_days']['clicks']} cliques ({t['7_days']['var']})\n"
    msg += f"• 28 dias: {t['28_days']['clicks']} cliques ({t['28_days']['var']})\n"
    msg += f"• 90 dias: {t['90_days']['clicks']} cliques ({t['90_days']['var']})\n\n"
    
    # Top pages
    msg += "🏆 *TOP 10 PÁGINAS*\n"
    for i, (page, clicks, pos, ctr) in enumerate(report['top_pages'][:10], 1):
        page_short = page.replace('https://guiaculinaria.com.br/', '/')
        msg += f"{i}. {clicks} cliques | pos {pos:.1f} | {page_short[:35]}\n"
    
    # Affiliate
    aff = report['affiliate']
    if aff.get('total', 0) > 0:
        msg += f"\n🛒 *CLIQUES AFILIADOS:* {aff['total']}\n"
    
    # Alerts
    if report['needs_seo']:
        msg += f"\n⚠️ *PÁGINAS PRECISAM SEO:* {len(report['needs_seo'])}\n"
        for page, clicks, pos in report['needs_seo'][:5]:
            page_short = page.replace('https://guiaculinaria.com.br/', '/')
            msg += f"• {clicks} cliques | pos {pos:.1f} | {page_short[:35]}\n"
    
    return msg

if __name__ == '__main__':
    site = sys.argv[1] if len(sys.argv) > 1 else 'guiaculinaria.com.br'
    
    # Load config
    with open('/root/.openclaw/workspace/skills/site-analytics/config.json') as f:
        config = json.load(f)
    
    if site in config['sites']:
        site_config = config['sites'][site]
        report = generate_report(site_config, site)
        print(format_telegram_message(report, site_config.get('name', site)))
    else:
        print(f"Site {site} não encontrado na configuração")
        print(f"Sites disponíveis: {list(config['sites'].keys())}")