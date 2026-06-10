# Estrutura de Artigo para Guia Culinária

## Template de Publicação

### Estrutura HTML do Artigo (ORDEM EXATA)

```
1. CSS Styles (copiar do artigo de referência)
2. H1 Title - Palavra-chave primária forte
3. Parágrafo introdutório breve
4. Tabela Comparativa (imagem + nome + badge + especificações + botão)
5. H2 - Introdução com palavra-chave primária
6. Texto introdutório (2-3 parágrafos)
7. Para cada produto (17x):
   - H3 com nome do produto
   - div.gc-produto-afiliado (imagem + nome + botão)
   - H3 subtítulo do produto
   - Texto de review (mínimo 50-100 palavras por produto)
8. H2 - Palavra-chave secundária 1 + conteúdo
9. H2 - Palavra-chave secundária 2 + conteúdo
10. H2 - Palavra-chave secundária 3 + conteúdo
11. H2 - Conclusão (palavra-chave primária)
12. FAQ com schema.org
```

### Regras de SEO

- **Palavra-chave primária** "liquidificadores" em:
  - H1 (title)
  - 2+ H2 (intro e conclusão)
  - 1-2 H3 (reviews)
  - Primeiro parágrafo após H2
  - Meta description

- **Palavra-chave secundária** em:
  - 2-3 H2 adicionais (potência, custo-benefício, mais vendidos)

- **Mínimo de palavras**: 900 (para 17 produtos, target 2500+)

### Exemplo Real - Liquidificadores

**H1:** Os 17 Melhores Liquidificadores de 2026: Potência, Custo-Benefício e Qualidade

**H2s:**
- Melhores liquidificadores 2026: como escolher o ideal para sua cozinha
- Como escolher o melhor liquidificador: potencia e capacidade
- Liquidificador bom e barato: vale a pena?
- Liquidificadores mais vendidos e avaliados de 2026
- Conclusao: qual o melhor liquidificador de 2026?

**H3s por produto:**
- [Nome do produto]
- Review completo do [nome do produto]

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

- [ ] Título H1 com palavra-chave primária
- [ ] Meta description com palavra-chave (150-160 chars)
- [ ] Tabela comparativa após H1 (com badge nos top 3)
- [ ] H2 introdutório com palavra-chave
- [ ] Cada produto: H3 + gc-produto-afiliado + H3 + texto
- [ ] Mínimo 900 palavras (target 2500+)
- [ ] 2+ H2 com palavra-chave primária
- [ ] 3 H2 com palavras-chave secundárias
- [ ] FAQ com schema.org
- [ ] Imagens com alt text otimizado
- [ ] Links com rel="nofollow sponsored noopener"
