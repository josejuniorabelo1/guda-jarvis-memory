#!/usr/bin/env python3
import csv, json, os, re, html, subprocess, mimetypes, unicodedata
from pathlib import Path
import requests

WP='https://guiaculinaria.com.br'
USER='Davi'
PWD=os.environ['GC_WP_PASS']
BASE=Path('/root/blog-generator')
CSV=BASE/'guda-memory/artigos-seruch-controle.csv'
IMGROOT=BASE/'guda-memory/gc-imagens-artigos'
OUT=BASE/'gc-conteudos-corrigidos'
OUT.mkdir(exist_ok=True)

ACCENTS={'Cafe ':'Café ','cafe ':'café ','Tres Coracoes':'Três Corações','tres coracoes':'três corações','Vacuo':'Vácuo','vacuo':'vácuo','Pratico':'Prático','Eletrica':'Elétrica','eletrica':'elétrica','Maquina':'Máquina','maquina':'máquina','Capsula':'Cápsula','capsula':'cápsula','Domestica':'Doméstica','domestica':'doméstica','E Boa':'É Boa','e Boa':'é Boa',' e boa':' é boa','Eletrico':'Elétrico','eletrico':'elétrico','Portatil':'Portátil','portatil':'portátil','Coracoes':'Corações','coracoes':'corações'}
def fix(s):
    s=s or ''
    for a,b in ACCENTS.items(): s=s.replace(a,b)
    return s.replace('Caféteira','Cafeteira').replace('caféteira','cafeteira').replace(' de2026',' de 2026')
def slugify(s):
    s=unicodedata.normalize('NFKD', fix(s)).encode('ascii','ignore').decode('ascii').lower()
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return re.sub('-+','-',s)
def title_case(s):
    s=fix(s); small={'de','da','do','das','dos','a','o','e','em','na','no','para','com'}
    return ' '.join(w if i and w.lower() in small else w[:1].upper()+w[1:] for i,w in enumerate(s.split()))
def strong_title(row):
    kw=fix(row['KW1']); base=title_case(kw)
    tipo=row['TIPO']; slug=row['SLUG']
    if tipo!='review':
        if kw.startswith('como '): return f'{title_case(kw)}: Guia Prático para 2026'
        return f'Como {base}: Guia Prático para 2026'
    if ' é bom' in kw or ' é boa' in kw or ' e bom' in kw or ' e boa' in kw:
        return f'{base}? Veja se Vale a Pena em 2026'
    if kw.startswith('qual '): return f'{base}? Guia Completo para 2026'
    if 'melhor ' in kw:
        return f'{base} de 2026: Veja as Opções que Valem a Pena'
    return f'{base}: Guia de Compra para 2026'
def products(prod): return [] if not prod or prod.strip()=='-' else [fix(p.strip()) for p in prod.split('|') if p.strip()]
def p(t): return '<p>'+html.escape(t)+'</p>'
STYLE='''<style>\n.amazon-btn,a.amazon-btn{display:inline-block!important;background:#000!important;color:#fff!important;padding:12px 18px!important;border-radius:6px!important;text-decoration:none!important;font-weight:700!important;text-align:center!important;line-height:1.2!important;box-shadow:none!important;}\n.amazon-compare-table{width:100%;overflow-x:auto;margin:20px 0;}\n.compare-table{width:100%;border-collapse:collapse;}\n.compare-table th,.compare-table td{border:1px solid #eee;padding:12px;vertical-align:top;}\n.compare-table th{background:#f7f7f7;}\n.gc-produto-afiliado{border:1px solid #e8e8e8!important;border-radius:14px!important;padding:24px!important;margin:18px 0 26px!important;background:#fff!important;text-align:center!important;}\n.gc-produto-img{max-width:300px!important;height:260px!important;object-fit:contain!important;margin:0 auto 18px!important;}\n.gc-produto-nome{font-size:17px!important;font-weight:700!important;color:#111!important;margin:0 0 16px!important;}\n.gc-img-secao{margin:18px 0 24px;text-align:center}.gc-img-secao img{max-width:100%;height:auto;border-radius:10px;}\n.gc-pendente{font-size:13px;color:#755;background:#fff7e6;border-left:4px solid #e0a331;padding:10px;margin:12px 0;}\n@media(max-width:768px){.compare-table thead th{display:none!important}.compare-table td:not(:last-child):not(:nth-last-child(2)){display:none!important}.compare-table{font-size:11px!important}.amazon-btn{display:block!important;width:100%!important;box-sizing:border-box!important}}\n</style>'''
def btn(label): return f'<a class="amazon-btn" href="#link-afiliado-pendente" target="_blank" rel="nofollow noopener sponsored" style="display:inline-block!important;background:#000!important;color:#fff!important;padding:12px 18px!important;border-radius:6px!important;text-decoration:none!important;font-weight:700!important;text-align:center!important;line-height:1.2!important;box-shadow:none!important;">VER MELHOR PREÇO</a><!-- link afiliado pendente: {html.escape(label)} -->'
def img_tag(media, alt, cls=''):
    if not media: return ''
    klass=f' class="{cls}"' if cls else ''
    return f'<img src="{html.escape(media["url"])}" alt="{html.escape(alt)}" loading="lazy"{klass} />'
def section_img(media, alt):
    return f'<div class="gc-img-secao">{img_tag(media, alt)}</div>' if media else ''

def login():
    s=requests.Session(); s.get(WP+'/wp-login.php',timeout=30)
    r=s.post(WP+'/wp-login.php',data={'log':USER,'pwd':PWD,'wp-submit':'Log In','redirect_to':WP+'/wp-admin/','testcookie':'1'},headers={'Cookie':'wordpress_test_cookie=WP+Cookie+check'},allow_redirects=False,timeout=30)
    if r.status_code not in (301,302): raise SystemExit(f'login failed {r.status_code}')
    nonce=s.get(WP+'/wp-admin/admin-ajax.php?action=rest-nonce',timeout=30).text.strip()
    return s, nonce

def convert_to_webp(src, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(src),'-vf','scale=1600:-1:force_original_aspect_ratio=decrease','-q:v','82',str(dest)],check=True)

def upload_media(s, nonce, file, title, alt):
    data=file.read_bytes()
    headers={'X-WP-Nonce':nonce,'Content-Disposition':f'attachment; filename="{file.name}"','Content-Type':'image/webp'}
    r=s.post(WP+'/wp-json/wp/v2/media',headers=headers,data=data,timeout=80)
    if not r.ok: raise RuntimeError(f'upload media failed {file}: {r.status_code} {r.text[:200]}')
    item=r.json(); mid=item['id']
    s.post(f'{WP}/wp-json/wp/v2/media/{mid}',headers={'X-WP-Nonce':nonce,'Content-Type':'application/json'},json={'title':title,'alt_text':alt,'caption':alt},timeout=30)
    return {'id':mid,'url':item['source_url'],'title':title,'alt':alt,'file':str(file)}

def upload_images(s, nonce, rows):
    cache_file=OUT/'media-map.json'
    cache=json.loads(cache_file.read_text()) if cache_file.exists() else {}
    for row in rows:
        slug=row['SLUG']
        if slug in cache: continue
        d=IMGROOT/slug
        # compatibility for one old folder name
        if not d.exists() and slug=='melhor-maquina-de-gelo-portatil': d=IMGROOT/'melhor-maquina-de-gelo-portatil'
        medias=[]
        if d.exists():
            imgs=sorted([x for x in d.iterdir() if x.suffix.lower() in ('.png','.jpg','.jpeg','.webp')])[:4]
            for idx,src in enumerate(imgs):
                if 'hero' in src.name.lower(): name=slugify(strong_title(row))
                elif idx==1: name=slugify('Como escolher '+fix(row['KW1']))
                elif idx==2: name=slugify('O que comparar antes de comprar '+fix(row['KW1']))
                else: name=slugify(src.stem)
                dest=OUT/'webp'/slug/f'{name}.webp'
                if src.suffix.lower()=='.webp': dest.write_bytes(src.read_bytes())
                else: convert_to_webp(src,dest)
                title=title_case(name.replace('-',' '))
                alt=fix(title)
                medias.append(upload_media(s,nonce,dest,title,alt))
        cache[slug]=medias
        cache_file.write_text(json.dumps(cache,ensure_ascii=False,indent=2),encoding='utf-8')
    return cache

def review(row, media):
    title=strong_title(row); kw=fix(row['KW1']); kw2=fix(row['KW2']); prods=products(row['PRODUTOS'])
    h=[STYLE]
    # Tabela imediatamente após o H1 do WordPress (conteúdo não repete H1)
    h.append('<div class="amazon-compare-table"><table class="compare-table"><thead><tr><th>Produto</th><th>Especificações</th><th>Ação</th></tr></thead><tbody>')
    badges=['Melhor escolha','Mais vendido','Custo-benefício','Alternativa']
    for i,prod in enumerate(prods):
        # Produto real ainda precisa de imagem própria; não usar imagem genérica como se fosse produto.
        pending='<div class="gc-pendente">Imagem real do produto pendente na biblioteca do WordPress.</div>'
        h.append(f'<tr><td><div class="product-info"><div class="product-details"><h3>{html.escape(prod)}</h3><span class="badge">{badges[i] if i<len(badges) else "Opção"}</span></div>{pending}</div></td><td><ul class="specs-list"><li>Categoria: {html.escape(title_case(row["CLUSTER"].replace("-"," ")))}</li><li>Indicação: uso doméstico</li><li>Critérios: praticidade, durabilidade e custo-benefício</li><li>Conferir: voltagem, dimensões, garantia e avaliações recentes</li></ul></td><td>{btn(prod)}</td></tr>')
    h.append('</tbody></table></div>')
    h.append(f'<h2>{html.escape(title_case(kw))}: guia rápido antes de comprar</h2>')
    if media: h.append(section_img(media[0], title))
    h.append(p(f'Comprar {kw} exige atenção porque o melhor modelo não é necessariamente o mais caro. O ideal é escolher uma opção que combine com a sua rotina, com o espaço disponível na cozinha e com a frequência de uso.'))
    h.append(p('A tabela acima ajuda você a comparar os principais modelos citados neste rascunho. Antes da publicação, os links afiliados e as imagens reais de produto precisam ser substituídos pelos materiais finais da biblioteca do WordPress.'))
    for prod in prods:
        h.append(f'<h3>{html.escape(prod)}</h3>')
        h.append(f'<div class="gc-produto-afiliado"><div class="gc-pendente">Imagem real do produto pendente na biblioteca do WordPress.</div><p class="gc-produto-nome">{html.escape(prod)}</p>{btn(prod)}</div>')
        h.append(f'<h3>Review completo do {html.escape(prod)}</h3>')
        h.append(p(f'O {prod} aparece como uma alternativa relevante para quem busca {kw} com foco em praticidade. Ele deve ser avaliado pelo conjunto: construção, facilidade de limpeza, reputação da marca, disponibilidade de assistência e avaliações recentes de compradores.'))
        h.append(p('Antes de decidir, compare o preço final com frete e confirme se o modelo atende ao volume de uso da sua casa. Esse cuidado evita pagar por recursos que você não usa ou comprar uma opção simples demais para a sua rotina.'))
    h.append(f'<h2>Como escolher {html.escape(kw)} em 2026</h2>')
    if len(media)>1: h.append(section_img(media[1], f'Como escolher {kw}'))
    h.append(p('Depois de analisar os produtos, observe capacidade, acabamento, facilidade de limpeza e garantia. Esses critérios costumam pesar mais no uso real do que recursos extras pouco usados.'))
    h.append(p('Também vale conferir se o produto cabe no local onde será usado ou guardado. Um modelo bom no papel pode se tornar inconveniente se ocupar espaço demais ou exigir limpeza trabalhosa.'))
    h.append(f'<h2>{html.escape(title_case(kw2))}: vale a pena?</h2>')
    if len(media)>2: h.append(section_img(media[2], kw2))
    h.append(p(f'A busca por {kw2} normalmente mostra uma intenção de compra mais avançada. Nesse ponto, vale comparar preço, reputação da marca e comentários de quem já usa o produto há algum tempo.'))
    h.append(p('Se a diferença de preço for pequena, priorize o modelo com melhor garantia, avaliações mais consistentes e características mais alinhadas ao seu uso diário.'))
    h.append(f'<h2>O que comparar antes de comprar {html.escape(kw)}</h2>')
    h.append(p('Compare sempre especificações equivalentes: capacidade com capacidade, potência com potência e recursos com recursos. Só assim a comparação deixa de ser apenas preço e passa a mostrar valor real.'))
    h.append(p('Em produtos de cozinha, durabilidade e limpeza simples costumam definir a satisfação depois da compra. Por isso, leia avaliações negativas também; elas revelam ruídos, limitações e problemas recorrentes.'))
    h.append(f'<h2>Conclusão: {html.escape(title_case(kw))} vale a pena?</h2>')
    h.append(p(f'{title_case(kw)} vale a pena quando você escolhe um modelo compatível com sua rotina e substitui a compra por impulso por comparação objetiva. Antes de publicar este artigo, faltam apenas inserir os links afiliados reais e as imagens reais dos produtos.'))
    h.append(f'<h2>Perguntas Frequentes sobre {html.escape(kw)}</h2>')
    for q,a in [(f'{title_case(kw)} vale a pena?','Vale quando o modelo atende sua rotina, tem boa garantia e preço competitivo.'),('Qual modelo escolher primeiro?','Comece pelo que tem melhor equilíbrio entre avaliações, garantia, capacidade e preço final.'),('Preciso comprar o mais caro?','Não. O mais caro só vale se os recursos extras forem úteis para você.'),('O que falta revisar antes de publicar?','Inserir links afiliados reais, imagens reais de produto em WebP e revisar preços/ disponibilidade.')]:
        h.append(f'<h3>{html.escape(q)}</h3>'); h.append(p(a))
    return title, '\n\n'.join(h)

def info(row, media):
    title=strong_title(row); kw=fix(row['KW1']); kw2=fix(row['KW2'])
    h=[STYLE]
    h.append(f'<h2>{html.escape(title_case(kw))}: guia prático</h2>')
    if media: h.append(section_img(media[0], title))
    h.append(p(f'Saber {kw} ajuda você a evitar erros comuns e usar melhor o equipamento. O processo costuma ser simples, mas exige atenção a limpeza, encaixes, quantidade correta e segurança.'))
    h.append(p('A seguir, veja um passo a passo objetivo para aplicar na rotina sem complicar. A ideia é deixar o conteúdo pronto para leitura e depois complementar com imagens internas em WebP quando necessário.'))
    h.append('<ol><li>Confira se o equipamento está limpo, seco e bem encaixado.</li><li>Respeite a quantidade indicada pelo fabricante.</li><li>Faça um teste curto antes de usar em maior volume.</li><li>Evite forçar peças, travas ou botões.</li><li>Finalize limpando e secando as partes removíveis.</li></ol>')
    h.append(f'<h2>Cuidados importantes ao {html.escape(kw)}</h2>')
    if len(media)>1: h.append(section_img(media[1], f'Cuidados ao {kw}'))
    h.append(p('O principal cuidado é não improvisar quando algo parece travado ou fora do normal. Desligue o equipamento, verifique encaixes e leia as instruções do fabricante antes de tentar novamente.'))
    h.append(p('Também é importante guardar tudo seco e limpo. Umidade e resíduos podem causar cheiro, manchas, ferrugem ou mau funcionamento ao longo do tempo.'))
    h.append(f'<h2>{html.escape(title_case(kw2))}</h2>')
    if len(media)>2: h.append(section_img(media[2], kw2))
    h.append(p(f'A dúvida sobre {kw2} costuma aparecer quando o resultado não sai como esperado. Nesses casos, revise energia, montagem, limpeza e quantidade usada antes de concluir que há defeito.'))
    h.append(p('Se o problema persistir mesmo após esses testes, o caminho mais seguro é procurar assistência ou suporte da marca, evitando danos maiores.'))
    h.append(f'<h2>Erros comuns ao {html.escape(kw)}</h2>')
    h.append('<ul><li>Ignorar o manual no primeiro uso.</li><li>Usar quantidade acima do limite.</li><li>Lavar partes elétricas diretamente na água.</li><li>Guardar peças úmidas.</li><li>Forçar funcionamento quando há travamento.</li></ul>')
    h.append(f'<h2>Conclusão: {html.escape(title_case(kw))} sem complicação</h2>')
    h.append(p(f'Agora você já sabe {kw} com mais segurança. Siga o passo a passo, respeite os limites do equipamento e mantenha a limpeza em dia para preservar o desempenho.'))
    h.append(f'<h2>Perguntas Frequentes sobre {html.escape(kw)}</h2>')
    for q,a in [(f'{title_case(kw)} é difícil?','Não. Com atenção aos encaixes e limites do equipamento, o processo fica simples.'),('O que fazer se travar?','Desligue da tomada, aguarde e confira limpeza, encaixes e excesso de conteúdo.'),('Posso lavar todas as peças?','Não. Lave apenas peças removíveis indicadas pelo fabricante.'),('Quando procurar assistência?','Quando o problema continua após testes básicos e limpeza correta.')]:
        h.append(f'<h3>{html.escape(q)}</h3>'); h.append(p(a))
    return title, '\n\n'.join(h)

def meta(kw):
    s=f'{title_case(kw)}: compare modelos, veja critérios de escolha, cuidados antes da compra e prepare o rascunho para publicar com segurança.'
    return s[:158]

rows=list(csv.DictReader(open(CSV,encoding='utf-8'), delimiter=';'))
s,nonce=login()

# Use already uploaded images if available; do not block structural correction on media uploads.
cache_file=OUT/'media-map.json'
media_map=json.loads(cache_file.read_text()) if cache_file.exists() else {}
# fetch drafts
headers={'X-WP-Nonce':nonce,'Content-Type':'application/json'}
drafts=s.get(WP+'/wp-json/wp/v2/posts',params={'status':'draft','per_page':100,'context':'edit'},headers=headers,timeout=40).json()
by_slug={d.get('slug'):d for d in drafts}
result=[]
for row in rows:
    slug=row['SLUG']; media=media_map.get(slug,[])
    title,content=(review(row,media) if row['TIPO']=='review' else info(row,media))
    (OUT/f'{int(row["NUM"]):02d}-{slug}.html').write_text(content,encoding='utf-8')
    post=by_slug.get(slug)
    if not post:
        result.append({'slug':slug,'ok':False,'error':'draft missing'}); continue
    payload={'title':title,'content':content,'status':'draft','excerpt':meta(row['KW1']),'meta':{'rank_math_title':title[:64],'rank_math_description':meta(row['KW1']),'rank_math_focus_keyword':fix(row['KW1'])}}
    if media: payload['featured_media']=media[0]['id']
    r=s.post(f'{WP}/wp-json/wp/v2/posts/{post["id"]}',headers=headers,json=payload,timeout=60)
    result.append({'slug':slug,'id':post['id'],'ok':r.ok,'status_code':r.status_code,'status':(r.json().get('status') if r.ok else None),'featured_media':media[0]['id'] if media else None,'media_count':len(media),'title':title,'body':None if r.ok else r.text[:200]})
(OUT/'update-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'updated':sum(1 for x in result if x['ok']),'total':len(result),'with_media':sum(1 for x in result if x.get('media_count',0)>0),'result':result},ensure_ascii=False,indent=2))
