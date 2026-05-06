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
- Este cuaderno es **complemento pedagógico**: interpreta y conecta aprendizaje.
- La **fuente canónica** para estado de implementación y evidencia factual del proyecto es
  [docs/project-state.md](project-state.md).

## Cómo usar este documento

1. Elegí un hito de aprendizaje de la ruta en [docs/learning-path.md](learning-path.md).
2. Completá el bloque del hito con evidencia real (archivos, rutas, tests, docs).
3. Cerrá el hito con criterio técnico y checklist completa antes de pasar al siguiente.

## Índice de hitos

- [Hito 0 — Mapa documental y reglas del repo](#hito-0--mapa-documental-y-reglas-del-repo)
- [Hito 1 — Request/response + URLs/templates](#hito-1--requestresponse--urlstemplates)
- [Hito 2 — Auth básica](#hito-2--auth-básica)
- [Hito 3 — Evolución segura del catálogo](#hito-3--evolución-segura-del-catálogo)
- [Hito 4 — Contratos de búsqueda y UX incremental](#hito-4--contratos-de-búsqueda-y-ux-incremental)

## Índice conceptual mínimo

- [Request/response](#hito-1--requestresponse--urlstemplates)
- [URLs y templates](#hito-1--requestresponse--urlstemplates)
- [Autenticación básica](#hito-2--auth-básica)
- [Evolución incremental de dominio](#hito-3--evolución-segura-del-catálogo)
- [Contratos de búsqueda](#hito-4--contratos-de-búsqueda-y-ux-incremental)
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
- Contrato `?next=` en login: si el usuario llega desde una ruta protegida, vuelve a ese destino después de autenticarse.
- Escenarios negativos cubiertos: logout anónimo redirige a login; registro inválido mantiene contexto y errores visibles.

### Criterio / decisión

La auth se considera comprendida cuando se puede explicar el flujo completo (formulario -> vista -> sesión -> acceso a perfil) con evidencia en código y tests, incluyendo qué pasa cuando el usuario llega desde una ruta protegida o cuando el formulario falla.

### Errores o malentendidos

- Creer que auth es solo UI del formulario.
- No diferenciar usuario autenticado de autorización por permisos.
- Documentar “funciona” sin respaldo en tests o rutas.
- Pensar que login exitoso siempre debe ir a home, ignorando la intención previa del usuario (`?next=`).
- Cubrir solo caminos felices y no proteger errores de registro o logout anónimo.

### Checklist de autoverificación

- [x] Puedo ubicar rutas de login/logout/perfil sin buscar globalmente.
- [x] Puedo describir qué valida un test de auth existente.
- [x] Puedo justificar una decisión de auth con evidencia de código/tests.
- [x] Entiendo por qué `?next=` preserva intención de navegación y mejora la UX de autenticación.
- [x] Sé identificar al menos dos escenarios negativos que también forman parte del contrato de auth.

### Próximo paso

Extender estudio hacia catálogo + buscador integrando auth con casos de uso reales y contratos visibles de UX.

## Hito 3 — Evolución segura del catálogo

### Contexto

Con la base de navegación y auth ya entendidas, el siguiente salto fue extender el dominio del catálogo sin romper el baseline histórico del proyecto.

### Conceptos clave

- Evolución incremental de modelos en Django.
- Diferencia entre baseline histórico y ampliación posterior mediante migraciones.
- Compatibilidad hacia atrás en datos y comportamiento público.
- Relación `ForeignKey` opcional para enriquecer dominio sin forzar datos preexistentes.

### Evidencia en código y docs

- `tienda_videojuegos/catalogo/models.py` (`Genero`, `Producto.genero`, `fecha_lanzamiento`, descripciones, `precio_oferta`, `edad_minima`).
- `tienda_videojuegos/catalogo/migrations/0001_initial.py` (baseline histórico intacto).
- `tienda_videojuegos/catalogo/migrations/0002_genero_producto_extend.py` (ampliación incremental del dominio).
- `tienda_videojuegos/catalogo/tests.py` (contratos de migración, dominio extendido, admin y seed).
- `docs/project-state.md` (estado factual del catálogo extendido).

### Criterio / decisión

La evolución del catálogo se considera bien entendida cuando se puede explicar por qué los nuevos campos viven en una migración incremental y cómo eso protege compatibilidad con el MVP original.

### Errores o malentendidos

- Pensar que enriquecer el dominio obliga a reescribir la migración inicial.
- Agregar campos nuevos sin distinguir cuáles deben ser opcionales para mantener compatibilidad.
- Documentar “catálogo extendido” sin evidencia en tests de migración o comportamiento.

### Checklist de autoverificación

- [x] Puedo explicar por qué `0001_initial.py` se preserva como baseline y la ampliación ocurre en `0002_genero_producto_extend.py`.
- [x] Puedo justificar por qué `genero` y otros campos nuevos son opcionales en términos de compatibilidad.
- [x] Puedo señalar qué tests prueban la evolución segura del dominio.

### Próximo paso

Conectar esta evolución del dominio con casos de uso visibles del catálogo (filtros, detalle enriquecido y navegación por género) antes de seguir expandiendo features.

## Hito 4 — Contratos de búsqueda y UX incremental

### Contexto

Antes de abrir una feature grande como carrito, necesitábamos endurecer comportamiento visible ya existente para aprender a trabajar con cambios chicos, criterios claros y tests que realmente protejan UX.

### Conceptos clave

- Contrato de búsqueda por query string.
- Diferencia entre comportamiento real y expectativa mal formulada en tests.
- UX incremental: preservar intención del usuario vale tanto como “hacer funcionar” la vista.
- Escenarios negativos como parte del comportamiento, no como casos accesorios.

### Evidencia en código y docs

- `tienda_videojuegos/buscador/tests.py` (query vacía, productos inactivos, sin resultados, nombre + plataforma, paginación con query string).
- `tienda_videojuegos/usuarios/tests.py` (redirect con `?next=`, logout anónimo, registro inválido).
- `tienda_videojuegos/usuarios/views.py` (validación segura de `next` con `url_has_allowed_host_and_scheme`).
- `tienda_videojuegos/usuarios/templates/usuarios/login.html` (preservación de `next` en hidden input).
- `docs/learning-path.md` (Etapa 4 — mejoras incrementales).

### Criterio / decisión

No toda mejora valiosa es una feature nueva. En esta etapa decidimos que primero conviene fortalecer contratos visibles del sistema ya existente: búsquedas, errores, redirecciones e intención de navegación. Eso prepara mejor el terreno para futuras features de negocio.

### Errores o malentendidos

- Creer que un test aporta valor solo por existir, aunque afirme una expectativa incorrecta.
- Tratar query vacía como caso “menor” en vez de definir explícitamente su contrato.
- Pensar que auth correcta es solo validar credenciales, sin preservar el destino original del usuario.
- Saltar a carrito sin antes dominar estado, navegación y contratos visibles del sistema actual.

### Checklist de autoverificación

- [x] Puedo explicar por qué una query vacía del buscador muestra todos los productos activos en este proyecto.
- [x] Puedo señalar qué tests protegen resultados vacíos, productos inactivos y paginación con query string.
- [x] Entiendo por qué `?next=` debe validarse y no redirigirse ciegamente.
- [x] Puedo justificar por qué estas mejoras chicas fortalecen fundamentos antes de abrir carrito.

### Próximo paso

Pasar del refinamiento visible a la exploración conceptual de estado y sesión en Django para evaluar con criterio qué tipo de carrito tendría sentido implementar después.
