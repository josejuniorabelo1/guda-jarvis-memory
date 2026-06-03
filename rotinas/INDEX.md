# 🔄 Rotinas — Índice

**Atualizado:** 2026-06-03

---

## Rotinas Ativas (Jarvis — OpenClaw)

| Rotina | Horário | O que faz | Entrega |
|--------|---------|-----------|---------|
| Heartbeat | A cada ~30min | Checa emails, posts publicados, depleção de agendados | Telegram (José Júnio) |
| Alerta depleção posts | Heartbeat | Se posts agendados acabam em ≤4 dias, alerta | Telegram |
| Notificação publicação | Heartbeat | Avisa quando artigo agendado vai ao ar | Telegram |
| Monitor afiliados Guia Culinária | Semanal (seg) | Verifica cliques, links, limpeza de artigos | Telegram |
| Análise de tráfego (todos os sites) | Semanal (seg 09:00 BRT) | GA4 + Search Console com detalhes por blog | Telegram |
| Resumo diário de posts publicados | Diário (18:30 BRT) | Confirma artigos do dia + agendados amanhã | Telegram |

---

## Rotinas de Publicação (Blogs)

| Blog | Horários de publicação | Status |
|------|----------------------|--------|
| Portal da Vitamina | 08:00, 10:00, 12:00, 14:00, 16:00 BRT | 🟢 Ativo (até 25/06) |
| IA Concurso | 07:03, 18:03 BRT | 🟢 Ativo |
| Guia Culinária | Sem agendamento fixo atual | ⏸ Manual |
| Bom Suplemento | Sem agendamento fixo atual | ⏸ Pendente |
| Cozinha Decorada | Sem agendamento fixo atual | ⏸ Pendente |

---

## Rotinas Legadas (Guda/Hermes — Referência)

| Job | Schedule | Função | Status |
|-----|----------|--------|--------|
| blogs-daily-traffic-sync | 6AM | Puxa GA + tráfego | ❌ Migrado para Jarvis |
| blogs-daily-audit | 12PM | Verifica links, speed | ❌ Não implementado |
| blogs-weekly-report | Seg 9AM | Relatório semanal | ❌ Não implementado |
| blogs-monthly-seo | 1º dia do mês | Análise SEO mensal | ❌ Não implementado |

---

## Como Documentar Nova Rotina

1. Adicionar entrada neste INDEX.md
2. Se for cron complexo, criar arquivo `rotinas/[nome].md` com detalhes
3. Commit com prefixo `feat: rotina [nome]`
