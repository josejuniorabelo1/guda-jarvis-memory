# 🗺 MAPA.md — Segundo Cérebro

**Repositório:** josejuniorabelo1/guda-jarvis-memory
**Proprietário:** José Júnio Rabelo
**Agente principal:** Jarvis (OpenClaw)
**Atualizado:** 2026-06-02

---

## 📍 Estrutura Geral

```
.
├── MAPA.md                  ← Você está aqui (índice geral)
├── empresa/                 ← Contexto global do negócio
│   ├── config.md           ← Proprietário, timezone, VPS
│   ├── clientes.md         ← Clientes externos (digitalser, etc.)
│   └── decisoes.md         ← Decisões estratégicas importantes
├── blogs/                   ← Cada blog = uma área de negócio
│   ├── README.md           ← Dashboard geral dos 5 blogs
│   ├── guiaculinaria/      ← Review produtos cozinha (Amazon + ML)
│   ├── portadavitamina/    ← Vitaminas (afiliado)
│   ├── bomsuplemento/      ← Suplementos (afiliado)
│   ├── iaconcurso/         ← IA + Concurso Público (afiliado)
│   └── cozinhadecorada/    ← Cozinha geral (afiliado)
├── skills/                  ← Automações reutilizáveis
│   ├── INDEX.md            ← Mapa de todas as skills
│   └── publicacao-automatizada/  ← Skill principal de artigos
├── rotinas/                 ← Crons e heartbeats documentados
│   └── INDEX.md            ← Mapa de todas as rotinas
├── templates/               ← Modelos reutilizáveis
│   └── artigo-review.md   ← Template de artigo review/afiliado
├── agentes/                 ← Configuração dos agentes
│   ├── jarvis.md           ← Jarvis (OpenClaw — agente principal)
│   └── guda.md             ← Guda (Hermes — legado/referência)
├── seguranca/               ← Permissões e políticas
│   └── acesso.md           ← Quem acessa o quê
├── knowledge/               ← Conhecimento absorvido (cursos, docs)
│   └── imersao-modulo1.md  ← Imersão OpenClaw nos Negócios — Dia 1
├── jarvis-memory.md         ← Memória do Jarvis (perfil + learnings)
├── guda-memory.md           ← Memória do Guda (perfil + learnings)
└── .env-blogs               ← Credenciais (NÃO versionado)
```

---

## 🧭 Como Navegar

| Preciso de... | Vá para... |
|---------------|------------|
| Visão geral dos blogs | `blogs/README.md` |
| Config de um blog específico | `blogs/[nome]/MAPA.md` |
| Como publicar artigos | `skills/publicacao-automatizada/SKILL.md` |
| Rotinas agendadas (crons) | `rotinas/INDEX.md` |
| Credenciais WordPress | `.env-blogs` (local, não versionado) |
| Template de artigo | `templates/artigo-review.md` |
| Contexto do negócio | `empresa/config.md` |
| Decisões importantes | `empresa/decisoes.md` |
| Conhecimento da imersão | `knowledge/imersao-modulo1.md` |

---

## 🔑 Regras do Repositório

1. **Toda pasta tem MAPA.md** — índice do que existe ali
2. **Credenciais NUNCA no repo** — usar `.env-blogs` (gitignore)
3. **Commits descritivos** — prefixo: feat/fix/docs/chore
4. **Skills documentadas** — toda skill tem SKILL.md com input/processo/output
5. **Rotinas documentadas** — todo cron tem entrada no `rotinas/INDEX.md`
