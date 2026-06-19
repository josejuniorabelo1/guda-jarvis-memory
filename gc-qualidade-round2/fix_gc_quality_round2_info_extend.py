#!/usr/bin/env python3
import os,re,json,html,requests
WP='https://guiaculinaria.com.br'; USER='Davi'; PWD=os.environ['GC_WP_PASS']
extra='''
<h2>Como adaptar o passo a passo à sua rotina</h2>
<p>Nem toda cozinha funciona do mesmo jeito, então o ideal é adaptar o passo a passo ao seu ritmo. Se você usa o equipamento todos os dias, deixe as peças principais sempre limpas e acessíveis. Se usa poucas vezes por semana, guarde tudo seco e protegido para evitar poeira, umidade e cheiro acumulado.</p>
<p>Também vale criar um padrão próprio de uso. Defina a quantidade que costuma funcionar melhor, o tempo médio necessário e a ordem de montagem. Essa pequena organização evita testes repetidos e reduz a chance de erro quando você está com pressa.</p>
<p>Em equipamentos de café, gelo ou conservação de alimentos, a regularidade faz diferença. Usar água limpa, manter reservatórios higienizados e não ultrapassar limites de capacidade melhora o resultado e aumenta a vida útil do produto.</p>
<h2>Sinais de que você precisa ajustar o modo de uso</h2>
<p>Alguns sinais mostram que o processo precisa ser revisto: demora maior que o normal, ruído diferente, travamento, vazamento, cheiro forte, resultado fraco ou peças difíceis de encaixar. Quando isso acontece, não continue usando no automático. Pare, revise a montagem e faça uma limpeza completa.</p>
<p>Se o problema aparece logo após uma mudança de quantidade ou ingrediente, provavelmente o ajuste está no uso, não no equipamento. Reduza a carga, teste novamente e observe se o funcionamento volta ao normal.</p>
<p>Quando o problema persiste mesmo com uso correto, o melhor caminho é consultar o manual ou acionar assistência. Isso evita improvisos que podem danificar peças e comprometer a garantia.</p>
<h2>Checklist rápido antes de usar novamente</h2>
<ul><li>Peças removíveis limpas e secas.</li><li>Reservatório, recipiente ou compartimento dentro do limite indicado.</li><li>Produto ligado na voltagem correta.</li><li>Encaixes firmes, sem folgas ou travas forçadas.</li><li>Superfície estável, seca e segura.</li><li>Limpeza planejada logo após o uso.</li></ul>
<p>Seguindo esse checklist, você reduz erros simples e mantém o equipamento pronto para entregar um resultado mais previsível. Essa é a diferença entre usar o produto de vez em quando com dificuldade e realmente incorporar o aparelho à rotina da cozinha.</p>
'''
s=requests.Session(); s.get(WP+'/wp-login.php',timeout=20); s.post(WP+'/wp-login.php',data={'log':USER,'pwd':PWD,'wp-submit':'Log In','redirect_to':WP+'/wp-admin/','testcookie':'1'},allow_redirects=False,timeout=20)
nonce=s.get(WP+'/wp-admin/admin-ajax.php?action=rest-nonce',timeout=20).text.strip(); h={'X-WP-Nonce':nonce,'Content-Type':'application/json'}
slugs=['como-moer-cafe-na-hora-guia-definitivo','como-fazer-cafe-na-cafeteira-italiana','como-escolher-tamanho-cafeteira-italiana','como-usar-maquina-de-gelo-guia-completo','como-destravar-cafeteira-tres-coracoes','como-fazer-cafe-na-cafeteira-tres-coracoes','como-usar-seladora-a-vacuo']
drafts=s.get(WP+'/wp-json/wp/v2/posts',params={'status':'draft','per_page':100,'context':'edit'},headers=h,timeout=40).json(); by={d['slug']:d for d in drafts}
res=[]
for slug in slugs:
 p=by[slug]; raw=p['content']['raw']
 raw=raw.replace('<h2>Perguntas Frequentes', extra+'\n<h2>Perguntas Frequentes')
 r=s.post(f'{WP}/wp-json/wp/v2/posts/{p["id"]}',headers=h,json={'content':raw,'status':'draft'},timeout=60)
 words=len(re.sub('<[^>]+>',' ',raw).split())
 res.append({'slug':slug,'id':p['id'],'ok':r.ok,'words':words})
print(json.dumps(res,ensure_ascii=False,indent=2))
