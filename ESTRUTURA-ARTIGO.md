# Estrutura de Artigo para Guia Culinária

## Template de Publicação

### Estrutura HTML do Artigo (ORDEM EXATA)

```
1. CSS Styles (copiar do artigo de referência)
2. H1 Title - NÃO REPETIR no H2; usar formato diferente (Como..., As nº..., ...é boa?)
3. Tabela Comparativa (IMEDIATAMENTE após H1 - antes de qualquer H2)
   - Imagem + Nome do produto + Badge (Melhor escolha/Mais vendido/Custo-benefício) + Especificações + Botão
4. H2 - Introdução (palavra-chave primária, título DIFERENTE do H1)
5. Texto introdutório (2-3 parágrafos) - palavra-chave primária no primeiro parágrafo
6. Para cada produto (17x):
   - H3 com nome do produto (sem "Review completo do" antes)
   - div.gc-produto-afiliado (imagem + nome + botão) - SOMENTE isso, sem H3 antes
   - H3 subtítulo (ex: "Review completo do [nome]")
   - Texto de review (mínimo 50-100 palavras por produto)
7. H2 - Palavra-chave secundária 1 + conteúdo (2-3 parágrafos)
8. H2 - Palavra-chave secundária 2 + conteúdo (2-3 parágrafos)
9. H2 - Palavra-chave secundária 3 + conteúdo (2-3 parágrafos)
10. H2 - Conclusão (palavra-chave primária no título)
11. FAQ com schema.org (4-5 perguntas)
```

### Regras de SEO

- **Palavra-chave primária** em:
  - H1 (title)
  - 2+ H2 (intro e conclusão)
  - 1-2 H3 (reviews)
  - Primeiro parágrafo após H2
  - Meta description

- **Palavra-chave secundária** em:
  - 3 H2 adicionais (potência, custo-benefício, mais vendidos, como escolher, etc)

- **Mínimo de palavras**: 900 (para 17 produtos, target 2500+)

### Exemplo Real - Geladeiras

**H1:** Melhores Geladeiras com Gelo na Porta

**Tabela (logo após H1):**
- Geladeira Electrolux Multidoor Efficient | Badge: Econônico | Especificações | [VER MELHOR PREÇO]
- Geladeira Brastemp French Door | Badge: Custo benefício | Especificações | [VER MELHOR PREÇO]
- Geladeira Panasonic Frost Free 480L | Badge: Oferta | Especificações | [VER MELHOR PREÇO]
- (... mais produtos ...)

**H2s:**
- "Melhores geladeiras com gelo na porta: guia completo para escolher" (intro com keyword)
- "Como escolher a melhor geladeira com gelo na porta" (secundária)
- "Vale a pena comprar geladeira com gelo na porta?" (secundária)
- "Conclusão" (keyword no título)

**H3s por produto:**
- H3: Geladeira Electrolux Multidoor
- div.gc-produto-afiliado (imagem + nome + botão)
- H3: Boa escolha para quem quer dispenser de água e gelo
- Texto: pontos positivos, pontos de atenção

### Meta Description

```
Melhores liquidificadores de 2026: compare 17 modelos das melhores marcas. 
Guia completo com reviews, preços e características para escolher o melhor 
liquidificador para sua cozinha. Verifique especificações, potência e custo-benefício.
```

### CSS Classes

```css
.amazon-btn, .btn-preco {
  background: #111 !important;
  color: #fff !important;
  border-radius: 8px !important;
  padding: 13px 18px !important;
  font-weight: 700 !important;
  text-align: center !important;
  text-decoration: none !important;
}

.gc-produto-afiliado {
  border: 1px solid #e8e8e8 !important;
  border-radius: 14px !important;
  padding: 24px !important;
  margin: 18px 0 26px !important;
  background: #fff !important;
  text-align: center !important;
}

.gc-produto-img {
  max-width: 300px !important;
  height: 260px !important;
  object-fit: contain !important;
  margin: 0 auto 18px !important;
}

.gc-produto-nome {
  font-size: 17px !important;
  font-weight: 700 !important;
  color: #111 !important;
  margin: 0 0 16px !important;
}
```

### Checklist de Publicação

- [ ] H1 com palavra-chave primária (formato: Como..., As nº..., ...é boa?)
- [ ] Meta description com palavra-chave (150-160 chars)
- [ ] Tabela comparativa IMEDIATAMENTE após H1 (antes de qualquer H2)
- [ ] Tabela com badges nos top 3 (Melhor escolha, Mais vendido, Custo-benefício)
- [ ] H2 introdutório com palavra-chave (título DIFERENTE do H1)
- [ ] Palavra-chave no primeiro parágrafo após H2
- [ ] Cada produto: H3 nome → div.gc-produto-afiliado (imagem+nome+botão) → H3 subtítulo → texto
- [ ] 3+ H2 com palavras-chave secundárias
- [ ] H2 conclusão com palavra-chave primária
- [ ] Mínimo 900 palavras (target 2500+ para 17 produtos)
- [ ] FAQ com schema.org
- [ ] Imagens com alt text otimizado
- [ ] Links com rel="nofollow sponsored noopener"

### Erros Comuns a Evitar

1. ❌ NÃO criar H1 duplicado
2. ❌ NÃO colocar tabela depois de H2 (deve ser logo após H1)
3. ❌ NÃO repetir H1 no H2 (usar título diferente)
4. ❌ NÃO colocar H3 antes da div.gc-produto-afiliado
5. ❌ NÃO criar review genérico igual para todos os produtos
