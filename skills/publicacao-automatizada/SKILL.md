# Skill: Publicação Automatizada de Artigos

## O que faz
Cria artigos de blog otimizados para SEO e afiliados, agenda publicação automática (2x/dia) e gerencia o fluxo de links de afiliado com o José Júnio.

## Quando usar
- Quando receber um CSV/lista de palavras-chave validadas (100+ views)
- Quando for hora de agendar novos artigos
- Quando precisar enviar lista de produtos para links de afiliado
- Palavras-gatilho: "cria artigo", "artigo para", "escreve artigo", "gera artigo", "novo artigo"

## Blogs ativos
- guiaculinaria.com.br (review produtos cozinha — Amazon + ML)
- bomsuplemento.com.br (suplementos — afiliado)
- portaldavitamina.com.br (vitaminas — afiliado)
- cozinhadecorada.com.br (cozinha geral — afiliado)
- iaconcurso.com (IA + concurso — afiliado/infoproduto)

## Autor
- Publicar sempre como: **José Júnio**

## Passo a passo

### 1. Receber keywords
- Fonte: CSV do Semrush (filtrado por 100+ views mensais)
- Ordenar da maior pesquisa para a menor
- Salvar em `blogs/[blog]/3-trafego/oportunidades-keywords.txt`

### 2. Criar artigos
- Seguir template: `templates/artigo-review.md`
- Estrutura obrigatória:
  - H1 com keyword primária no começo (não necessariamente 1ª palavra, mas nas primeiras posições) + gatilho forte
  - Meta description (140-160 chars) com CTA
  - Slug otimizado (keyword com hífens)
  - Tabela comparativa HTML (links nofollow) — apenas reviews
  - Blocos de produtos (prós/contras simétricos) — apenas reviews
  - Selo "Melhor Custo-Benefício" em apenas 1 produto
  - H2, H3 e FAQ obrigatórios em TODOS os artigos
  - Links internos: no máximo 2 por artigo
  - Links externos: no máximo 2 por artigo
  - FAQ com schema (mínimo 4, máximo 6 perguntas)
  - Imagens WebP (geradas via Stability AI)
- Artigos informativos: mesma base sem tabela/produtos
- Se couber infoproduto/ebook: avisar José Júnio antes

### 2.1 Regra de Títulos e Desenvolvimento
- Palavra-chave primária no começo do título
- Desenvolver o tema no contexto do título (ex: se fala de "copa", desenvolver no ambiente de copa)
- Título até 64 caracteres

### 2.2 Regra de Cauda Longa (Keywords)
- **NUNCA repetir a keyword primária exata** em múltiplos artigos do mesmo blog
- Se já existe artigo com "xxx", criar variações em cauda longa:
  - "xxx é boa"
  - "xxx com yyy"
  - "xxx para zzz"
  - "melhor xxx para [contexto]"
- Verificar keywords existentes antes de criar novo artigo

### 2.3 Regra de Links Internos em Rascunhos
- Artigos em rascunho: **NÃO** colocar links internos
- Adicionar links internos somente **DEPOIS** de publicar o artigo
- Motivo: links para posts não publicados geram 404

### 3. Agendar publicação
- Frequência: 2 artigos por dia
- Horários: 07:02 (manhã) e 18:02 (noite) — America/Sao_Paulo
- Duração: 25 dias corridos por lote
- Status inicial: rascunho → agendar com data/hora exata

### 4. Fluxo de links de afiliado
- **Toda segunda-feira às 08:00 (BRT):**
  - Enviar lista de produtos dos artigos de terça a segunda seguinte
  - Formato: nome do produto + artigo onde será usado
  - José Júnio retorna os links de afiliado
  - Jarvis insere nos artigos antes da publicação
- Artigos sem review (informativos): não precisam de links de produto
- Se couber infoproduto: avisar José Júnio para buscar link

### 5. Confirmação diária
- Todo dia às 18:30 (BRT): enviar relatório confirmando:
  - Artigos publicados no dia (título + URL)
  - Artigos agendados para amanhã
  - Problemas encontrados (se houver)

## Acesso aos blogs
- Método: Cookie login via wp-login.php + nonce REST API
- Credenciais: `/root/guda-jarvis-memory/.env-blogs`
- User: Davi (Administrador)
- Preferência futura: Application Passwords (mais estável)

## Geração de imagens
- API: Stability AI (key no .env-blogs)
- Formato: WebP
- Imagem de destaque: relacionada à keyword
- Imagens internas: mínimo 2 por artigo
- Nomenclatura: `keyword-principal-2026.webp`

## Output
- Artigos publicados no WordPress com agendamento
- Relatório diário às 18:30 via Telegram
- Lista semanal de produtos (segunda às 08:00)
- Keywords salvas no GitHub

## Dependências
- WordPress REST API (autenticado)
- Stability AI API (imagens)
- GitHub repo: guda-jarvis-memory
- Template: templates/artigo-review.md
