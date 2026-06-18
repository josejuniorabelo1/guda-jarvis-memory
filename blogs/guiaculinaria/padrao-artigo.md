# Guia Culinária — Padrão de Artigo Review/Afiliado

**Blog:** https://guiaculinaria.com.br
**Gerenciado por:** Jarvis (OpenClaw)
**Última atualização:** 2026-06-18

---

## ⚠️ CSS DO TEMA — Armadilha Importante

O tema do Guia Culinária impõe `background: var(--amazon-orange) !important` (laranja) nos botões
`.single-amazon-btn` e `.amazon-btn` via CSS inline no corpo do artigo.

**Solução:** Sempre injetar um `<style>` no início do conteúdo E usar estilo inline nos botões:

```html
<style>
.single-amazon-btn,.amazon-btn,a.single-amazon-btn,a.amazon-btn{
  background:#000!important;box-shadow:none!important;
}
</style>
```

E no botão:
```html
<a class="amazon-btn" href="..." target="_blank" rel="nofollow noopener sponsored"
   style="display:inline-block!important;background:#000!important;color:#fff!important;
          padding:12px 18px!important;border-radius:6px!important;
          text-decoration:none!important;font-weight:700!important;
          text-align:center!important;line-height:1.2!important;
          box-shadow:none!important;">
  VER MELHOR PREÇO
</a>
```

**Nunca usar** `single-amazon-btn` como class principal.

---

## ✅ Estrutura Padrão de Artigo Review/Afiliado

### 1. CSS MOBILE (injetar no início do conteúdo)
```html
<style>
@media(max-width:768px){
  .compare-table thead th{display:none!important;}
  .compare-table td:not(:last-child):not(:nth-last-child(2)){display:none!important;}
  .compare-table{font-size:11px!important;}
}
</style>
```

### 2. TABELA COMPARATIVA (envolta em div amazon-compare-table)
```html
<div class="amazon-compare-table">
  <table class="compare-table">
    <thead>
      <tr><th>Produto</th><th>Especificações</th><th>Ação</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div class="product-info">
            <div class="product-details">
              <!-- H3 vem ANTES da img, dentro de product-details -->
              <h3>Nome do Produto</h3>
              <span class="badge">Recomendada</span>
            </div>
            <!-- IMG: usar URL real, NÃO placeholder SVG -->
            <img src="https://guiaculinaria.com.br/wp-content/uploads/ANO/mes/NOME-REAL-DO-ARQUIVO.jpg"
                 alt="Nome do Produto" decoding="async" />
          </div>
        </td>
        <td>
          <ul class="specs-list">
            <li>Marca: X</li>
            <li>Capacidade: X Litros</li>
            <li>Potência: XW</li>
            <li>Voltagem: 110V ou 220V</li>
            <li>Características: ...</li>
          </ul>
        </td>
        <td>
          <a class="amazon-btn" href="/go/XX" target="_blank"
             rel="nofollow noopener sponsored"
             style="display:inline-block!important;background:#000!important;color:#fff!important;
                    padding:12px 18px!important;border-radius:6px!important;
                    text-decoration:none!important;font-weight:700!important;
                    text-align:center!important;line-height:1.2!important;
                    box-shadow:none!important;">VER MELHOR PREÇO</a>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

**⚠️ ATENÇÃO — Armadilhas da tabela:**
- IMG: URL real completa (`https://guiaculinaria.com.br/...`), não placeholder SVG
- Se o lazy-load do tema gera SVG placeholder + `data-lazy-src`, substituir `src="svg..."` pela URL real e remover `data-lazy-src`
- Não usar `loading="lazy"` na tabela comparativa

### 3. INTRODUÇÃO (2-3 parágrafos)
```html
<p>O número de pessoas que buscam praticidade... cresceu muito nos últimos anos.
Com isso, independentemente da idade, a prioridade é cuidar da saúde...</p>

<p>As fritadeiras sem óleo ganharam os Corações das pessoas e buscar a melhor
Air Fryer não garante apenas benefícios à saúde...</p>
```

### 4. ANÁLISES INDIVIDUAIS (um bloco por produto)

**Estrutura obrigatória:**
```html
<h3>Nome Completo do Produto – Frase com Palavra-Chave SEO</h3>

<div class="produto-destaque">
  <img src="URL-REAL-DA-IMAGEM.jpg" alt="Nome do Produto" loading="lazy" />
  <p style="margin-top:12px;margin-bottom:4px;font-weight:700;">Nome do Produto</p>
  <a class="amazon-btn" href="/go/XX" target="_blank"
     rel="nofollow noopener sponsored"
     style="display:inline-block!important;background:#000!important;color:#fff!important;
            padding:12px 18px!important;border-radius:6px!important;
            text-decoration:none!important;font-weight:700!important;
            text-align:center!important;line-height:1.2!important;
            box-shadow:none!important;">VER MELHOR PREÇO</a>
</div>

<p>Texto SEO com contextualização, keywords, benefícios, citação da marca...</p>

<h4>Especificações</h4>
<ul>
  <li>Marca: X</li>
  <li>Modelo: XXXX</li>
  <li>Capacidade: X Litros</li>
  <li>Potência: XW</li>
  <li>Voltagem: 110V / 220V</li>
  <li>Cor: X</li>
  <li>Características: ...</li>
</ul>

<h4>Diferenciais</h4>
<ul>
  <li>Diferencial 1: explicação</li>
  <li>Diferencial 2: explicação</li>
  <li>Diferencial 3: explicação</li>
</ul>
```

**Ordem dentro do bloco:**
`H3 → produto-destaque (img + nome + botão preto) → texto SEO → especificações → diferenciais`

### 5. GUIA DE COMPRA
```html
<h2>Como Escolher a Melhor [PRODUTO] em 2026</h2>
<p>Critérios organizados por importância: capacidade, potência, revestimento...</p>
<p>Mais critérios...</p>
```

### 6. PERGUNTAS FREQUENTES (FAQ)
```html
<h2>Perguntas Frequentes sobre [PRODUTO]</h2>

<h3>Pergunta 1?</h3>
<p>Resposta curta e direta.</p>

<h3>Pergunta 2?</h3>
<p>Resposta...</p>

<!-- 5-6 perguntas no total -->
```

---

## 🎨 Botões de Afiliado — Padrão Definitivo

```html
<a class="amazon-btn" href="/go/XX" target="_blank"
   rel="nofollow noopener sponsored"
   style="display:inline-block!important;background:#000!important;color:#fff!important;
          padding:12px 18px!important;border-radius:6px!important;
          text-decoration:none!important;font-weight:700!important;
          text-align:center!important;line-height:1.2!important;
          box-shadow:none!important;">
  VER MELHOR PREÇO
</a>
```

---

## 🔗 Links de Afiliado

- **Tag Amazon:** `josejuniorabe-20`
- **Shortlinks internos:** `/go/XX` (ex: `/go/df`, `/go/dg`)
- Plugins: Affiliate Link Manager, Pretty Links, ThirstyAffiliates

---

## 📁 Arquivos Relacionados

- `blogs/guiaculinaria/MAPA.md` — visão geral do blog
- Artigos de referência públicos:
  - https://guiaculinaria.com.br/fritadeira-eletrica-air-fryer/ (padrão COMPLETO: tabela + 13 individuais + guia + FAQ)
  - https://guiaculinaria.com.br/fritadeira-airfryer-mondial/ (padrão Individual)
