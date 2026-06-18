# Guia Culinária — Padrão de Artigo Review/Afiliado

**Blog:** https://guiaculinaria.com.br
**Gerenciado por:** Jarvis (OpenClaw)
**Última atualização:** 2026-06-18

---

## ⚠️ CSS DO TEMA — Armadilha Importante

O tema do Guia Culinária impõe `background: var(--amazon-orange) !important` (laranja) nos botões
`.single-amazon-btn` e `.amazon-btn` via CSS inline no corpo do artigo.

**Solução:** Sempre que inserir botões de afiliado, usar ESTE estilo inline exato para sobrepor:

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

Além disso, injetar um `<style>` override no início do conteúdo do post:
```html
<style>
.single-amazon-btn,.amazon-btn,a.single-amazon-btn,a.amazon-btn{background:#000!important;box-shadow:none!important;}
</style>
```

---

## ✅ Estrutura Padrão de Artigo

### 1. INTRODUÇÃO (2-3 parágrafos)
- Resposta direta à pergunta/título
- Contextualização da categoria
- Promessa do que o artigo entrega

### 2. TABELA COMPARATIVA
```html
<table class="compare-table">
  <thead><tr><th>Produto</th><th>Especificações</th><th>Ação</th></tr></thead>
  <tbody>
    <tr>
      <td>
        <div class="product-info">
          <img src="..." alt="..." />
          <div class="product-details">
            <h3>Nome do Produto</h3>
            <span class="badge premium">Recomendada</span>
          </div>
        </div>
      </td>
      <td>
        <ul class="specs-list">
          <li>Marca: X</li>
          <li>Capacidade: X litros</li>
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
```

### 3. ANÁLISES INDIVIDUAIS (um bloco por produto)

**Estrutura obrigatória:**
```
<h3>N. Nome Completo do Produto</h3>

<div class="produto-destaque">
  <img src="..." alt="Nome do Produto" loading="lazy" />
  <br />
  <a class="amazon-btn" href="/go/XX" target="_blank"
     rel="nofollow noopener sponsored"
     style="display:inline-block!important;background:#000!important;color:#fff!important;
            padding:12px 18px!important;border-radius:6px!important;
            text-decoration:none!important;font-weight:700!important;
            text-align:center!important;line-height:1.2!important;
            box-shadow:none!important;">VER MELHOR PREÇO</a>
</div>

<p>Texto de análise SEO otimizado com contextualização do produto...</p>

<h4>Especificações</h4>
<ul>
  <li>Marca: X</li>
  <li>Capacidade: X litros</li>
  <li>Potência: XW</li>
  <li>Voltagem: 110V ou 220V</li>
  <li>Linha: X (se aplicável)</li>
  <li>Indicação: perfil ideal</li>
</ul>

<h4>Prós</h4>
<ul>
  <li>...</li>
</ul>

<h4>Contras</h4>
<ul>
  <li>...</li>
</ul>

<p><strong>Melhor para:</strong> frase de conclusão.</p>
```

**Ordem dentro do bloco:** H3 (nome) → imagem + botão preto → parágrafo intro → especificações → prós → contras → conclusão

### 4. GUIA DE COMPRA
```
<h2>Como escolher a melhor [PRODUTO]?</h2>
<p>Critérios organizados por importância...</p>
```

### 5. PERGUNTAS FREQUENTES (FAQs)
```
<h2>Perguntas frequentes</h2>

<h3>Pergunta 1?</h3>
<p>Resposta curta e direta.</p>
```

### 6. CONCLUSÃO
```
<h2>Conclusão</h2>
<p>Resumo + recomendação principal.</p>
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

**Nunca usar:** `single-amazon-btn` como class principal (tema força laranja nela).
Sempre usar `amazon-btn` que também precisa do override.

---

## 🔗 Links de Afiliado

- **Tag Amazon:** `josejuniorabe-20`
- **Shortlinks internos:** `/go/XX` (ex: `/go/df`, `/go/dg`)
- Plugins: Affiliate Link Manager, Pretty Links, ThirstyAffiliates

---

## 📁 Arquivos Relacionados

- `blogs/guiaculinaria/MAPA.md` — visão geral do blog
- `ESTRUTURA-ARTIGO.md` — estrutura geral (backup)
- Artigos de referência públicos:
  - https://guiaculinaria.com.br/fritadeira-eletrica-air-fryer/ (tabela comparativa + individuais)
  - https://guiaculinaria.com.br/fritadeira-airfryer-mondial/ (padrão Individual)
