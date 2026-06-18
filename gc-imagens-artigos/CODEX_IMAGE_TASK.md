# Tarefa Codex — gerar imagens dos artigos Guia Culinária

Objetivo: gerar/preparar imagens para os 21 artigos em:
- `/root/blog-generator/guda-memory/gc-artigos-moedor-cafe/*.md`
- `/root/blog-generator/guda-memory/gc-artigos-cafeteira/*.md`
- `/root/blog-generator/guda-memory/gc-artigos-gelo/*.md`

Requisitos:
1. Para cada artigo, identificar a seção de imagens/prompts no Markdown.
2. Criar uma pasta por slug em `/root/blog-generator/guda-memory/gc-imagens-artigos/<slug>/`.
3. Gerar pelo menos:
   - imagem principal/hero/capa
   - imagens internas mencionadas no artigo, quando houver.
4. Estilo: foto editorial realista, alta qualidade, sem texto embutido, formato web, adequado ao Guia Culinária.
5. Nomear arquivos em kebab-case com sufixos claros: `hero`, `comparativo`, `passo-a-passo`, etc.
6. Criar/atualizar `/root/blog-generator/guda-memory/gc-imagens-artigos/manifest.json` com:
   - artigo
   - slug
   - caminho do markdown
   - imagens geradas
   - prompt usado
   - status
7. Corrigir ou sinalizar placeholders de produto `PLACEHOLDER_*_IMG` nos artigos:
   - `01-melhor-moedor-de-cafe.md`
   - `02-melhor-moedor-cafe-eletrico.md`
   - `06-moedor-cafe-tramontina-e-bom.md`
   - `21-melhor-maquina-de-gelo-portatil-2026.md`

Se não houver ferramenta real de geração de imagem disponível dentro do Codex, preparar todos os prompts finais e o manifesto de geração, deixando explícito o bloqueio.
