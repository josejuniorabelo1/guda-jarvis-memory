# Core Web Vitals — Guia Culinária

**Última atualização:** 2026-05-29
**Status:** Otimização em andamento

---

## Diagnóstico (29/05/2026)

### Antes da otimização
| Métrica | Valor |
|---------|-------|
| HTML total | 991 KB |
| CSS inline | 681 KB |
| CSS externo | 32 arquivos |
| JS externo | 23 arquivos |
| TTFB | 2.85s |
| Tempo total | 3.73s |
| Imagens | 47 (41 lazy) |
| posts_per_page | 100 |

### Após otimização
| Métrica | Valor |
|---------|-------|
| HTML total | 286 KB (-71%) |
| CSS inline | 48 KB (-93%) |
| CSS externo | 26 arquivos |
| JS externo | 24 arquivos |
| TTFB (melhor) | 0.63s (-78%) |
| TTFB (pior) | 4.3s (CDN DYNAMIC) |
| Imagens | 94 (41 lazy) |
| posts_per_page | 10 |

---

## Otimizações aplicadas
1. ✅ posts_per_page: 100 → 10
2. ✅ WP Rocket Minify CSS ativado
3. ✅ WP Rocket Lazyload imagens ativado
4. ✅ WP Rocket Defer JS + Delay JS (já estava)
5. ✅ Autoptimize desativado (conflitava com WP Rocket)
6. ✅ Cache limpo e regenerado

## Pendências
- ⚠️ CDN Hostinger não cacheia (DYNAMIC) → configurar no hPanel
- ⚠️ Remove Unused CSS (WP Rocket) → requer licença ativa
- ⚠️ 44 imagens JPG/PNG na home → converter pra WebP
- ⚠️ Home Elementor com 39 seções/57 widgets → simplificar
- ⚠️ Considerar Cloudflare pra cache de página

## Próxima verificação
- Segunda-feira 02/06/2026: rodar PageSpeed e comparar
