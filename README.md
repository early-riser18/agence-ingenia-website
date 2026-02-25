# Agence Ingenia — Codebase structure (LLM-oriented)

Static marketing site for Agence Ingenia. Built with **Jinja2** templates, **Tailwind CSS**, and a **Python build script**. Output is plain HTML/CSS/JS; no frontend framework.

## Directory layout

```
agence-ingenia-website/
├── build_pages.py          # Build script: Jinja2 render + optional file watcher
├── tailwind.config.js      # Tailwind config
├── package.json            # npm: tailwindcss (build scripts for CSS)
├── index.html              # Built output (currently from EN template)
├── en/index.html           # English locale page (if built separately)
├── fr/index.html           # French locale page (if built separately)
├── CNAME                   # GitHub Pages custom domain
├── src/
│   ├── templates/          # Jinja2 page templates
│   │   ├── index_en.html   # English index (includes partials)
│   │   └── index_fr.html   # French index (includes partials)
│   ├── partials/           # Reusable HTML fragments per locale
│   │   ├── en/             # English: head, header, footer, section_*.html
│   │   └── fr/             # French: same structure
│   │   └── video_prezi_overlay.html  # Shared (no locale)
│   ├── input.css           # Tailwind source
│   ├── output.css          # Compiled CSS (generated)
│   ├── utils.js            # Client JS (scroll, use-cases loading)
│   ├── use-cases_en.json   # Use-case copy + assets (EN)
│   └── use-cases_fr.json   # Use-case copy + assets (FR)
└── assets/                 # Static media
    ├── favicon/
    ├── use_cases/screenshots/
    ├── customers_pictures/
    ├── ai_assistant_feature/
    └── *.mp4, *.svg, *.jpg, etc.
```

## Build flow

1. **CSS**: `npm run build` (or `build:prod` for minified) runs Tailwind: `src/input.css` → `src/output.css`.
2. **HTML**: `python build_pages.py` loads Jinja2 with `FileSystemLoader("src")`, renders `templates/index_en.html` (see `pages` and `output_page` in script) to `index.html`. Optional: pass a directory path to watch for changes and rebuild on save.

**Note**: The script currently builds only one page (`index_en.html` → `index.html`). French and locale-specific outputs (`fr/index.html`, `en/index.html`) may be produced by extending `pages`/output paths in `build_pages.py` or by another process.

## Key files for edits

| Goal | Files |
|------|--------|
| Page structure / sections | `src/templates/index_*.html` (which partials are included) |
| Section content (EN/FR) | `src/partials/en/*.html`, `src/partials/fr/*.html` |
| Use-case copy and images | `src/use-cases_en.json`, `src/use-cases_fr.json` |
| Use-case section behavior | `src/partials/*/section_use_cases.html`, `src/utils.js` |
| Global styles | `src/input.css`, `tailwind.config.js` |
| Favicons / PWA | `assets/favicon/` |

## Data and runtime behavior

- **Use cases**: Loaded in the browser by `src/utils.js` via `fetch(/src/use-cases_${lg}.json)`. `lg` is derived from page (e.g. `en`/`fr`). Section `section_use_cases.html` renders the grid; cards are populated from the JSON.
- **Templating**: No server at runtime. Jinja2 is used only at build time; all `{% include %}` are resolved in `build_pages.py`.

## Locales

- **en**: `partials/en/`, `use-cases_en.json`, template `index_en.html`.
- **fr**: `partials/fr/`, `use-cases_fr.json`, template `index_fr.html`.
- Shared: `partials/video_prezi_overlay.html`, `assets/`, `utils.js`.

## Other files

- `nice_background.html`, `test_static.html`, `use_case1_agents.html`, `use_case1_questions.html`: standalone/demo HTML; not part of the main build.
- `__pycache__/`: Python bytecode for `build_pages.py` (safe to ignore).
