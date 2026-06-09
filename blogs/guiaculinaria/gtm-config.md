# GTM — Google Tag Manager — Guia Culinária

**Container ID:** GTM-PNRV7BKF
**Site:** https://guiaculinaria.com.br
**Última atualização:** 2026-06-09

---

## 🎯 O que Rastrear (Planejado)

### 1. Pageviews
- Todas as páginas do site
- Categorias (reviews, guias, comparações)
- Páginas de produto específicas

### 2. Cliques em Botões de Afiliado
- Botão "VER MELHOR PREÇO" (Amazon)
- Botão "VER MELHOR PREÇO" (Mercado Livre)
- Clics nos shortlinks `/go/XX`

### 3. Scroll Profundidade
- 25%, 50%, 75%, 100%
- Identificar quanto usuário chega no conteúdo

### 4. Cliques em Links Externos
- Amazon (amzn.to, amazon.com.br)
- Mercado Livre (mercadolivre.com.br)
- Outros sites de afiliado

### 5. Engajamento
- Tempo na página
- Tempo até primeiro clique
- Cliques por sessão

### 6. Afiliados específicos
- Amazon: tag `josejuniorabe-20`
- Mercado Livre: links de afiliado ML
- Taxa de conversão (clique → compra)

### 7. SEO/Performance
- Core Web Vitals via GA4
- Page speed insights
- Console errors

---

## 📡 Integração com Sheets

### Planilha Google Sheets
- Cria planilha "GuiaCulinaria_GTM_Dados"
- Abas: Pageviews, Cliques, Scroll, Conversoes
- GTM envia dados via tag Custom HTML + Apps Script webhook

### Fluxo
```
GTM Tag → Fetch API → Google Apps Script → Google Sheets
```

---

## 🔧 Configuração Necessária

### Google Cloud (para OAuth - futuro)
1. Criar projeto em console.cloud.google.com
2. Habilitar Google Tag Manager API
3. Criar OAuth 2.0 credentials
4. Compartilhar com jarvis@openclaw (a definir)

### Google Sheets (Webhook - mais fácil)
1. Criar Apps Script no Google Sheets
2. Deploy como Web App
3. Passar URL para Jarvis
4. Jarvis configura GTM para enviar dados

---

## ✅ Status Atual

- [ ] Google Cloud OAuth (pendente)
- [ ] Google Sheets webhook (pendente)
- [ ] GTM Container JSON (a fazer)
- [ ] Tags no GTM (a fazer)
- [ ] Teste de rastreamento (a fazer)

---

## 📝 JSON do Container (a gerar)

O JSON será gerado para importação direta no GTM.