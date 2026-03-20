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
| Commits | `GGA` | Code review automático |

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
# GGA revisará automáticamente
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
find-skills  → Buscar skills
skill-creator → Crear nuevos skills
pr-review    → Revisar PRs de GitHub
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
- GGA revisa automáticamente con pre-commit hook

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

## 🔗 Recursos

- Skills: `/home/ernesg93/.claude/skills/`, `/home/ernesg93/.config/opencode/skills/`
- GGA: Pre-commit hook activo, revisa .py, .html, .css, .js
- Docs: AGENTS.md
