# Skill Registry - VIDEOJUEGOS_TIENDA

Este documento mapea las situaciones del proyecto con los skills disponibles.

---

## 📋 Mapeo de Situaciones → Skills

| Situación | Skill | Descripción |
|-----------|-------|-------------|
| Nuevo cambio/fetaure | `sdd-*` (ciclo completo) | Workflow estructurado |
| Investigar algo | `sdd-explore` | Analizar código, investigar ideas |
| Propuesta de cambio | `sdd-propose` | Documentar intent, scope, approach |
| Especificaciones | `sdd-spec` | Requisitos con escenarios Given/When/Then |
| Diseño técnico | `sdd-design` | Arquitectura, estructuras de archivos |
| Desglose de tareas | `sdd-tasks` | Implementación en tareas concretas |
| Implementar código | `sdd-apply` | Escribir código siguiendo specs |
| Verificar cambios | `sdd-verify` | Comparar implementación vs specs |
| Revisar código | `django-drf` | Patrones Django, convenciones |
| Testing | `pytest` | Tests en Python |
| E2E testing | `playwright` | Tests end-to-end |
| Browser automation | `agent-browser` | Automatizacion de navegador via CLI (Vercel agent-browser) |
| Commits | `GGA` | Code review automático |
| Changelog | `changelog-maintenance` | Formato Keep a Changelog + Semver |

---

## 🚀 Guía de Uso por Escenario

### 1. Cambio Sustancial (ej: agregar modelo Videojuego)

```bash
# Usar ciclo SDD completo
/sdd-new agregar-videojuego
```

Esto ejecuta:
1. `sdd-explore` → Investigar requisitos
2. `sdd-propose` → Propuesta de cambio
3. `sdd-spec` → Especificaciones detalladas
4. `sdd-design` → Diseño técnico
5. `sdd-tasks` → Desglose de tareas
6. `sdd-apply` → Implementación
7. `sdd-verify` → Verificación

### 2. Cambio Rápido (ej: ajustar CSS, fix menor)

```bash
# Sin SDD, implementar directo con GGA
git add .
git commit -m "fix: description"
# GGA revisará automáticamente (si el hook está instalado: `gga install`)
```

### 3. Investigar/Explorar (ej: cómo funciona el auth de Django)

```bash
# Usar sdd-explore
/sdd-explore django-auth
```

### 4. Agregar Tests

```bash
# Usar pytest
/skill pytest
# Luego implementar tests siguiendo patrones
```

---

## 📁 Estructura de Skills Disponibles

### SDD Workflow
```
sdd-init     → Inicializar contexto
sdd-explore → Investigar
sdd-propose → Propuesta
sdd-spec    → Especificaciones
sdd-design  → Diseño técnico
sdd-tasks   → Desglose de tareas
sdd-apply   → Implementación
sdd-verify  → Verificación
sdd-archive → Archivar
```

### Framework
```
django-drf  → Patrones Django REST Framework
pytest       → Testing en Python
playwright   → E2E testing
```

### Utilidades
```
find-skills              → Buscar skills
skill-creator            → Crear nuevos skills
pr-review                → Revisar PRs de GitHub
changelog-maintenance    → Mantenimiento de CHANGELOG con Semver
```

### find-skills (metahabilidad)

```bash
# Buscar e instalar skills del ecosistema
npx skills find <query>
npx skills add <repo-url-o-owner/repo> --skill <skill-name> -g -y
```

---

## 🎯 Reglas de Carga de Skills

### Auto-detección (miembro debería hacer)

| Contexto | Skill a cargar |
|----------|---------------|
| Cambios en models.py | `django-drf` |
| Cambios en views.py | `django-drf` |
| Cambios en serializers.py | `django-drf` |
| Tests en Python | `pytest` |
| Tests E2E | `playwright` |
| Browser automation / smoke E2E | `agent-browser` |
| Antes de release/merge | `changelog-maintenance` |
| Cambios sustanciales | `sdd-*` (ciclo completo) |

###-before cada implementación

1. **Leer skill del framework** (django-drf)
2. **Seguir convenciones** del AGENTS.md
3. **Aplicar patrones** del skill
4. **Usar GGA** para revisar antes de commit

---

## 📝 Convenciones de Este Proyecto

### Commits
- Usar conventional commits: `feat:`, `fix:`, `chore:`, `docs:`
- GGA revisa automáticamente con pre-commit hook (instalar con `gga install`)

### Código
- 4 espacios, max 120 chars
- snake_case para variables
- PascalCase para clases
- Templates en `templates/<app>/`
- Static en `static/css/`, `static/js/`, `static/img/`

### Testing
- Tests en `tests.py` de cada app
- Seguir patrón `test_<nombre>_<escenario>`
- Usar Django TestCase

---

## 📝 Actualización del CHANGELOG

**OBLIGATORIO** después de cada release o merge a master.

### Cuándo actualizar:
- ✅ Después de hacer merge a `master`/`main`
- ✅ Antes de crear un tag de release
- ✅ Cuando se completa un feature sustancial
- ❌ NO en cada commit (solo en cambios significativos)

### Formato de entrada:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- Descripción del feature nuevo

### Changed
- Descripción de mejora

### Fixed
- Descripción del bug fix

### Removed
- Descripción de funcionalidad removida
```

### Categorías válidas:
| Categoría | Uso |
|-----------|-----|
| Added | Features nuevos |
| Changed | Cambios en funcionalidad existente |
| Deprecated | Funcionalidad que será removida |
| Removed | Funcionalidad eliminada |
| Fixed | Bug fixes |
| Security | Cambios de seguridad |

### Workflow completo (con changelog):

```
1. sdd-apply → Implementar cambios
2. git add . && git commit -m "feat: nueva funcionalidad"
3. GGA revisa automáticamente (pre-commit hook)
4. git push origin <rama>
5. Merge a master/main
6. ACTUALIZAR CHANGELOG.md ← OBLIGATORIO
7. git add CHANGELOG.md && git commit -m "docs: update changelog"
8. Crear tag si es release: git tag v1.0.0
```

---

## 🔗 Recursos
- Skills: `/home/ernesg93/.claude/skills/`, `/home/ernesg93/.config/opencode/skills/`
- GGA: Pre-commit hook (instalar con `gga install`), revisa .py, .html, .css, .js
- Docs: AGENTS.md
- Changelog: CHANGELOG.md
