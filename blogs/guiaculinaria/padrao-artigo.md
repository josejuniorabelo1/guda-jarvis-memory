# Guia Culinária — Padrão de Artigo Review/Afiliado

**Blog:** https://guiaculinaria.com.br
**Gerenciado por:** Jarvis (OpenClaw)
**Última atualização:** 2026-06-09

---

## ✅ Estrutura Padrão de Artigo

Todo artigo review/afiliado deve seguir esta estrutura:

### 1. TABELA COMPARATIVA (no início, após introduçao)
```
| Produto | Indicação | Especificações | Preço |
|---------|-----------|----------------|-------|
```
- Formato: tabela HTML ou lista lado a lado
- Colunas: Produto, Indicação (ex: "Recomendada", "Custo-benefício"), Especificações, Botão
- Botão: `[VER MELHOR PREÇO](https://guiaculinaria.com.br/go/XX)`

### 2. INTRODUÇÃO (2-3 parágrafos)
- Resposta direta à pergunta/título
- Contextualização do produto/categoria
- Promessa do que o artigo entrega

### 3. ANÁLISES INDIVIDUAIS (um section por produto)
```
### N. Nome do Produto

[affiliatable id='XXXXX']

Texto de análise...

### Especificações
- Capacidade: X litros
- Potência: XW
- Voltagem: 110V ou 220V
- Modelo: XXXX

### Prós
- Lista de prós

### Contras
- Lista de contras

### Melhor para:
Frase de conclusão do perfil ideal
```

### 4. GUIA DE COMPRA (antes das FAQs)
```
## Como escolher o melhor [PRODUTO]?

Critérios organizados por importância:
1. Capacidade/tamanho
2. Potência
3. Voltagem
4. Tipo de painel/controles
5. Recursos extras
```

### 5. PERGUNTAS FREQUENTES (FAQs)
```
## Perguntas frequentes

### Pergunta 1?
Resposta curta e direta.

### Pergunta 2?
Resposta...
```

### 6. CONCLUSÃO
```
## Conclusão: vale a pena comprar [PRODUTO]?

Resumo + recomendação principal + verificação de voltagem/capacidade
```

---

## 🔗 Links de Afiliado

### Amazon
- Tag: `josejuniorabe-20`
- Formato curto: `amzn.to/XXXX`
- Plugins: Affiliate Link Manager, Pretty Links, ThirstyAffiliates

### Mercado Livre
- Links diretos do ML (ainda poucos, ~1-2 por site)
- Precisam ser convertidos paralinks de afiliado quando encontrados

### Shortlinks internos
- Padrão: `/go/XX` (ex: `/go/df`, `/go/dg`)
- Redirecionam para links externos de afiliado

---

## 📊 Elementos Visuais

### Botões de Afiliado
- Texto: **VER MELHOR PREÇO**
- Estilo: botão destacado, cor secundária do tema
- Posição: abaixo de cada análise de produto

### Tabela Comparativa
- Cabeçalho destacado
- Linhas alternadas (zebra)
- Botão na última coluna
- Responsivo (scroll horizontal em mobile)

### Cards de Produto
- Imagem à esquerda
- Nome + especificações à direita
- Badge de "Recomendada" / "Custo-benefício" quando aplicável
- Botão CTA no canto

---

## 🚀 Rotina de Atualização

1. José envia links de afiliado novos via Telegram
2. Jarvis atualiza posts existentes (CTA, shortlinks, tabelas)
3. Jarvis cria novos posts seguindo este padrão
4. Monitoramento: heartbeat a cada 4 dias (último post agendado)

---

## 📁 Arquivos Relacionados

- `blogs/guiaculinaria/MAPA.md` — visão geral do blog
- `blogs/guiaculinaria/rotina-monitoramento.md` — detalhes do heartbeat
- `blogs/guiaculinaria/afiliados-amazon.md` — tags e validações

---

## 🔧 Trello (pendente)
- API Key + Token: pendente de José
- Board principal: gerenciar fila de artigos