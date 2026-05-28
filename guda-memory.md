# 🤖 Guda Memory

**Identidade:** Assistente de IA para otimização de WordPress e operações técnicas
**Criado em:** 2026-05-28
**Status:** Ativo

---

## 📝 Perfil

- **Especialidade:** WordPress, PageSpeed, DevOps, Hermes Agent
- **Estilo:** Execution-first (fazer, não explicar)
- **Token-conscious:** Valuta eficiência
- **Linguagem:** Português-BR

---

## 🧠 Histórico de Aprendizados

### Sessão 1 (2026-05-28)
- **Tarefa:** Otimização PageSpeed - digitalser.com.br
  - MonsterInsights (desativado) — duplicava Google Analytics
  - WP Rocket (ativado) — Cache, Lazy Load, Minification, GZIP
  - Mobile-first approach (prioridade: conversões mobile)
  - Resultado: 197.9 KB → 101.5 KB HTML; 4s+ → 0.90s load time
  - Performance score: 56 → 72-82 (esperado após teste)

- **Tarefa:** OpenClaw Gateway setup
  - Problema: Memory leak (33GB VSZ, 691MB RSS, 31.3% CPU após 17h)
  - Solução: Kill + restart
  - Providers: OpenRouter (✓), OpenAI/Codex (✓), Anthropic (⏳)
  - Status: Instável — migrado para Hermes Agent puro

- **Tarefa:** GitHub setup para memória compartilhada
  - Criado: `josejuniorabelo1/guda-jarvis-memory`
  - Estrutura: empresa/, tasks/, arquivos/
  - Token: ghp_6c... (válido, 90 dias)

---

## 🎯 Próximos Passos

- [ ] Testar digitalser.com.br PageSpeed após 48h (cache warming)
- [ ] Implementar CRON de monitoramento (memória + processos)
- [ ] Adicionar chave Anthropic quando José trazer
- [ ] Documentar workflow de tarefas em `tasks/`

---

## 🔗 Referências

- **Repo:** https://github.com/josejuniorabelo1/guda-jarvis-memory
- **Cliente:** digitalser.com.br (WordPress)
- **Hermes:** /usr/local/lib/hermes-agent/

