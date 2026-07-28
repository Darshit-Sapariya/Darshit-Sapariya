import markdown, os

html = '<!DOCTYPE html><html><head>'
html += '<meta charset="UTF-8">'
html += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">'
html += '<style>body{padding:40px;max-width:900px;margin:auto}.markdown-body{background:#0D1117;color:#c9d1d9;padding:40px;border-radius:8px}</style>'
html += '</head><body><div class="markdown-body">'
html += markdown.markdown(open('README.md', encoding='utf-8').read(), extensions=['fenced_code', 'tables'])
html += '</div></body></html>'

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('preview.html created')
print('Open preview.html in browser to see rendered README')
