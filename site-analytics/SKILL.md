# Site Analytics Skill

Monitora performance de sites de conteúdo afiliados usando Google Search Console API + WordPress.

## Configuração

### APIs necessárias:
- **Google Search Console**: scope `webmasters.readonly`
- **WordPress**: XML-RPC ou REST API (cookie de admin)
- **Google Analytics 4**: Measurement Protocol (eventos)

### Arquivo de credenciais:
```
/root/.openclaw/workspace/.gtm-token.json
```
Contém OAuth tokens para Search Console e GTM.

### Cookie WordPress:
```
/tmp/gc_fresh.txt
```

## Uso

### 1. Relatório Semanal (segunda 4h)

Executa análise completa de um site e envia resumo via Telegram:

```
python3 /root/.openclaw/workspace/skills/site-analytics/weekly-report.py --site guiaculinaria.com.br
```

### 2. Dados disponíveis

O relatório inclui:

| Métrica | Fonte | Descrição |
|---|---|---|
| Tráfego orgânico | Search Console | Cliques, impressões, CTR, posição |
| Top páginas | Search Console | 20 páginas mais acessadas |
| Top queries | Search Console | 20 consultas mais comuns |
| Cliques afiliados | WordPress (GCAM) | Links Amazon/ML com mais cliques |
| Artigos sem estrutura | WordPress REST | Páginas com link mas sem tabela/botão |
| Alertas críticos | Múltiplas | Páginas com tráfego mas posição ruim |

### 3. Alertas gerados

| Tipo | Condição | Ação |
|---|---|---|
| Posição ruim | CTR > 1% mas posição > 10 | Revisar SEO/meta |
| Sem conversão | +5 cliques mas 0 vendas | Verificar links/tag |
| Artigo órfão | Tráfego alto sem CTA | Adicionar tabela/botão |
| Velocidade | PageSpeed < 50 | Otimizar imagens/code |

## Estrutura de arquivos

```
skills/site-analytics/
  SKILL.md           # Este arquivo
  weekly-report.py   # Script do relatório semanal
  config.json        # Config de sites monitorados
  reports/           # Relatórios gerados (YYYY-MM-DD.json)
```

## Extensão para novos sites

Para adicionar um novo site:

1. Autorizar Search Console no mesmo projeto GCP
2. Adicionar URL em `config.json`
3. Testar com: `python3 weekly-report.py --site novo-site.com.br`

