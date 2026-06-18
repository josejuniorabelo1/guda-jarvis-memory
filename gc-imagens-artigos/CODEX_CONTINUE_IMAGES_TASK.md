# Continuar imagens Guia Culinária

Contexto:
- Pasta: `/root/blog-generator/guda-memory/gc-imagens-artigos/`
- Manifesto: `/root/blog-generator/guda-memory/gc-imagens-artigos/manifest.json`
- Já existem 21 imagens hero/capa geradas, uma por artigo.
- Existem 47 imagens pendentes marcadas com status diferente de `generated`.

Objetivo:
1. Ler o manifesto.
2. Gerar todas as imagens pendentes possíveis, usando o prompt de cada item.
3. Salvar cada arquivo exatamente no `path` indicado no manifesto.
4. Atualizar `status` para `generated`, com `generated_path` e `generated_at`.
5. Se alguma imagem não puder ser gerada, manter `pending_generation` e adicionar `blocker` claro.
6. Ao final, escrever resumo em `/root/blog-generator/guda-memory/gc-imagens-artigos/codex-continue-result.txt` com:
   - total de artigos
   - total de imagens
   - quantas geradas
   - quantas pendentes
   - lista de arquivos gerados
   - placeholders de produto ainda pendentes.

Importante:
- Sem texto embutido nas imagens.
- Estilo realista/editorial, adequado ao Guia Culinária.
- Não sobrescrever imagens hero existentes, a menos que seja necessário corrigir erro.
