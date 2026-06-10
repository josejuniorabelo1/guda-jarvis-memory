# Jarvis Memory - Guia Culinária

Repositório de memória e configuração do Jarvis para o projeto Guia Culinária.

## Estrutura

- `skills/site-analytics/` - Skill de monitoramento de performance
- `audit-report-20260610.md` - Auditoria completa do site
- `traffic-comparison.json` - Dados comparativos de tráfego

## APIs Disponíveis

- **Google Search Console**: Trafego orgânico, posicoes, CTR
- **WordPress REST/XML-RPC**: Conteudo, atualizacoes
- **GCAM Monitor**: Cliques em links de afiliados
- **Google Tag Manager**: Eventos GA4 (pageview, scroll, cliques)

## Scripts

- `skills/site-analytics/weekly-report.py` - Relatorio semanal automatizado

## Config

Ver `skills/site-analytics/config.json` para sites monitorados.
