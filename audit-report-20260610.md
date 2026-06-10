# Auditoria Completa — Guia Culinária
**Data:** 10/06/2026 | **Problema:** Conversão Amazon caiu de 1,93% (Q1) para 0,48% (Q2)

---

## 📊 Números do Trimestre

| Período | Cliques Amazon | Conversão | Taxa | Vendas |
|---|---|---|---|---|
| **Q1 (Jan-Mar)** | 1.142 | 22 | 1,93% | 22 |
| **Q2 (Abr-Jun)** | 839 | ~4 | 0,48% | ~4 |
| **Diferença** | **-26%** | **-82%** | **-75%** | **-82%** |

> ⚠️ Q2 do WordPress monitor mostra 1.222 cliques (amzn.to + go/). 
> A diferença de ~383 cliques = links diretos / social / bookmarks / não rastreados.

---

## 🔍 Diagnóstico — O Problema Não São os Links

**Links `amzn.to` funcionando corretamente** ✅
- Tag `josejuniorabe-20` presente em todos os redirecionamentos
- Todos os 568 links rastreados redirecionando para Amazon com comissão

**Links diretos Amazon — verificados:**
- Todos os artigos verificados têm tag de afiliado correta
- Nenhum link "quebrado" encontrado

---

## 🚨 Problemas Encontrados

### 1. **ARTIGOS COM ESTRUTURA INCOMPLETA (Impacto Alto)**

Artigos com links Amazon mas SEM tabela comparativa e SEM botão "VER MELHOR PREÇO":

| ID | Artigo | Links Amazon | Estrutura |
|---|---|---|---|
| 10497 | Melhores Air Fryers Forno | 22 links | ❌ Sem table, sem btn |
| 363 | Melhores Air Fryers Oven | 9 links | ❌ Sem table, sem btn |
| 10272 | Batedeira Britânia bbt350 | 1 link | ❌ Sem table, sem btn |
| 6936 | Batedeira Planetária Mondial 700w | 1 link | ❌ Sem table, sem btn |

**Impacto:** Visitantes chegam ao artigo, clicam em link de texto, vão para Amazon mas sem CTA claro. Conversão comprometida.

### 2. **QUEDA DE TRÁFEGO ORGÂNICO (Causa Principal)**

Cliques caíram 26% de Q1 para Q2. Possíveis causas:
- Alterações no algoritmo do Google (atualizações de 2026)
- Concorrentes crescendo no nicho
- Queries de produto com menos volume em Q2 (sazonalidade culinária)

### 3. **MIX DE TRÁFEGO MUDOU**

Os ~383 cliques não rastreados pelo amzn.to ( diferença entre monitor WP e Amazon) indicam:
- Links diretos no artigo (sem tag ou sem tracking)
- Tráfego social (Instagram, Pinterest, YouTube)
- Tráfego de search engines secundários (Bing, Yahoo, Baidu)

Esse tráfego "não rastreado" provavelmente converte pior (0,48%) do que o tráfego orgânico rastreado (1,93%).

---

## ✅ Artigos com Estrutura Correta

| ID | Artigo | amzn.to | Table | Buy Btn |
|---|---|---|---|---|
| 11197 | Melhores Panelas que Não Grudam | ✅ 14 | ✅ | ✅ |
| 435 | Melhores Marcas de Air Fryer | ✅ 28 | ✅ | ✅ |
| 6018 | Melhor Air Fryer Mondial | ✅ 10 | ✅ | ✅ |
| 5855 | Melhores Marcas de Liquidificador | ✅ 5 | ✅ | ✅ |
| 159 | Fritadeira Cadence | ✅ 10 | ✅ | ✅ |
| 153 | Melhor Fritadeira Elétrica com Óleo | ✅ | ✅ | ✅ |

---

## 📋 Ações Prioritárias (Ordenadas por Impacto)

### 🔴 PRIORIDADE 1 — Corrigir Artigos Sem Estrutura (IMEDIATO)

Os 4 artigos acima estão perdendo vendas por não terem tabela + botão. 
Cada artigo precisa de:
1. Tabela comparativa no topo
2. Botão "VER MELHOR PREÇO" em cada linha
3. CTA final

**Potencial de recuperação:** Se esses artigos voltarem a 1,93% de conversão, representam ~30+ cliques a mais por mês = ~R$150-400/mês em comissão.

### 🟡 PRIORIDADE 2 — Adicionar Tracking nos Links Diretos

Nem todos os links do site estão em `amzn.to`. Links diretos Amazon não são rastreados pelo GCAM. Considerar:
- Converter links diretos para `amzn.to` (manualmente ou via plugin)
- Adicionar UTM params nos links diretos

### 🟡 PRIORIDADE 3 — Aumentar Produção de Artigos

71 artigos atualizados em 2026. Com 289 artigos no total, muitos estão desatualizados e não ranqueiam. Foco em:
- Atualizar artigos antigos com dados de 2026
- Adicionar estrutura de afiliado em artigos que só têm links de texto

### 🟢 PRIORIDADE 4 — SEO e Tráfego

Queda de 26% nos cliques precisa ser investigada:
- Verificar posições no Google para keywords principais
- Comparar tráfego Q1 vs Q2 por artigo específico
- Considerar investir em backlinks

---

## 💰 Estimativa de Impacto

| Ação | Impacto Estimado |
|---|---|
| Corrigir 4 artigos sem estrutura | +R$150-400/mês |
| Converter links diretos para amzn.to | +R$50-100/mês |
| Atualizar 20 artigos antigos com estrutura | +R$200-500/mês |
| **Total potencial** | **+R$400-1.000/mês** |

---

## ❓ O que NÃO encontramos como causa

- ❌ Links `amzn.to` quebrados — funcionando OK
- ❌ Tag de afiliado faltando — todas OK
- ❌ Produtos fora de estoque — não verificado (requer verificação manual na Amazon)
- ❌ Preços muito altos — não verificado (requer comparação manual)

---

## 🗓️ Próximos Passos

1. [ ] Corrigir os 4 artigos sem tabela/botão (IDs: 10497, 363, 10272, 6936)
2. [ ] Verificar preços dos produtos mais clicados na Amazon (estoque + preço)
3. [ ] Listar todos os artigos com links diretos e converter para amzn.to
4. [ ] Acompanhar dados do GA4 a partir de hoje para ter métricas em tempo real
5. [ ] Revisar posicionamento no Google Search Console