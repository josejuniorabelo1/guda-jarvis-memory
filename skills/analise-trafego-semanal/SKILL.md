# Skill: Análise de Tráfego Semanal

## O que faz
Coleta e reporta métricas de tráfego de todos os blogs via Google Analytics 4 e Google Search Console. Gera relatório detalhado por blog.

## Quando usar
- Toda **segunda-feira às 09:00 BRT** (cron semanal)
- Quando José Júnio pedir análise de tráfego de qualquer blog

## Blogs cobertos
- iaconcurso.com
- portaldavitamina.com.br
- bomsuplemento.com.br
- guiaculinaria.com.br
- cozinhadecorada.com.br

## Passo a passo

### 1. Coletar dados GA4 (por blog)
- Usuários únicos (7 dias)
- Sessões
- Pageviews
- Bounce rate
- Tempo médio na página
- Trend vs semana anterior (% crescimento/queda)

### 2. Coletar dados Search Console (por blog)
- Cliques totais (7 dias)
- Impressões
- CTR médio
- Posição média
- Top 5 keywords com mais cliques
- Top 5 páginas com mais impressões
- Keywords novas no top 20

### 3. Gerar relatório
- Formato: comparativo semana anterior
- Destaques: maiores ganhos e perdas
- Insights acionáveis (oportunidades)
- Atualizar arquivo `blogs/[blog]/3-trafego/analise-geral.md`

### 4. Entregar
- Enviar resumo consolidado via Telegram (José Júnio)
- Formato curto: 1 bloco por blog, métricas-chave + insight principal

## Dependências
- Google Analytics 4 API (OAuth token em `/root/.hermes/google_token.json`)
- Google Search Console API
- GA4 Property IDs configurados por blog

## Status atual
⚠️ **NÃO FUNCIONAL** — precisa de:
1. OAuth token configurado
2. GA4 Property IDs por blog
3. Search Console verificado para cada domínio

## Output
- Arquivo atualizado: `blogs/[blog]/3-trafego/analise-geral.md`
- Mensagem Telegram com resumo
