import markdown

with open("markdown_extraction.md",'r') as f:
  text=f.read()
  html=html+markdown.markdown(text,extensions=['tables'])
with open('resultat.html','w') as f:
 f.write(html)