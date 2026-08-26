#!/usr/bin/env python3
"""Genera index.html a partir del diseño más reciente (.dc.html) inyectando el
<head> con todo el SEO (seo/head.html). Así el SEO nunca se pierde aunque el
diseño se regenere desde Claude Design.

Uso:  python3 seo/build_index.py "Esmalte Studio v3.dc.html"
"""
import re
import sys
import pathlib

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "Esmalte Studio v3.dc.html")
head = pathlib.Path("seo/head.html").read_text(encoding="utf-8").strip()
html = src.read_text(encoding="utf-8")

# 1) Idioma del documento
html = re.sub(r"<html\b[^>]*>", '<html lang="es">', html, count=1)

# 2) Reemplazar TODO el <head> por el head SEO
html = re.sub(r"<head>.*?</head>", f"<head>\n{head}\n</head>", html,
              count=1, flags=re.S)

# 3) Quitar del <helmet> los tags SEO duplicados (title/description/og/twitter)
#    conservando fuentes y <style> (que llevan el CSS del diseño).
def clean_helmet(m):
    block = m.group(0)
    out = []
    for line in block.splitlines():
        s = line.strip()
        if (s.startswith("<title>")
                or 'name="description"' in s
                or 'property="og:' in s
                or 'name="twitter:' in s):
            continue
        out.append(line)
    return "\n".join(out)

html = re.sub(r"<helmet>.*?</helmet>", clean_helmet, html, count=1, flags=re.S)

pathlib.Path("index.html").write_text(html, encoding="utf-8")
print(f"index.html generado desde: {src.name}")
