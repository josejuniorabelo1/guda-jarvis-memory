# GTM — Como Configurar Passo a Passo

**Container:** GTM-PNRV7BKF
**Site:** https://guiaculinaria.com.br

---

## 📋 PASSO 1: Configurar Google Sheets (Webhook)

### Criar a Planilha
1. Abre Google Sheets → novo arquivo "GuiaCulinaria_Analytics"
2. Cria abas: `Pageviews`, `Cliques`, `Scroll`, `Conversoes`

### Criar o Apps Script
1. Menu → Extensões → Apps Script
2. Cola este código:

```javascript
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var tab = sheet.getSheetByName('Dados') || sheet.insertSheet('Dados');
  
  var data = JSON.parse(e.postData.contents);
  var row = [
    new Date(),
    data.event || '',
    data.eventCategory || '',
    data.eventAction || '',
    data.eventLabel || '',
    data.linkUrl || '',
    data.pageUrl || '',
    data.pageTitle || '',
    data.depth || ''
  ];
  
  tab.appendRow(row);
  return ContentService.createTextOutput('OK');
}
```

3. Salva (Ctrl+S)
4. Implantar → Nova implantação → tipo: **App da Web**
5. Quem pode acessar: **Qualquer pessoa**
6. Copia a URL (termina em `/exec`)

---

## 📋 PASSO 2: Importar Tags no GTM

### Acessar GTM
1. Vai em https://tagmanager.google.com
2. Seleciona container **GTM-PNRV7BKF**
3. Menu → Admin → Importar Container

### Tags a criar (manualmente):

#### TAG 1: GA4 Pageview
- Tipo: **Google Tag (GA4)**
- Measurement ID: seu ID GA4 (ex: G-XXXXXXXXXX)
- Trigger: **All Pages**

#### TAG 2: Clique Amazon
- Tipo: **Google Analytics: GA4 Event**
- Configuration Tag: GA4 (mesma da tag 1)
- Event Name: `click_amazon`
- Trigger: **Click - só links Amazon**

#### TAG 3: Clique Mercado Livre
- Tipo: **Google Analytics: GA4 Event**
- Configuration Tag: GA4 (mesma da tag 1)
- Event Name: `click_mercadolivre`
- Trigger: **Click - só links Mercado Livre**

#### TAG 4: Scroll Tracking
- Tipo: **Google Analytics: GA4 Event**
- Configuration Tag: GA4 (mesma da tag 1)
- Events: `scroll_25`, `scroll_50`, `scroll_75`, `scroll_100`
- Trigger: **Scroll Depth** (25%, 50%, 75%, 100%)

#### TAG 5: Webhook para Sheets
- Tipo: **Custom HTML**
- Cola o código abaixo (substitui URL pelo seu Apps Script URL):

```html
<script>
(function() {
  var WEBHOOK_URL = 'COLE_SEU_URL_AQUI';
  
  window.dataLayer = window.dataLayer || [];
  
  var originalPush = window.dataLayer.push;
  window.dataLayer.push = function(obj) {
    if (obj && obj.event) {
      fetch(WEBHOOK_URL + '?t=' + Date.now(), {
        method: 'POST',
        mode: 'no-cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
      });
    }
    return originalPush.apply(this, arguments);
  };
})();
</script>
```

---

## 📋 PASSO 3: Triggers

### Trigger: Click Amazon
- Tipo: **Click - All Elements**
- Condição: `Click URL` → `contains` → `amzn.to` OU `amazon.com.br`

### Trigger: Click Mercado Livre
- Tipo: **Click - All Elements**
- Condição: `Click URL` → `contains` → `mercadolivre`

### Trigger: Click Shortlinks
- Tipo: **Click - All Elements**
- Condição: `Click URL` → `starts with` → `/go/`

### Trigger: Scroll 25%
- Tipo: **Scroll Depth**
- Vertical scroll: **percent**
- Percentage: **25**

### Trigger: Scroll 50%, 75%, 100%
- Mesma coisa, muda só a %

---

## 📋 PASSO 4: Variáveis

### Ativar Built-in Variables:
1. Variáveis → Configurar
2. Marca: `Click URL`, `Click Text`, `Page Path`, `Page Title`, `Scroll Depth`

---

## 📋 PASSO 5: Publicar

1. Preview (testar com Chrome)
2. Se tudo funcionando → Submit → Publicar

---

## ✅ Resultado Esperado

| Evento | Descrição |
|--------|-----------|
| `pageview` | A cada página carregada |
| `click_amazon` | Click em link Amazon |
| `click_mercadolivre` | Click em link ML |
| `scroll_25` | Scroll 25% da página |
| `scroll_50` | Scroll 50% da página |
| `scroll_75` | Scroll 75% da página |
| `scroll_100` | Scroll até final |

Dados vão pro:
- **GA4** → relatórios padrão
- **Sheets** → planilha com todos os eventos

---

## 🔧 Onde eu entro?

Depois que você configurar, me passa:
1. URL do Apps Script
2. Measurement ID do GA4

Aí eu consigo ler a planilha Sheets e analisar os dados automaticamente. 🎯