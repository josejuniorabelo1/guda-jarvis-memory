# Jarvis Memory — Long-term Memory

**Última atualização:** 2026-06-21

---

## Credenciais e Acessos

### Google OAuth (Desktop App — novo!)
- **Client ID:** `922496577393-5uku1uiqmg5civ5ks2pb520f9q7iuoqa.apps.googleusercontent.com`
- **Client Secret:** `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`
- **Refresh Token:** `1//0fTjIWkhltZEBCgYIARAAGA8SNwF-L9IrtUnqpf-tMN0SubdnF9zlSSmk4D7e0XLpz91oIO0UKJuWsIAErWC-HeXKn0ytN14Ryj8`
- **Scopes:** webmasters.readonly + analytics.readonly + tagmanager.readonly
- **Token file:** `~/.openclaw/workspace/.gtm-token.json`
- **ATENÇÃO:** Refresh token não expira desde que o app não seja recriado

### Google Search Console (via OAuth)
- **Scopes:** webmasters.readonly (owner de 12 sites)
- **Sites gerenciados:**
  - sc-domain:guiaculinaria.com.br (owner)
  - https://portaldavitamina.com.br (owner)
  - https://bomsuplemento.com.br (owner)
  - https://iaconcurso.com (owner)
  - https://cozinhadecorada.com.br (owner)
  - sc-domain:mundoculinaria.com.br (owner)

### Google Analytics (via OAuth)
- **Account:** "Conta do Google Ads" (ID: 208277846)
- **Properties:**
  - GUIA CULINÁRIA (GA4)
  - portaldavitamina (GA4)
  - iaconcurso (GA4)
  - bom suplemento (GA4)
- **API:** analyticsadmin.googleapis.com (habilitada 2026-06-21)

### Google Tag Manager (via OAuth)
- **Contas acessíveis:**
  - guiaculinária (Account ID: 6357997271)
  - portadavitamina (Account ID: 6357990124)
  - IACONCURSO (Account ID: 6357996611)
- **Container:** GTM-PNRV7BKF (Guia Culinária)
- **Scopes:** tagmanager.readonly

### GitHub
- **Token:** `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`
- **Repo:** `https://github.com/josejuniorabelo1/guda-jarvis-memory`
- **Clone local:** `/root/guda-jarvis-memory`

### Trello
- **API Key:** `db6480c71704ebbef12b971fed76e30b`
- **Token:** `ATTA69010423becce794b978634c0acb154dbcf053a1e4b57889e1310f01e6b3df83DC855F47` (sem expiração)
- **Board produção:** https://trello.com/b/nXYc6ThE/guia-culin%C3%A1ria-produ%C3%A7%C3%A3o-de-conte%C3%BAdo

### Site Analytics Skill
- **Location:** `~/.openclaw/workspace/skills/site-analytics/`
- **Script:** `weekly-report.py`
- **Config:** `config.json` (sites monitorados)

### Credenciais WordPress
- **Cookie file:** `/tmp/gc_fresh.txt` (renovar quando expirar)
- **User:** Davi | **Pass:** `9429rMTOqC$g0dcpfE6R*L3c`
- **API Key:** `db6480c71704ebbef12b971fed76e30b`
- **Plugins:** Guia Afiliater, Amazon Affiliate Controller, Site Kit

### Portal da Vitamina
- **URL:** https://portaldavitamina.com.br
- **WP REST:** usuário `josejuniorabelo` (não "Jarvis-Vitamina")
- **App Password:** `ovfz M23s 3v8L xlIo ETR2 KZxX`

### IA Concurso
- **URL:** https://iaconcursos.com.br
- **Credenciais:** pendentes (acesso quebrado)

---

## Configurações de Monitoramento

### Alertas Semanais
- **Horário:** Toda segunda 4h (America/Sao_Paulo)
- **Relatório:** tráfego 7/28/90 dias, top páginas, cliques afiliados, alertas SEO
- **Cron job ID:** `3fca6231-8e5b-4bf1-87b9-1c851279ee82`

### Heartbeat Tasks
- Verificar posts agendados (Portal da Vitamina, IA Concurso)
- Alerta se posts acabarem em ≤4 dias
- Monitor semanal de afiliados do Guia Culinária

---

## Sites para Monitorar
| Site | Status | Prioridade |
|------|--------|------------|
| Guia Culinária | ✅ Ativo | Alta |
| Portal da Vitamina | ✅ Ativo | Alta |
| Bom Suplemento | ✅ Ativo | Alta |
| IA Concurso | ⚠️ Credenciais pendentes | Alta |
| Cozinha Decorada | ✅ Ativo | Média |

---

## Notas Importantes
- Amazon affiliate tag (Guia Culinária): `josejuniorabe-20`
- IA Concurso está pausado para novos posts (só manter os existentes)
- GTM tags ativas: GA4 Config + GA4 Events (scroll 25/50/75/100%, affiliate click, buy button click)
