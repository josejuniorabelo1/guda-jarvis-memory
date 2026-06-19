#!/usr/bin/env python3
import csv,json,os,re,html,unicodedata
from pathlib import Path
import requests
WP='https://guiaculinaria.com.br'; USER='Davi'; PWD=os.environ['GC_WP_PASS']
BASE=Path('/root/blog-generator'); CSV=BASE/'guda-memory/artigos-seruch-controle.csv'; OUT=BASE/'gc-qualidade-round2'; OUT.mkdir(exist_ok=True)
MEDIA_FILE=BASE/'gc-conteudos-corrigidos/media-map.json'
media_map=json.loads(MEDIA_FILE.read_text()) if MEDIA_FILE.exists() else {}
ACC={'Cafe ':'Café ','cafe ':'café ','Tres Coracoes':'Três Corações','tres coracoes':'três corações','Vacuo':'Vácuo','vacuo':'vácuo','Pratico':'Prático','Eletrica':'Elétrica','eletrica':'elétrica','Maquina':'Máquina','maquina':'máquina','Capsula':'Cápsula','capsula':'cápsula','Domestica':'Doméstica','domestica':'doméstica','Eletrico':'Elétrico','eletrico':'elétrico','Portatil':'Portátil','portatil':'portátil','Coracoes':'Corações','coracoes':'corações'}
def fix(s):
 s=s or ''
 for a,b in ACC.items(): s=s.replace(a,b)
 return s.replace(' de2026',' de 2026').replace('Caféteira','Cafeteira').replace('caféteira','cafeteira')
def titlecase(s):
 s=fix(s); small={'de','da','do','das','dos','a','o','e','em','na','no','para','com'}
 return ' '.join(w if i and w.lower() in small else w[:1].upper()+w[1:] for i,w in enumerate(s.split()))
def strong_title(r):
 kw=fix(r['KW1']); base=titlecase(kw)
 if r['TIPO']!='review':
  if r['SLUG']=='como-escolher-tamanho-cafeteira-italiana': return 'Como Escolher o Tamanho da Cafeteira Italiana: Guia para 2026'
  return f'{base}: Guia Prático para 2026'
 if ' é bom' in kw or ' é boa' in kw or ' e bom' in kw or ' e boa' in kw: return f'{base.replace(" e Bom"," É Bom").replace(" e Boa"," É Boa")}? Análise Completa em 2026'
 if kw.startswith('qual '): return f'{base}? Guia Completo para 2026'
 if 'melhor ' in kw: return f'{base} de 2026: Comparativo Completo'
 return f'{base}: Guia de Compra para 2026'
def prods(s): return [] if not s or s.strip()=='-' else [fix(x.strip()) for x in s.split('|') if x.strip()]
def p(t): return '<p>'+html.escape(t)+'</p>'
def li(items): return '<ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in items)+'</ul>'
STYLE='''<style>
.amazon-btn,a.amazon-btn{display:inline-block!important;background:#000!important;color:#fff!important;padding:12px 18px!important;border-radius:6px!important;text-decoration:none!important;font-weight:700!important;text-align:center!important;line-height:1.2!important;box-shadow:none!important;}
.amazon-compare-table{width:100%;overflow-x:auto;margin:20px 0}.compare-table{width:100%;border-collapse:collapse}.compare-table th,.compare-table td{border:1px solid #eee;padding:12px;vertical-align:top}.compare-table th{background:#f7f7f7}.produto-destaque{border:1px solid #e8e8e8!important;border-radius:14px!important;padding:24px!important;margin:18px 0 26px!important;background:#fff!important;text-align:center!important}.gc-produto-nome{font-size:17px!important;font-weight:700!important;color:#111!important;margin:0 0 16px!important}.gc-img-secao{margin:18px 0 24px;text-align:center}.gc-img-secao img{max-width:100%;height:auto;border-radius:10px}.gc-pendente{font-size:13px;color:#755;background:#fff7e6;border-left:4px solid #e0a331;padding:10px;margin:12px 0}
@media(max-width:768px){.compare-table thead th{display:none!important}.compare-table td:not(:last-child):not(:nth-last-child(2)){display:none!important}.compare-table{font-size:11px!important}.amazon-btn{display:block!important;width:100%!important;box-sizing:border-box!important}}
</style>'''
def btn(label): return f'<a class="amazon-btn" href="#link-afiliado-pendente" target="_blank" rel="nofollow noopener sponsored" style="display:inline-block!important;background:#000!important;color:#fff!important;padding:12px 18px!important;border-radius:6px!important;text-decoration:none!important;font-weight:700!important;text-align:center!important;line-height:1.2!important;box-shadow:none!important;">VER MELHOR PREÇO</a><!-- link afiliado pendente: {html.escape(label)} -->'
def img(m,alt): return f'<div class="gc-img-secao"><img src="{html.escape(m["url"])}" alt="{html.escape(alt)}" loading="lazy" /></div>' if m else ''
def meta(kw): return (f'{titlecase(kw)}: veja comparação, critérios de escolha, cuidados de compra e respostas objetivas para decidir com segurança em 2026.')[:158]
def table(r, ps):
 badges=['Melhor escolha','Mais vendido','Custo-benefício','Alternativa']
 h=['<div class="amazon-compare-table"><table class="compare-table"><thead><tr><th>Produto</th><th>Especificações</th><th>Ação</th></tr></thead><tbody>']
 for i,prod in enumerate(ps):
  specs=[f'Marca/modelo: {prod}', f'Categoria: {titlecase(r["CLUSTER"].replace("-"," "))}', 'Indicação: uso doméstico', 'Conferir antes da compra: voltagem, dimensões e garantia', 'Status: imagem real e link afiliado pendentes']
  h.append(f'<tr><td><div class="product-info"><div class="product-details"><h3>{html.escape(prod)}</h3><span class="badge">{badges[i] if i<len(badges) else "Opção"}</span></div><div class="gc-pendente">Imagem real do produto pendente. Entra aqui quando José enviar o link/produto.</div></div></td><td>{li(specs)}</td><td>{btn(prod)}</td></tr>')
 h.append('</tbody></table></div>')
 return '\n'.join(h)
def review(r):
 kw=fix(r['KW1']); kw2=fix(r['KW2']); ps=prods(r['PRODUTOS']); medias=media_map.get(r['SLUG'],[]); internal=medias[1:] # nunca repetir destaque no primeiro H2
 h=[STYLE, table(r,ps)]
 h.append(f'<h2>{html.escape(titlecase(kw))}: o que observar antes de comprar</h2>')
 h.append(p(f'Escolher {kw} exige mais do que olhar apenas preço e aparência. O melhor produto é aquele que resolve uma necessidade real na sua cozinha, cabe no espaço disponível, tem manutenção simples e não cria trabalho extra depois da compra. Por isso, este rascunho foi reorganizado para funcionar como um guia de decisão, com tabela comparativa no início, análise individual dos modelos e critérios objetivos para avaliar cada opção.'))
 h.append(p('Antes da publicação final, os botões precisam receber os links afiliados corretos e as imagens reais de produto devem substituir os avisos de pendência. Mesmo assim, a estrutura de compra já está pronta para receber esses dados sem quebrar o layout do artigo.'))
 h.append(p(f'Outro ponto importante é comparar produtos dentro da mesma proposta. No caso de {kw}, um modelo pode ser mais interessante pelo preço, outro pela marca e outro pela praticidade no uso diário. A escolha mais segura nasce do equilíbrio entre esses fatores.'))
 for i,prod in enumerate(ps):
  h.append(f'<h3>{html.escape(prod)}</h3>')
  h.append(f'<div class="produto-destaque"><div class="gc-pendente">Imagem real do produto pendente na biblioteca do WordPress.</div><p class="gc-produto-nome">{html.escape(prod)}</p>{btn(prod)}</div>')
  h.append(f'<h3>{html.escape(prod)} na prática</h3>')
  h.append(p(f'O {prod} entra na comparação como uma alternativa para quem busca {kw} com foco em uso doméstico. Ele deve ser analisado pelo conjunto da obra: reputação da marca, facilidade de uso, limpeza, garantia, avaliações recentes e compatibilidade com a rotina da casa. Quando o produto é usado com frequência, esses detalhes pesam mais do que um recurso chamativo no anúncio.'))
  h.append(p('Na hora de revisar este bloco para publicação, o ideal é confirmar ficha técnica no link final do produto. Assim, a tabela e o bloco individual passam a trazer potência, capacidade, material, voltagem e características específicas sem risco de informação genérica.'))
  h.append('<h4>Especificações a confirmar</h4>'+li(['Potência/capacidade oficial do anúncio','Voltagem disponível no produto escolhido','Dimensões e material de fabricação','Garantia e assistência da marca','Avaliações recentes de compradores']))
  h.append('<h4>Diferenciais esperados</h4>'+li(['Facilidade de uso no dia a dia','Boa relação entre preço e recursos','Limpeza simples após o uso','Compatibilidade com cozinhas domésticas']))
 h.append(f'<h2>Como escolher {html.escape(kw)} sem errar</h2>')
 if internal: h.append(img(internal[0], f'Como escolher {kw}'))
 h.append(p('Depois de comparar os modelos, pense primeiro no tipo de uso. Quem pretende usar o produto todos os dias deve priorizar resistência, limpeza fácil e garantia. Já quem pretende usar ocasionalmente pode escolher uma alternativa mais simples, desde que ela cumpra bem a função principal.'))
 h.append(p('Também é importante observar o espaço disponível. Produtos de cozinha que ficam difíceis de guardar acabam sendo menos usados. Se o item precisa sair do armário toda vez, o tamanho, o peso e a facilidade de montagem fazem diferença no longo prazo.'))
 h.append(p('Por fim, leia avaliações negativas com atenção. Elas mostram falhas recorrentes, ruído, aquecimento, fragilidade de peças ou dificuldade de limpeza. Uma avaliação isolada pode ser exceção, mas reclamações repetidas merecem cuidado.'))
 h.append(f'<h2>{html.escape(titlecase(kw2))}: critérios de compra</h2>')
 if len(internal)>1: h.append(img(internal[1], kw2))
 h.append(p(f'Quem pesquisa por {kw2} normalmente está mais perto da decisão de compra. Nessa etapa, compare preço final, frete, garantia e disponibilidade do produto. Um valor aparentemente menor pode deixar de compensar quando o frete é alto ou quando a marca tem pouca assistência.'))
 h.append(p('Outro critério é a clareza do anúncio. Produtos com ficha técnica completa, boas fotos, avaliações detalhadas e perguntas respondidas costumam oferecer mais segurança. Se o anúncio deixa dúvidas básicas, vale procurar outra opção antes de inserir o link final no artigo.'))
 h.append(f'<h2>Manutenção e durabilidade de {html.escape(kw)}</h2>')
 h.append(p('A durabilidade depende tanto da construção quanto do uso correto. Evitar sobrecarga, respeitar limites de capacidade e limpar logo após o uso são cuidados simples que preservam o desempenho. Em produtos elétricos, conferir voltagem antes da compra é indispensável.'))
 h.append(p('Para o leitor, essa seção ajuda a reduzir arrependimento. Muitas compras ruins acontecem porque a pessoa olha apenas preço e esquece de manutenção, reposição de peças e facilidade de limpeza. Um produto um pouco mais caro pode compensar se durar mais e exigir menos esforço.'))
 h.append(f'<h2>Qual {html.escape(kw)} combina melhor com sua rotina?</h2>')
 h.append(p(f'A decisão final sobre {kw} deve considerar frequência de uso, orçamento e nível de praticidade esperado. Se o objetivo é uso intenso, escolha o modelo com melhor construção e avaliações mais consistentes. Se o uso for eventual, priorize simplicidade e custo controlado.'))
 h.append(p('Antes de publicar, este rascunho ainda precisa receber os links afiliados reais e imagens de produto. Com esses dados inseridos, a comparação fica completa e pronta para orientar o leitor sem depender de promessas genéricas.'))
 h.append(f'<h2>Perguntas Frequentes sobre {html.escape(kw)}</h2>')
 faqs=[(f'Como escolher {kw}?','Compare capacidade, construção, garantia, avaliações recentes e custo final com frete.'),('O produto mais caro é sempre melhor?','Não. Ele só compensa quando os recursos extras fazem sentido para sua rotina.'),('O que revisar antes de publicar este artigo?','Inserir links afiliados reais, imagens de produto em WebP e ficha técnica confirmada.'),('Vale comparar avaliações negativas?','Sim. Elas mostram problemas recorrentes que nem sempre aparecem na descrição do anúncio.'),('Preciso conferir voltagem?','Sim, sempre que o produto for elétrico. Esse erro pode causar troca, devolução ou dano.')]
 for q,a in faqs: h.append(f'<h3>{html.escape(q)}</h3>'+p(a))
 return '\n\n'.join(h)
def info(r):
 kw=fix(r['KW1']); kw2=fix(r['KW2']); medias=media_map.get(r['SLUG'],[]); internal=medias[1:]
 h=[STYLE]
 h.append(f'<h2>{html.escape(titlecase(kw))}: passo a passo seguro</h2>')
 # sem imagem de destaque no primeiro H2
 h.append(p(f'Aprender {kw} ajuda a usar melhor o equipamento e evita erros comuns que reduzem o resultado. Mesmo quando o processo parece simples, pequenos detalhes fazem diferença: limpeza, quantidade correta, tempo de uso, montagem e cuidado ao guardar.'))
 h.append(p('Este guia foi ampliado para entregar uma explicação completa, com passo a passo, erros comuns e critérios práticos. A ideia é que o leitor consiga aplicar as orientações no dia a dia sem precisar procurar outro conteúdo para entender o básico.'))
 h.append('<ol><li>Confira se todas as peças estão limpas, secas e bem encaixadas.</li><li>Leia as instruções principais do fabricante antes do primeiro uso.</li><li>Use quantidade moderada para evitar vazamento, travamento ou mau funcionamento.</li><li>Faça um teste simples antes de usar em maior volume.</li><li>Depois do uso, limpe as partes removíveis e guarde tudo seco.</li></ol>')
 h.append(f'<h2>Cuidados importantes ao {html.escape(kw)}</h2>')
 if internal: h.append(img(internal[0], f'Cuidados ao {kw}'))
 h.append(p('O primeiro cuidado é não forçar o equipamento quando algo parece errado. Se uma peça não encaixa, se o botão não responde ou se o produto faz um ruído incomum, desligue e revise a montagem. Forçar pode transformar um ajuste simples em defeito real.'))
 h.append(p('Outro ponto é respeitar os limites de capacidade. Produtos de cozinha costumam funcionar melhor quando usados dentro da faixa recomendada. Excesso de água, café, gelo, alimento ou embalagem pode prejudicar o resultado e diminuir a vida útil.'))
 h.append(p('A limpeza também precisa ser feita logo após o uso. Resíduos secos grudam nas peças, favorecem cheiro ruim e podem afetar o funcionamento. Quando houver parte elétrica, nunca mergulhe o corpo do produto em água.'))
 h.append(f'<h2>{html.escape(titlecase(kw2))}: o que fazer quando não funciona como esperado</h2>')
 if len(internal)>1: h.append(img(internal[1], kw2))
 h.append(p(f'A dúvida sobre {kw2} geralmente aparece quando o resultado não sai como o esperado. Nesses casos, siga uma ordem simples: verifique energia, encaixes, quantidade usada, limpeza e tempo de funcionamento. Essa sequência resolve boa parte dos problemas sem improviso.'))
 h.append(p('Se o problema continuar, evite usar objetos pontiagudos, produtos químicos fortes ou calor excessivo. Essas soluções podem danificar peças plásticas, vedação, resistência ou componentes internos. O melhor caminho é procurar orientação do fabricante ou assistência.'))
 h.append(f'<h2>Erros comuns ao {html.escape(kw)}</h2>')
 h.append(li(['Ignorar o manual no primeiro uso','Usar quantidade acima do limite recomendado','Guardar peças úmidas ou sujas','Forçar travas, botões ou encaixes','Usar o produto em voltagem incorreta','Não fazer limpeza logo após o uso']))
 h.append(p('Esses erros parecem pequenos, mas se repetem muito na rotina. Corrigir apenas a limpeza e o armazenamento já melhora bastante a durabilidade do produto e a qualidade do resultado.'))
 h.append(f'<h2>Como manter o resultado consistente ao {html.escape(kw)}</h2>')
 h.append(p('Para manter consistência, crie uma rotina simples: preparar, usar, limpar, secar e guardar. Quando essa sequência vira hábito, o equipamento fica pronto para o próximo uso e apresenta menos falhas.'))
 h.append(p('Também vale anotar configurações que funcionam melhor para você, como quantidade, tempo e ajuste usado. Essa prática é útil especialmente em cafeteiras, máquinas de gelo e seladoras, porque pequenas variações mudam o resultado final.'))
 h.append(f'<h2>Quando revisar peças, limpeza e modo de uso</h2>')
 h.append(p('Faça uma revisão sempre que notar perda de desempenho, ruído diferente, vazamento, travamento ou resultado inconsistente. Muitas vezes o problema está em uma borracha mal encaixada, reservatório sujo, excesso de produto ou peça úmida.'))
 h.append(p('Se a revisão básica não resolver, procure suporte antes de insistir. Continuar usando um equipamento com defeito pode piorar o problema e aumentar o custo de reparo.'))
 h.append(f'<h2>Perguntas Frequentes sobre {html.escape(kw)}</h2>')
 faqs=[(f'{titlecase(kw)} é difícil?','Não. Com limpeza, encaixe correto e respeito ao limite do equipamento, o processo fica simples.'),('O que fazer se travar?','Desligue da tomada, espere alguns minutos e confira encaixes, limpeza e excesso de conteúdo.'),('Posso lavar todas as peças?','Não. Lave apenas as partes removíveis indicadas pelo fabricante e nunca mergulhe a parte elétrica.'),('Como evitar cheiro ou manchas?','Limpe logo após o uso, seque bem e guarde em local ventilado.'),('Quando procurar assistência?','Quando o problema continua depois de revisar energia, montagem, limpeza e modo de uso.')]
 for q,a in faqs: h.append(f'<h3>{html.escape(q)}</h3>'+p(a))
 return '\n\n'.join(h)
rows=list(csv.DictReader(open(CSV,encoding='utf-8'),delimiter=';'))
s=requests.Session(); s.get(WP+'/wp-login.php',timeout=20); lr=s.post(WP+'/wp-login.php',data={'log':USER,'pwd':PWD,'wp-submit':'Log In','redirect_to':WP+'/wp-admin/','testcookie':'1'},allow_redirects=False,timeout=20)
nonce=s.get(WP+'/wp-admin/admin-ajax.php?action=rest-nonce',timeout=20).text.strip(); headers={'X-WP-Nonce':nonce,'Content-Type':'application/json'}
drafts=s.get(WP+'/wp-json/wp/v2/posts',params={'status':'draft','per_page':100,'context':'edit'},headers=headers,timeout=40).json(); by={d['slug']:d for d in drafts}
result=[]
for r in rows:
 title=strong_title(r); content=review(r) if r['TIPO']=='review' else info(r); slug=r['SLUG']; post=by[slug]
 (OUT/f'{int(r["NUM"]):02d}-{slug}.html').write_text(content,encoding='utf-8')
 payload={'title':title,'content':content,'status':'draft','excerpt':meta(r['KW1']),'meta':{'rank_math_title':title[:64],'rank_math_description':meta(r['KW1']),'rank_math_focus_keyword':fix(r['KW1'])}}
 medias=media_map.get(slug,[])
 if medias: payload['featured_media']=medias[0]['id']
 resp=s.post(f'{WP}/wp-json/wp/v2/posts/{post["id"]}',headers=headers,json=payload,timeout=60)
 words=len(re.sub('<[^>]+>',' ',content).split())
 result.append({'slug':slug,'id':post['id'],'ok':resp.ok,'status_code':resp.status_code,'words':words,'title':title,'featured':payload.get('featured_media'), 'body':None if resp.ok else resp.text[:200]})
(OUT/'update-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'updated':sum(x['ok'] for x in result),'min_words':min(x['words'] for x in result),'under900':[x for x in result if x['words']<900], 'result':result},ensure_ascii=False,indent=2))
