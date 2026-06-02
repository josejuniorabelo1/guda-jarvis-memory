# 🔐 Segurança — Controle de Acesso

**Atualizado:** 2026-06-02

---

## Agentes e Permissões

| Agente | Leitura | Escrita | Observações |
|--------|---------|---------|-------------|
| Jarvis (principal) | Todo o repo | Todo o repo | Agente do José Júnio |
| Guda (legado) | Todo o repo | Todo o repo | Inativo — referência |

---

## Credenciais

| O quê | Onde fica | Formato |
|-------|-----------|---------|
| WordPress (5 blogs) | `.env-blogs` (raiz, gitignored) | USER + PASS por blog |
| Stability AI | `.env-blogs` | API key |
| GitHub PAT | Embedded no remote URL | Token pessoal |
| Telegram Bot | OpenClaw config (`openclaw.json`) | Bot token |
| Claude API | OpenClaw config | API key Anthropic |

---

## Regras de Segurança

1. **Credenciais NUNCA no código** — tudo em `.env-blogs` ou variáveis de ambiente
2. **`.env-blogs` no .gitignore** — nunca versionado
3. **GitHub repo privado** — acesso só pelo token do José Júnio
4. **WordPress: user Davi** — conta de administrador dedicada
5. **Bot Telegram: allowlist** — só José Júnio pode interagir
6. **Rotação de tokens** — revisar a cada 90 dias (próxima: ago/2026)

---

## Camadas (Modelo Imersão OpenClaw)

### Camada 1 — Servidor
- ✅ VPS dedicada (vmid5150)
- ⚠️ Verificar: SSH key-only, Fail2ban, UFW
- ⚠️ Verificar: Gateway em localhost only

### Camada 2 — Agente
- ✅ dmPolicy: allowlist (só José Júnio)
- ✅ Credenciais em .env (não no código)
- ✅ requireMention em grupos

### Camada 3 — Processo
- ✅ Logs completos (OpenClaw)
- ✅ Memória no GitHub (versionado)
- ⚠️ Implementar: audit cron automático
- ⚠️ Implementar: rotação de tokens programada
