# 🧠 Guda + Jarvis Memory — Cérebro Compartilhado

Sistema de memória compartilhada (Nível 3) para agentes autônomos Guda e Jarvis.

**Baseado em:** [Imersão OpenClaw — O Problema dos 3 Níveis de Memória](https://docs.openclaw.com/memory)

---

## 📁 Estrutura

```
.
├── guda-memory.md           # Memória pessoal de Guda (histórico, learnings)
├── jarvis-memory.md         # Memória pessoal de Jarvis (histórico, learnings)
├── empresa/                 # Contexto compartilhado da empresa
│   ├── clientes.md         # Clientes e relacionamentos
│   ├── projetos.md         # Projetos em andamento
│   ├── processos.md        # Processos e workflows
│   └── config.md           # Configuração global
├── tasks/                  # Registro de tarefas executadas
│   └── [YYYY-MM-DD]_task_name.md
└── arquivos/               # Arquivos de suporte
    └── [documentos]
```

---

## 🎯 Como funciona

1. **Agente (Guda/Jarvis) inicia uma tarefa**
   - Puxa contexto do GitHub
   - Executa a tarefa
   - Atualiza a memória

2. **Próximo agente acessa o repo**
   - Vê TODO o histórico
   - Usa learnings de outras executões
   - Não precisa reinventar a roda

3. **Histórico fica guardado**
   - Todos os commits = auditoria completa
   - Revert é fácil se algo der errado
   - Timeline clara de decisões

---

## 🔄 Fluxo de Commit

```bash
# Guda/Jarvis fazem uma tarefa
git pull origin main
# ... editar arquivos ...
git add .
git commit -m "feat: [task-type] Descrição da mudança"
git push origin main
```

---

## 🚀 Primeiros Passos

1. Clone este repo
2. Crie sua conta Guda/Jarvis em `guda-memory.md` e `jarvis-memory.md`
3. Defina a empresa em `empresa/config.md`
4. Comece a registrar tarefas em `tasks/`

---

**Status:** ✅ Pronto para usar
**Última atualização:** 2026-05-28
