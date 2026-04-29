# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2026-04-29

### Added

- App `usuarios` con flujo base de autenticacion
- Registro que crea el usuario, inicia sesion y redirige a inicio
- Login real con `AuthenticationForm` y logout dedicado
- Perfil protegido con `login_required`
- Menu de usuario en el header con accesos a login, registro, perfil y cierre de sesion

### Changed

- La experiencia de autenticacion ahora diferencia errores de usuario inexistente, contrasena incorrecta y credenciales vacias
- El formulario de registro usa toggle para mostrar u ocultar contrasenas desde `static/js/script.js`
- `tienda_videojuegos/db.sqlite3` deja de versionarse para evitar ruido local

### Fixed

- Portada de `God of War Ragnarok` alineada con el slug real `god-of-war-ragnarok-1`

## [1.2.0] - 2026-03-29

### Added

- App `buscador` con resultados en `/buscador/`
- Búsqueda por texto libre que interpreta nombre de juego, plataforma o combinaciones simples
- Vista de detalle por slug en `/catalogo/<slug>/`
- Template `catalogo/detalle_juego.html` con portada, precio, plataforma y stock
- Portadas dinámicas por slug con fallback a `default.png`
- Paginación en catálogo y buscador (6 productos por página)
- Más juegos y portadas de ejemplo en `populate_productos`

### Changed

- El header ahora envía búsquedas reales al buscador del proyecto
- Las cards de catálogo y buscador enlazan al detalle del producto
- El provider por defecto de GGA pasó a `opencode`

## [1.1.0] - 2026-03-24

### Added

- **Phase 2.1 MVP - Catálogo de Productos**
  - Modelo `Producto` con campos esenciales (titulo, precio, stock, activo, plataforma, slug)
  - Auto-generación de slug único desde el título del producto
  - Vista `lista_juegos` para mostrar catálogo de productos activos
  - Template `catalogo/lista_juegos.html` con grid responsivo de productos
  - Admin interface personalizado para gestión de productos con list_display, list_filter, search_fields
  - Management command `populate_productos` para poblar base de datos con productos de ejemplo
  - Migración inicial `0001_initial.py` para modelo Producto
  - Configuración de variables de entorno con `python-dotenv`
  - Archivo `.env.example` con plantilla de configuración
  - URL namespacing para app catalogo (`app_name = 'catalogo'`)
  - Navbar fixed-top con ajuste de padding en body
  - Link funcional a Tienda en navbar usando `{% url 'catalogo:lista_juegos' %}`

### Changed

- `SECRET_KEY` y `DEBUG` ahora se cargan desde variables de entorno (.env)
- Navbar ahora es fixed-top para mejor experiencia de usuario
- CSS actualizado con variables CSS para navbar-height
- Body padding ajustado para compensar navbar fixed-top

### Security

- SECRET_KEY movido a variables de entorno (no hardcoded)
- Validación de SECRET_KEY requerida al iniciar aplicación
- Archivo .env excluido de control de versiones

## [1.0.0] - 2025-01-20

### Added

- Sitio responsivo completo con Bootstrap 5.3.0
- Navbar con logo y navegación
- Botón de cambio de tema (dark/light mode)
- Hero section con gradiente
- Grid de productos destacados
- Categorías con iconos de plataformas
- Footer con información y redes sociales
- Página de contacto con formulario
- GGA integrado para code review automático
- Skill registry para workflow de agentes
- CHANGELOG.md con formato Keep a Changelog

### Changed

- CSS personalizado con variables para theming
- Templates responsivos (mobile-first)
- Footer sticky siempre visible

### Fixed

- Navbar centrado en móvil
- Footer posicionado al fondo
- Botón de tema siempre visible junto al logo

### Security

- CSRF protection habilitado en Django
- ALLOWED_HOSTS configurado para desarrollo local

[Unreleased]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/releases/tag/v1.0.0
