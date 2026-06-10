# Estrutura de Artigo para Guia Culinária

## Template de Publicação

### Estrutura HTML do Artigo

```
1. CSS Styles (copiar do artigo de referência)
2. H1 Title - Palavra-chave primária forte
3. Tabela Comparativa (imagem + nome + especificações + botão)
4. H2 - Introdução com palavra-chave primária
5. Para cada produto:
   - H3 com nome do produto
   - div.gc-produto-afiliado (imagem + nome + botão)
   - H3 subtítulo do produto
   - Texto de review (mínimo 50-100 palavras por produto)
6. H2 - Palavra-chave secundária 1
7. Conteúdo relevante
8. H2 - Palavra-chave secundária 2
9. Conteúdo relevante
10. H2 - Conclusão (palavra-chave primária)
11. FAQ com schema.org
12. Meta description com palavra-chave
```

### Regras de SEO

- **Palavra-chave primária** em:
  - H1 (title)
  - 2+ H2
  - 1-2 H3
  - Primeiro parágrafo após H2
  - Meta description
  - Alt das imagens

- **Palavra-chave secundária** em:
  - 2-3 H2 adicionais
  - Conteúdo

- **Mínimo de palavras**: 900 (para 17 produtos, target 2500+)

- **Tabela**: imagem + nome + especificações + botão "VER MELHOR PREÇO"

- **gc-produto-afiliado**: imagem + nome + botão (dentro de cada H3 de produto)

### CSS Classes

```css
.amazon-btn, .btn-preco {
  background: #111 !important;
  color: #fff !important;
  border: 0 !important;
  border-radius: 8px !important;
  padding: 13px 18px !important;
  font-weight: 700 !important;
  text-align: center !important;
  text-decoration: none !important;
  line-height: 1.25 !important;
  display: inline-block !important;
}

.gc-produto-afiliado {
  border: 1px solid #e8e8e8 !important;
  border-radius: 14px !important;
  padding: 24px !important;
  margin: 18px 0 26px !important;
  background: #fff !important;
  box-shadow: 0 2px 10px rgba(0,0,0,.04) !important;
  text-align: center !important;
  max-width: 100% !important;
}

.gc-produto-img {
  width: 100% !important;
  max-width: 300px !important;
  height: 260px !important;
  object-fit: contain !important;
  margin: 0 auto 18px !important;
}

.gc-produto-nome {
  font-size: 17px !important;
  line-height: 1.35 !important;
  font-weight: 700 !important;
  color: #111 !important;
  margin: 0 0 16px !important;
}
```

### Exemplo de Meta Description

```
Melhores liquidificadores de 2026: compare 17 modelos das melhores marcas. 
Guia completo com reviews, preços e características para escolher o melhor 
liquidificador para sua cozinha. Verifique especificações, potência e custo-benefício.
```

### Exemplo de Título H1

```
Os 17 Melhores Liquidificadores de 2026: Potência, Custo-Benefício e Qualidade
```

### Exemplo de H2s

```
- Melhores liquidificadores: guia completo para escolher
- Como escolher o melhor liquidificador para sua cozinha
- Liquidificador bom e barato: vale a pena?
- Conclusão: qual o melhor liquidificador?
- Perguntas frequentes sobre liquidificadores
```

### Checklist de Publicação

- [ ] Título H1 com palavra-chave primária
- [ ] Meta description com palavra-chave (150-160 chars)
- [ ] Tabela comparativa após H1
- [ ] H2 introdutório com palavra-chave
- [ ] Cada produto: H3 + gc-produto-afiliado + texto
- [ ] Mínimo 900 palavras (target 2500+)
- [ ] 2+ H2 com palavra-chave primária
- [ ] 2-3 H2 com palavras-chave secundárias
- [ ] FAQ com schema.org
- [ ] Imagens com alt text otimizado
- [ ] Links com atributo rel="nofollow sponsored noopener"