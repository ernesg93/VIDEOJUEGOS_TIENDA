# Estado actual del proyecto

Este documento describe **qué existe hoy** en el código de `VIDEOJUEGOS_TIENDA`.

## Fuente factual usada

- `tienda_videojuegos/tienda_videojuegos/settings.py` (`INSTALLED_APPS`)
- `tienda_videojuegos/tienda_videojuegos/urls.py` (`urlpatterns`)
- `tienda_videojuegos/{home,catalogo,buscador,usuarios}/urls.py`
- `tienda_videojuegos/{home,catalogo,buscador,usuarios}/tests.py`

## Apps activas

Apps locales registradas: `home`, `catalogo`, `buscador`, `usuarios`.

## Rutas visibles

- `/` y `/contacto/` (`home`)
- `/catalogo/` y `/catalogo/<slug>/` (`catalogo`)
- `/buscador/?q=...` (`buscador`)
- `/usuarios/login/`, `/usuarios/logout/`, `/usuarios/perfil/`, `/usuarios/registro/` (`usuarios`)

## Capacidades existentes

- Catálogo con listado y detalle por slug.
- Buscador por texto libre en catálogo.
- Flujo de autenticación base (login, logout, perfil, registro).
- Templates para home, catálogo, buscador y usuarios.

## Evidencia de tests actuales

- `tienda_videojuegos/home/tests.py`
- `tienda_videojuegos/catalogo/tests.py`
- `tienda_videojuegos/buscador/tests.py`
- `tienda_videojuegos/usuarios/tests.py`
- `tienda_videojuegos/home/tests_documentation.py`

## Trazabilidad de requirements (spec → docs)

| Requirement (spec) | Archivo | Sección |
|---|---|---|
| Jerarquía documental pedagógica | [README.md](../README.md) | `## Empezá por acá (Django-first)` |
| Alineación documentación-código | [docs/project-state.md](project-state.md) | `## Apps activas`, `## Rutas visibles`, `## Evidencia de tests actuales` |
| Ruta de aprendizaje Django incremental | [docs/learning-path.md](learning-path.md) | `## Etapa 1 — Fundamentos` a `## Etapa 4 — Mejoras incrementales` |
| Gobernanza de workflow multiagente | [docs/workflow.md](workflow.md) | `## Roles`, `## Cuándo usar cada uno`, `## Principio pedagógico` |
| Roadmap orientado a fundamentos | [PRD.md](../PRD.md) | sección de roadmap de aprendizaje/fundamentos |
| Tratamiento de documentos ambiguos/fuera de foco | [DOCS.md](../DOCS.md) | stub de compatibilidad y alcance |

## Límites actuales

- No hay checkout ni pagos.
- No hay suite E2E declarada.
- El roadmap futuro vive en [PRD.md](../PRD.md) y no debe leerse como “ya implementado”.
