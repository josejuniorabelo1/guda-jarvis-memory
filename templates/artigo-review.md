# MODELO DE ARTIGO DE REVIEW DE ALTA CONVERSÃO (SEO & AFILIADOS)

## 1. CAMPOS DE METADADOS (Configuração no Yoast / RankMath)
* **Título SEO (Title Tag):** Até 64 caracteres. Palavra-chave primária obrigatoriamente no começo ou logo após palavras de força (Ex: "Melhores", "As 11").
* **Meta Description:** Entre 140 e 160 caracteres. Obrigatório conter a Palavra-chave Primária de forma fluida + uma CTA agressiva de vendas.
* **Slug / URL:** Apenas a palavra-chave separada por hífen. Exemplo: `melhores-xxxx-em-2026`

## 2. REGRAS E DIRETRIZES TÉCNICAS (Validação do Artigo)
* **Quantidade Mínima:** 900 palavras (conteúdo focado e direto, sem enrolação).
* **Tom de Voz:** Rigorosamente na 2ª pessoa ("Você"). Tom de excelente vendedor, formal, sem vícios de linguagem e focado em sanar as dores do cliente.
* **Densidade da Palavra-chave Primária:** Média de 1,5% do total do texto. Presença obrigatória no H1, no primeiro H2 (pós-tabela), diluído ao longo do conteúdo, em um H2 no meio do artigo, no H2 final e em pelo menos um H3.
* **Densidade da Palavra-chave Secundária:** Frequência moderada (dar "moral" a ela, sem exageros).
* **Links NoFollow:** Todos os botões em HTML e links de saída das tabelas comparativas devem conter `rel="nofollow"`.
* **Links Internos:** No máximo 2 links internos por artigo, direcionando para receitas, tutoriais ou guias complementares do próprio blog. **IMPORTANTE:** Em artigos em rascunho, NÃO inserir links internos — adicionar somente DEPOIS de publicar (evitar 404).
* **Links Externos:** No máximo 2 links externos por artigo.
* **Regra do Selo Único:** O termo "Melhor Custo-Benefício" só pode aparecer em UM único produto por artigo. Proibido repetir.
* **Simetria nos Bullet Points:** Prós e Contras devem ter rigorosamente a mesma quantidade de linhas (Ex: 3 prós e 3 contras).
* **Regra de Cauda Longa:** NUNCA repetir a keyword primária exata em múltiplos artigos do mesmo blog. Se já existe "xxx", criar variações: "xxx é boa", "xxx com yyy", "xxx para zzz", "melhor xxx para [contexto]".
* **Título:** Palavra-chave primária no começo do título (não necessariamente a 1ª palavra, mas nas primeiras posições). Desenvolver o tema no contexto do título (ex: se fala de "copa", desenvolver no ambiente de copa).

## 3. PADRÃO E FORMATO DAS IMAGENS
* **Imagem de Destaque:** Forte relação com a palavra-chave. Nome: `melhores-xxxx-em-2026.webp`. Alt Text = título do artigo.
* **Imagens Internas:** No mínimo 2 ao longo do artigo. Nomes otimizados (Ex: `detalhes-xxxx-2026.webp`).
* **Formato WebP:** Plugin obrigatório ativado (Converter for Media, WebP Express ou Imagify) para conversão automática.
* **Geração via API:** Usar Stability AI (STABILITY_AI_API_KEY no .env-blogs) para gerar imagens de destaque e internas.

## 4. ESQUELETO DO CONTEÚDO

### [H1] Título do Artigo (Até 64 chars com palavra-chave primária + força)
* Introdução: Parágrafo curto, direto e vendedor com foco em empatia e dor.

### [TABELA COMPARATIVA EM HTML]
* Modelo padrão de HTML limpo. Todos os botões configurados como NoFollow.

### [H2] Palavra-Chave Primária
* Texto markdown com a palavra-chave primária explícita e fluida nas primeiras linhas.

### [H2] Como Escolher o(a) Melhor [Nome da Categoria do Produto]
* Análise rápida de 3 a 4 critérios técnicos para gerar autoridade no Google Reviews System.

---

### BLOCO DE PRODUTOS INDIVIDUAIS (REPETIÇÃO SIMÉTRICA)

#### [H3] 1. Nome Completo do Produto - [Selo Exclusivo: Melhor Escolha Geral]
* [Imagem Interna Otimizada WebP]
* [Botão de Compra em HTML NoFollow]
* Texto descritivo detalhando o produto, benefícios práticos e indicação.
* **Prós:** (3 a 4 Bullet Points)
* **Contras:** (3 a 4 Bullet Points — mesma quantidade dos prós)

#### [H3] 2. Nome Completo do Produto - [Selo Exclusivo: Melhor Custo-Benefício]
* [Imagem Interna Otimizada WebP]
* [Botão de Compra em HTML NoFollow]
* Texto focado no custo-benefício inteligente.
* **Prós / Contras:** Mesma quantidade exata de linhas do produto anterior.

*(Repetir H3 para demais produtos. Selos variam: "Melhor Profissional", "Mais Durável", etc. NUNCA repetir Custo-Benefício.)*

---

### BLOCO DE FECHAMENTO E SEO TÉCNICO

### [H2] Palavra-Chave Secundária
* Texto focado em termos secundários que a persona busca com frequência.

### [H3] Subtópico Adicional com Palavra-Chave Primária ou Secundária
* Exploração de uma dor ou dúvida específica sobre o uso prático.

### [H2] Conclusão: Qual o Melhor [Palavra-Chave Primária]?
* Veredito final, resumido e imperativo para forçar o clique de compra.
* Inserir os links internos nesta seção ou no corpo do artigo.

---

### BLOCO DE PERGUNTAS FREQUENTES (SCHEMA FAQ)

### [H2] Perguntas Frequentes sobre [Categoria do Produto]
* **OBRIGATÓRIO:** Adicionar dentro do bloco nativo de FAQ do Yoast/RankMath para injetar JSON-LD.

#### [H4] Pergunta Frequente 1?
* Resposta curta e sem rodeios (máximo 3 linhas).

#### [H4] Pergunta Frequente 2?
* Resposta curta.

*(Mínimo 5-6 perguntas. Última focada na maior objeção: cartão/garantia/devolução.)*

---

## 5. NOTAS PARA ARTIGO INFORMACIONAL
* Mesma base do review, ajustando:
  - Sem tabela comparativa
  - Sem blocos de produtos individuais
  - Foco em resolver dúvida/dor com profundidade
  - Manter: H2, H3, FAQ, SEO, densidade de keywords, links internos (máx 2), links externos (máx 2), imagens WebP

## 6. AUTOR
* Publicar sempre como: **José Júnio**

## 7. GERAÇÃO DE IMAGENS
* API: Stability AI (chave no .env-blogs: STABILITY_AI_API_KEY)
* Gerar imagem de destaque + mínimo 2 internas
* Formato: WebP
* Nomenclatura: `keyword-principal-2026.webp`
