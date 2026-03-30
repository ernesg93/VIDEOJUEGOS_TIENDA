# VIDEOJUEGOS_TIENDA

Tienda de videojuegos construida con Django (templates + Bootstrap). Este repo incluye:

- Catalogo funcionando: modelo `Producto`, listado `/catalogo/`, detalle por slug, admin y comando de carga de datos.
- Buscador funcionando: `/buscador/` con busqueda por texto libre (nombre, plataforma o combinacion simple como `zelda switch`).
- Stack de agentes (Gentle): GGA (code review en pre-commit), Engram (memoria), skills del proyecto.

## Estado del proyecto

- Roadmap y requisitos: `PRD.md`
- Cambios versionados: `CHANGELOG.md`
- Reglas de codigo (usadas por GGA): `AGENTS.md`

## Requisitos

- Python (recomendado: usar venv)
- Node.js + npm (opcional; para `agent-browser`)

Dependencias Python:

- Canonico: `requirements.txt` (root)
- Alias: `tienda_videojuegos/requirements.txt` (incluye `-r ../requirements.txt`)

## Setup rapido (Windows)

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Crear variables de entorno:

1) Copiar `/.env.example` a `/.env`
2) Setear al menos `DJANGO_SECRET_KEY`.

Migraciones y servidor:

```bat
python tienda_videojuegos\manage.py migrate
python tienda_videojuegos\manage.py populate_productos
python tienda_videojuegos\manage.py runserver
```

URLs utiles:

- App: `http://127.0.0.1:8000/`
- Catalogo: `http://127.0.0.1:8000/catalogo/`
- Buscador: `http://127.0.0.1:8000/buscador/?q=zelda`
- Detalle ejemplo: `http://127.0.0.1:8000/catalogo/the-legend-of-zelda-breath-of-the-wild/`
- Admin: `http://127.0.0.1:8000/admin/`

## Setup rapido (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python tienda_videojuegos/manage.py migrate
python tienda_videojuegos/manage.py populate_productos
python tienda_videojuegos/manage.py runserver
```

## Estructura

- `tienda_videojuegos/`:
  - `manage.py`
  - `tienda_videojuegos/settings.py` (carga `.env` via `python-dotenv`)
  - Apps: `home/`, `catalogo/`, `buscador/`
- `.agent/skills/`: skills y registry del proyecto
- `.engram/`: sync de memoria (manifest + chunks)

## Funcionalidades actuales

- Catalogo paginado: 6 productos por pagina con `Primera`, `Anterior`, paginas visibles, `Siguiente`, `Ultima`.
- Portadas por slug desde `static/img/portadas/` con fallback a `default.png`.
- Vista de detalle por slug para cada juego.
- Buscador por texto libre que interpreta nombre de juego, plataforma o ambos.
- Seed de productos ampliado mediante `populate_productos`.

## Workflow de calidad (GGA)

GGA corre en `pre-commit` y usa la config del repo:

- Config: `.gga`
- Reglas: `AGENTS.md`

Git hooks no se versionan. En un clon nuevo instala el hook:

```bash
gga install
```

Tambien lo podes correr a mano:

```bash
gga run
gga config
```

Nota: GGA revisa `*.py`, `*.html`, `*.css`, `*.js` (y TS si existiera) y excluye migraciones (`*/migrations/*.py`).

## Engram sync (automatico)

Este repo versiona la memoria Engram en `.engram/` (manifest + chunks). Para automatizar el export/commit de memorias:

1) Instala los hooks del repo (una vez por clon)

Windows (PowerShell):

```powershell
./scripts/install-hooks.ps1
```

macOS/Linux (bash):

```bash
./scripts/install-hooks.sh
```

2) A partir de ahi, despues de cada `git commit` se genera un commit extra:

- `chore: sync engram memories`

Opt-out (por sesion):

```bash
ENGRAM_AUTO_SYNC=0 git commit -m "..."
```

## Browser automation (agent-browser)

Opcional, para smoke/E2E rapido sin Playwright.

Instalacion global:

```bash
npm install -g agent-browser
agent-browser install
```

Ejemplo contra el catalogo (con el `runserver` levantado):

```bash
agent-browser --allowed-domains "127.0.0.1,localhost" open http://127.0.0.1:8000/catalogo/
agent-browser wait --load networkidle
agent-browser snapshot -i --json
```

Ver skill del proyecto: `.agent/skills/agent-browser/SKILL.md`

## Skills (agentes)

Registry del proyecto:

- `.agent/skills/skill-registry.md`

Incluye `find-skills` para buscar/instalar skills del ecosistema con `npx skills`.

## Notas

- `/.env` esta ignorado por git (no commitear secretos).
- No uses `env/` como venv en Windows; usa `.venv/`.
