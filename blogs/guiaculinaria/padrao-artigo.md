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

### 0. REGRA MESTRA — SEMPRE antes de criar artigo do Guia Culinária

Antes de criar, corrigir ou subir qualquer artigo do **Guia Culinária**, ler este arquivo e seguir a ordem abaixo.

### 1. H1 / Title do WordPress — início real do artigo

O artigo deve começar visualmente pelo **H1**, que no WordPress é o **título do post**. Portanto:

- **Não inserir `<h1>` dentro do conteúdo**, para evitar H1 duplicado.
- O título/H1 precisa conter a palavra-chave principal + reforço de fundo de funil.
- Exemplos de formatos fortes:
  - `Como [palavra-chave]: Guia Completo para 2026`
  - `7 Melhores [palavra-chave] para Comprar em 2026`
  - `[palavra-chave] é Boa? Veja se Vale a Pena`
  - `[palavra-chave] para 2026: Como Escolher sem Errar`

### 2. CSS técnico — pode ficar injetado no início do conteúdo, mas não conta como estrutura visual

O CSS pode ser injetado no início do conteúdo por necessidade técnica do tema. Ele é invisível para o leitor; visualmente, quem abre o artigo deve ver primeiro o H1 do WordPress e logo depois a tabela comparativa.

```html
<style>
@media(max-width:768px){
  .compare-table thead th{display:none!important;}
  .compare-table td:not(:last-child):not(:nth-last-child(2)){display:none!important;}
  .compare-table{font-size:11px!important;}
}
</style>
```

### 3. TABELA COMPARATIVA (imediatamente após o H1, antes da introdução e antes de qualquer H2)
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

### 4. INTRODUÇÃO (2-3 parágrafos)
```html
<p>O número de pessoas que buscam praticidade... cresceu muito nos últimos anos.
Com isso, independentemente da idade, a prioridade é cuidar da saúde...</p>

<p>As fritadeiras sem óleo ganharam os Corações das pessoas e buscar a melhor
Air Fryer não garante apenas benefícios à saúde...</p>
```

### 5. ANÁLISES INDIVIDUAIS (um bloco por produto)

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

### 6. GUIA DE COMPRA — após os produtos

Depois das análises individuais, incluir sempre **2 ou 3 H2 informativos**, cada um com texto útil e, quando houver imagem disponível, **1 ou 2 imagens internas** no bloco correspondente.

```html
<h2>Como Escolher a Melhor [PRODUTO] em 2026</h2>
<p>Critérios organizados por importância: capacidade, potência, revestimento...</p>
<p>Mais critérios...</p>

<h2>[PALAVRA-CHAVE SECUNDÁRIA]: Vale a Pena?</h2>
<p>Texto de apoio com intenção comercial/informativa...</p>

<h2>O Que Comparar Antes de Comprar [PRODUTO]</h2>
<p>Texto de apoio com critérios objetivos...</p>
```

### 7. IMAGENS — WordPress, SEO e WebP

Todas as imagens usadas no artigo precisam estar salvas na **biblioteca de mídia do WordPress** antes da publicação.

Regras:
- Converter imagens para **WebP** sempre que possível.
- Nomear imagens com estrutura SEO.
- Imagem de destaque: baseada no **H1/title**.
- Imagens internas: baseadas no **H2** da seção onde aparecem.
- Produto na tabela e bloco individual: usar imagem real do produto, não placeholder, SVG ou imagem genérica.
- Se a imagem real do produto ainda não existir, marcar como **pendente** e não fingir produto com imagem ilustrativa.

Exemplo:
- H1: `Melhor Panela de Pressão Elétrica de 2026`
- Destaque: `melhor-panela-de-pressao-eletrica-2026.webp`
- H2: `Como escolher panela de pressão elétrica`
- Interna: `como-escolher-panela-de-pressao-eletrica.webp`

### 8. PERGUNTAS FREQUENTES (FAQ)
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
