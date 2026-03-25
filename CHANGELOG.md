# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/releases/tag/v1.0.0
