# Jarvis Memory — Long-term Memory

**Última atualização:** 2026-06-21

---

## Credenciais e Acessos

### Google OAuth (Desktop App)
- **Client ID:** ver `.gtm-token.json` local
- **Client Secret:** ver `.gtm-token.json` local
- **Refresh Token:** ver `.gtm-token.json` local
- **Scopes:** webmasters.readonly + analytics.readonly + tagmanager.readonly
- **Token file:** `~/.openclaw/workspace/.gtm-token.json`
- **⚠️ Secrets guardados localmente — NÃO commit deste arquivo**

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
- **Token:** guardado em variável local
- **Repo:** `https://github.com/josejuniorabelo1/guda-jarvis-memory`

### Trello
- **API Key:** `db6480c71704ebbef12b971fed76e30b`
- **Token:** guardado localmente
- **Board produção:** https://trello.com/b/nXYc6ThE/guia-culin%C3%A1ria-produ%C3%A7%C3%A3o-de-conte%C3%BAdo

### Site Analytics Skill
- **Location:** `~/.openclaw/workspace/skills/site-analytics/`
- **Script:** `weekly-report.py`

### Credenciais WordPress
- **Cookie file:** `/tmp/gc_fresh.txt`
- **User:** Davi
- **Plugins:** Guia Afiliater, Amazon Affiliate Controller, Site Kit

### Portal da Vitamina
- **URL:** https://portaldavitamina.com.br
- **WP REST:** usuário `josejuniorabelo`

### IA Concurso
- **URL:** https://iaconcursos.com.br
- **Credenciais:** pendentes

---

## Configurações de Monitoramento

### Alertas Semanais
- **Horário:** Toda segunda 4h (America/Sao_Paulo)
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
- GTM tags ativas: GA4 Config + GA4 Events (scroll 25/50/75/100%, affiliate click, buy button click)
- Secrets guardados localmente em `~/.openclaw/workspace/.gtm-token.json`
