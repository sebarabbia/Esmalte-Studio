repo: sebarabbia/Esmalte-Studio
branch: main
sitio: https://esmaltestudio.com

## Cómo publicar una versión nueva
El diseño se edita en Claude Design y se exporta como `Esmalte Studio vN.dc.html`.
Para publicar (que no se pierda el SEO ni el favicon):

1. Copiar el/los video(s) a `videos/` si faltan (trabajo-1.mp4, trabajo-2.mp4, trabajo-3.mp4).
2. Generar el index con el SEO inyectado:
   ./build.sh "Esmalte Studio vN.dc.html"
3. git add -A && git commit && git push

`build.sh` toma el diseño y le inyecta el `<head>` de `seo/head.html` (título,
descripción, Open Graph, favicon y datos estructurados). Nunca editar el `<head>`
a mano en `index.html`: se regenera. Editar `seo/head.html` en su lugar.

## No borrar (necesarios para que el sitio funcione)
- `CNAME` -> dominio propio esmaltestudio.com (si se borra, se cae el dominio).
- `favicon.svg`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon-48x48.png`,
  `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` -> favicon.
- `og-image.png` -> vista previa al compartir el link. Regenerar con Chrome:
  Chrome --headless --window-size=1200,630 --screenshot=og-image.png seo/og-template.html
- `robots.txt`, `sitemap.xml`, `site.webmanifest` -> SEO.

## SEO
- Mercado objetivo: odontólogos de Latinoamérica y España (contenido en español).
- Palabras clave: redes sociales para clínicas dentales, contenido para
  odontólogos, marketing odontológico, community manager para dentistas.
- Pendiente del dueño: Google Search Console, Google Business Profile, backlinks.

## Screen map
| Pantalla | Archivos de origen |
| --- | --- |
| index.html | Esmalte Studio v3.dc.html + seo/head.html (via build.sh) |
| assets/, videos/ | del repo |
