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
- Catálogo extendido con `Genero` y metadatos incrementales para producto (`fecha_lanzamiento`, descripciones, `precio_oferta`, `edad_minima`).
- Buscador por texto libre en catálogo.
- Flujo de autenticación base (login, logout, perfil, registro).
- Templates para home, catálogo, buscador y usuarios.

## Evolución reciente del catálogo

- El dominio de `Producto` ya no está limitado al MVP inicial.
- La evolución se hizo de forma incremental: el baseline histórico permanece en `0001_initial.py` y la ampliación vive en `0002_genero_producto_extend.py`.
- El modelo `Genero` permite clasificar productos sin romper compatibilidad con productos existentes.
- Los nuevos campos del catálogo amplían expresividad del dominio sin volver obligatorios los datos extendidos en registros previos.

## Evidencia funcional del catálogo extendido

- `tienda_videojuegos/catalogo/models.py` define `Genero` y los nuevos campos de `Producto`.
- `tienda_videojuegos/catalogo/tests.py` valida:
  - contratos de vistas públicas,
  - baseline vs migración incremental,
  - compatibilidad del dominio extendido,
  - contrato de admin,
  - comportamiento canónico del seed.

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
- La comprensión pedagógica del catálogo debe complementarse con el hito dedicado en [docs/learning-notebook.md](learning-notebook.md).
