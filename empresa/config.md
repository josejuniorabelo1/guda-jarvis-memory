# 🏢 Empresa — Contexto Compartilhado

**Data:** 2026-05-28
**Status:** Setup inicial

---

## 📋 Informações Gerais

- **Proprietário:** José Junio Rabelo
- **Timezone:** America/Sao_Paulo (BRT)
- **Idioma:** Português-BR

---

## 💼 Clientes

### digitalser.com.br
- **Tipo:** WordPress
- **Status:** Em otimização PageSpeed
- **Admin User:** admin (reCAPTCHA desativado)
- **Cookies:** /tmp/wordpress_cookies.txt (sessão ativa)
- **KPI:** Mobile conversions (prioridade)
- **Performance Target:** 72-82 (após otimizações)

---

## 🎯 Projetos

### Projeto 1: Otimização PageSpeed - digitalser.com.br
- **Status:** Em progresso
- **Atividades Completas:**
  - ✅ Desativado MonsterInsights (duplicava Google Analytics)
  - ✅ Ativado WP Rocket com configurações agressivas
  - ✅ Limpeza de database (revisions, drafts, trash)
  - ✅ Mobile-first optimization
- **Próximos Passos:**
  - ⏳ Testar performance após cache warming (48h)
  - ⏳ Implementar monitoramento contínuo

---

## 🔧 Processos

### Otimização de WordPress
1. Desativar plugins duplicados (MonsterInsights, etc)
2. Ativar cache (WP Rocket com lazy load)
3. Minificar CSS/JS
4. Limpar database
5. Monitorar performance

### Monitoramento de Memória
1. CRON a cada 15min
2. Se MEM > 80% → kill + restart
3. Log em GitHub + Telegram alert

---

## 🔐 Credenciais & Tokens

⚠️ **Nenhuma credencial deve ser armazenada aqui!**
Usar `.env` ou arquivo protegido.

---

## 🔗 Recursos

- **Repos:** https://github.com/josejuniorabelo1/
- **Hermes Agent:** /usr/local/lib/hermes-agent/
- **VPS:** CentOS 8, GLIBC 2.17

