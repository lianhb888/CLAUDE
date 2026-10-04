import json, base64, pathlib, re
from questions import Q, STEPS
here = pathlib.Path(__file__).parent
root = here.parent
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
imgs = {"q71": "mediciones-guia.jpg", "q72": "fotos-posiciones.jpg"}  # archivos junto al index.html (carpeta deploy/)
logo = b64(root/"ref/design/logo-dark.png", "image/png")
qs = []
for q in Q:
    n,key,t,title,help_ = q[:5]
    d = {"n":n,"k":key,"t":t,"q":title,"h":help_}
    if len(q)>5:
        if isinstance(q[5], list): d["o"]=q[5]
        elif isinstance(q[5], dict):
            if "img" in q[5] or "lista" in q[5]: d.update(q[5])
            else: d["ex"]=q[5]
        else: d["img"]=q[5]
    qs.append(d)
N=len(qs); assert [q["n"] for q in qs]==list(range(1,N+1))
flat=[n for _,ss in STEPS for s in ss for n in s]; assert flat==list(range(1,N+1)), "pasos"
steps=[{"sec":sec,"qs":s} for sec,ss in STEPS for s in ss]
import re
def scope_css(css):
    out=[]; i=0
    while i<len(css):
        j=css.find('{',i)
        if j<0: out.append(css[i:]); break
        sel=css[i:j].strip()
        # find matching close brace
        d=1;k=j+1
        while d and k<len(css):
            d+= (css[k]=='{') - (css[k]=='}'); k+=1
        body=css[j+1:k-1]
        if sel.startswith('@media'): out.append(sel+'{'+scope_css(body)+'}')
        elif sel.startswith('@keyframes') or sel.startswith(':root'): out.append(sel+'{'+body+'}')
        elif sel.startswith('html,body'): out.append('html,body{margin:0;background:var(--bg)}')
        elif sel=='*': out.append('#hb-survey,#hb-survey *{box-sizing:border-box}')
        else: out.append(','.join('#hb-survey '+s.strip() if not s.strip().startswith('#hb-survey') else s.strip() for s in sel.split(','))+'{'+body+'}')
        i=k
    return '\n'.join(out)
html = (here/"template.html").read_text(encoding="utf-8")
m=re.search(r'<style>(.*?)</style>',html,re.S)
html=html[:m.start(1)]+'\n'+scope_css(m.group(1))+'\n'+html[m.end(1):]
def js(o): return json.dumps(o, ensure_ascii=False).replace("</","<\\/")
html = html.replace("/*QUESTIONS*/[]", js(qs)).replace("/*STEPS*/[]", js(steps)).replace("/*IMGS*/{}", js(imgs)).replace("__LOGO__", logo)
(root/"encuesta-inicial.html").write_text(html, encoding="utf-8")
headers = ["Fecha y hora"]+[q["k"] for q in qs if q["k"]]
(root/"sheet-encabezados.tsv").write_text("\t".join(headers)+"\n", encoding="utf-8")
print(len(steps),"pasos;",len(headers),"columnas;",len(html)//1024,"KB")
