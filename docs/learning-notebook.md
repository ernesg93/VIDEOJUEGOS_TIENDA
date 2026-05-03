# Cuaderno de aprendizaje

Documento pedagógico público para consolidar **aprendizaje por hitos** con evidencia verificable en código y documentación.

## Propósito y límites

- Este cuaderno registra qué se entendió y por qué, apoyado en evidencia técnica concreta del repo.
- Está organizado por hitos de aprendizaje, no por sesiones de chat ni por tareas diarias.
- Este documento **no es una bitácora automática**.
- Este documento **no reemplaza**:
  - [docs/learning-path.md](learning-path.md) (plan de estudio por etapas),
  - [CHANGELOG.md](../CHANGELOG.md) (historial de cambios integrados),
  - [docs/tooling/engram.md](tooling/engram.md) (trazabilidad operativa de decisiones y artifacts SDD).

## Cómo usar este documento

1. Elegí un hito de aprendizaje de la ruta en [docs/learning-path.md](learning-path.md).
2. Completá el bloque del hito con evidencia real (archivos, rutas, tests, docs).
3. Cerrá el hito con criterio técnico y checklist completa antes de pasar al siguiente.

## Índice de hitos

- [Hito 0 — Mapa documental y reglas del repo](#hito-0--mapa-documental-y-reglas-del-repo)
- [Hito 1 — Request/response + URLs/templates](#hito-1--requestresponse--urlstemplates)
- [Hito 2 — Auth básica](#hito-2--auth-básica)

## Índice conceptual mínimo

- [Request/response](#hito-1--requestresponse--urlstemplates)
- [URLs y templates](#hito-1--requestresponse--urlstemplates)
- [Autenticación básica](#hito-2--auth-básica)
- [Source of truth documental](#hito-0--mapa-documental-y-reglas-del-repo)

## Mantenimiento

- La actualización es **por hito** (no diaria).
- Se actualiza cuando hay un cambio pedagógico relevante y verificable.
- Criterio de calidad mínimo para considerar un hito completo:
  - evidencia trazable a rutas reales,
  - criterio/decisión explícita,
  - checklist de autoverificación completa.

## Hito 0 — Mapa documental y reglas del repo

### Contexto

Antes de tocar features, necesitábamos entender dónde vive cada tipo de verdad documental y cómo no mezclar fuentes.

### Conceptos clave

- Jerarquía documental Django-first.
- Source of truth vs documentación de apoyo.
- Trazabilidad operativa separada de documentación pública.

### Evidencia en código y docs

- `docs/documentation-policy.md` (precedencia documental explícita).
- `README.md` (onboarding y orden de lectura).
- `docs/project-state.md` (estado real actual verificable).
- `docs/workflow.md` (operación con soporte multiagente).

### Criterio / decisión

El cuaderno se mantiene como complemento pedagógico: interpreta aprendizaje con evidencia, pero no redefine comportamiento factual del sistema.

### Errores o malentendidos

- Confundir `README.md` con roadmap detallado.
- Usar `CHANGELOG.md` como material de estudio conceptual.
- Pretender que Engram sea onboarding público en vez de trazabilidad operativa.

### Checklist de autoverificación

- [x] Puedo explicar la precedencia de `docs/documentation-policy.md` sin mirar.
- [x] Distingo onboarding (`README.md`) de estado factual (`docs/project-state.md`).
- [x] Sé dónde registrar cambios integrados (`CHANGELOG.md`) vs decisiones operativas (`docs/tooling/engram.md`).

### Próximo paso

Conectar el mapa documental con el flujo request/response real del proyecto Django.

## Hito 1 — Request/response + URLs/templates

### Contexto

Necesitábamos entender cómo una URL termina en una respuesta renderizada para navegar el proyecto con criterio.

### Conceptos clave

- Ciclo request/response en Django.
- Enrutamiento con `urls.py`.
- Render de templates por app.

### Evidencia en código y docs

- `tienda_videojuegos/tienda_videojuegos/urls.py` (router principal).
- `tienda_videojuegos/catalogo/urls.py` y `tienda_videojuegos/buscador/urls.py` (namespaces por app).
- `tienda_videojuegos/templates/base.html` y templates en `tienda_videojuegos/catalogo/templates/catalogo/` (render y herencia).
- `docs/learning-path.md` (etapas de fundamentos y resultado observable).

### Criterio / decisión

Para estudiar una funcionalidad nueva, primero se sigue la ruta URL -> vista -> template -> test/documentación; recién después se evalúa refactor.

### Errores o malentendidos

- Buscar lógica de negocio en templates.
- Saltar directo al CSS sin verificar vista y contexto.
- Cambiar rutas sin revisar nombres y enlaces dependientes.

### Checklist de autoverificación

- [x] Puedo trazar `/catalogo/` desde URL hasta template.
- [x] Distingo URL principal vs URL por app.
- [x] Verifico una ruta con evidencia en archivo real antes de documentar.

### Próximo paso

Sumar autenticación básica para comprender flujo de usuario y permisos iniciales.

## Hito 2 — Auth básica

### Contexto

Con request/response claro, el siguiente paso fue entender autenticación de usuarios para navegación protegida y perfil.

### Conceptos clave

- Login/logout y sesión de usuario.
- Vistas de acceso y perfil.
- Validación de flujo autenticado.

### Evidencia en código y docs

- `tienda_videojuegos/usuarios/urls.py` (rutas de login/logout/perfil/registro).
- `tienda_videojuegos/usuarios/views.py` (vistas de autenticación y perfil).
- `tienda_videojuegos/usuarios/tests.py` (evidencia en tests de comportamiento auth).
- `docs/learning-path.md` (Etapa 2 — Usuarios y auth).

### Criterio / decisión

La auth se considera comprendida cuando se puede explicar el flujo completo (formulario -> vista -> sesión -> acceso a perfil) con evidencia en código y tests.

### Errores o malentendidos

- Creer que auth es solo UI del formulario.
- No diferenciar usuario autenticado de autorización por permisos.
- Documentar “funciona” sin respaldo en tests o rutas.

### Checklist de autoverificación

- [x] Puedo ubicar rutas de login/logout/perfil sin buscar globalmente.
- [x] Puedo describir qué valida un test de auth existente.
- [x] Puedo justificar una decisión de auth con evidencia de código/tests.

### Próximo paso

Extender estudio hacia catálogo + buscador integrando auth con casos de uso reales.
