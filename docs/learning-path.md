# Ruta de aprendizaje

Ruta pedagógica sugerida para aprender Django con este repo.

Referencias de soporte:
- Estado real: [docs/project-state.md](project-state.md)
- Workflow de trabajo: [docs/workflow.md](workflow.md)
- Cuaderno pedagógico: [docs/learning-notebook.md](learning-notebook.md)

> Diferencia clave: este archivo define el **plan de estudio**; el cuaderno registra la **evidencia/reflexión por hito**.

## Etapa 1 — Fundamentos

- **Objetivo**: entender estructura de proyecto Django, apps, urls, templates y settings.
- **Prerrequisitos**: Python básico + virtualenv.
- **Resultado observable**: levantás servidor y navegás `/`, `/catalogo/`, `/buscador/`.

## Etapa 2 — Usuarios y auth

- **Objetivo**: comprender login/logout/perfil/registro con vistas y templates.
- **Prerrequisitos**: etapa 1 completada.
- **Resultado observable**: usuario puede autenticarse y acceder a `/usuarios/perfil/`.

## Etapa 3 — Catálogo y buscador

- **Objetivo**: dominar modelo/vistas/urls para listado + detalle + búsqueda.
- **Prerrequisitos**: etapas 1 y 2.
- **Resultado observable**: catálogo paginado y búsquedas por query string funcionando.

## Etapa 4 — Mejoras incrementales

- **Objetivo**: practicar tests, refactors chicos y documentación alineada.
- **Prerrequisitos**: etapas 1 a 3.
- **Resultado observable**: cambios pequeños con evidencia en tests y changelog.
