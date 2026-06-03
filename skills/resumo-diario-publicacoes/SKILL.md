# Skill: Resumo Diário de Publicações

## O que faz
Todo dia às 18:30 BRT, envia relatório confirmando os artigos publicados no dia e os agendados para amanhã, de todos os blogs ativos.

## Quando usar
- Cron diário: **18:30 BRT** (21:30 UTC)
- Faz parte do resumo final do dia junto com todos os sites

## Blogs cobertos
- iaconcurso.com (2x/dia: 07:03 e 18:03)
- portaldavitamina.com.br (5x/dia: 08, 10, 12, 14, 16h)
- bomsuplemento.com.br (horários variáveis)
- guiaculinaria.com.br (sem agendamento fixo)
- cozinhadecorada.com.br (sem agendamento fixo)

## Passo a passo

### 1. Verificar posts publicados hoje (por blog)
- Consultar WP REST API: `GET /wp-json/wp/v2/posts?after=[hoje 00:00]&before=[hoje 23:59]&status=publish`
- Listar: título + URL + horário

### 2. Verificar agendados para amanhã (por blog)
- Consultar: `GET /wp-json/wp/v2/posts?status=future&after=[amanha 00:00]&before=[amanha 23:59]`
- Ou: total de posts `status=future` restantes

### 3. Alertar problemas
- Blog que deveria ter publicado mas não publicou
- Posts com erro de agendamento (missed schedule)
- Poucos posts restantes no agendamento (≤4 dias)

### 4. Entregar
- Mensagem Telegram consolidada
- Formato por blog:
  ```
  📝 [Blog] — Hoje: X publicados | Amanhã: Y agendados
    • Título 1 (URL)
    • Título 2 (URL)
  ```

## Dependências
- WordPress REST API (cookie auth ou Application Password)
- Credenciais em `/root/guda-jarvis-memory/.env-blogs`

## Output
- Mensagem Telegram com resumo do dia
