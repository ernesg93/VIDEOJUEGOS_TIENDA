# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-03-24

### Added

- **Fase 2 - Catálogo Completo**
  - Modelo `Producto` con todos los campos (título, precio, stock, plataforma, género, etc.)
  - Modelo `Género` para categorización de juegos
  - Vista `lista_productos` con grid de productos activos
  - Vista `detalle_producto` con información completa
  - Filtros por plataforma y género
  - Panel de admin configurado para ambas entidades
  - Templates Bootstrap responsivos
  - 3 productos de ejemplo cargados

- **Documentación SDD**
  - PRD.md versión 2.0 con estructura profesional
  - AGENTS.md con reglas y skills por fase
  - SKILLS.md con referencia rápida de skills
  - Sistema de memoria Engram configurado

- **Skills instaladas**
  - django-tdd (testing TDD para Django)
  - django-patterns (patrones de Django)
  - python-testing-patterns (testing Python)
  - agent-browser (browser automation)
  - Skills SDD (sdd-init, sdd-propose, sdd-spec, etc.)

### Changed

- Proyecto reorganizado para seguir workflow SDD
- Modelo de datos expandido para soportar todas las fases
- Templates migrate de estructura básica a responsivos

### Removed

- Contenido temporal de pruebas

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

[Unreleased]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ernesg93/VIDEOJUEGOS_TIENDA/releases/tag/v1.0.0
