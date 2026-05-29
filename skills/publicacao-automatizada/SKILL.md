# Skill: Publicação Automatizada de Artigos

## O que faz
Cria artigos de blog otimizados para SEO e afiliados, agenda publicação automática (2x/dia) e gerencia o fluxo de links de afiliado com o José Júnio.

## Quando usar
- Quando receber um CSV/lista de palavras-chave validadas (100+ views)
- Quando for hora de agendar novos artigos
- Quando precisar enviar lista de produtos para links de afiliado

## Blogs ativos
- guiaculinaria.com.br (review produtos cozinha — Amazon + ML)
- bomsuplemento.com.br (suplementos — afiliado)
- portaldavitamina.com.br (vitaminas — afiliado)
- cozinhadecorada.com.br (cozinha geral — afiliado)
- iaconcurso.com (IA + concurso — afiliado/infoproduto)

## Passo a passo

### 1. Receber keywords
- Fonte: CSV do Semrush (filtrado por 100+ views mensais)
- Ordenar da maior pesquisa para a menor
- Salvar em `blogs/[blog]/3-trafego/oportunidades-keywords.txt`

### 2. Criar artigos
- Seguir template: `templates/artigo-review.md`
- Estrutura obrigatória:
  - H1 com keyword primária (até 64 chars)
  - Meta description (140-160 chars) com CTA
  - Slug otimizado (keyword com hífens)
  - Tabela comparativa HTML (links nofollow)
  - Blocos de produtos (prós/contras simétricos)
  - Selo "Melhor Custo-Benefício" em apenas 1 produto
  - Mínimo 2 links internos
  - FAQ com schema (mínimo 5 perguntas)
  - Imagens WebP (geradas via Stability AI)
- Artigos informativos: mesma base sem tabela/produtos
- Se couber infoproduto/ebook: avisar José Júnio antes

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
