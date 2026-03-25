# Tienda de Videojuegos 🕹️

E-commerce de videojuegos desarrollado con Django.

## 🚀 Estado del Proyecto

| Fase | Estado |
|------|--------|
| Fase 1: Fundamentos | ✅ Completado |
| Fase 2: Catálogo | ✅ Completado |
| Fase 3: Carrito/Checkout | ⏳ Pendiente |
| Fase 4: Usuarios | ⏳ Pendiente |
| Fase 5: Wishlist | ⏳ Pendiente |

## 🛠️ Tech Stack

- **Backend**: Django 6.0
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: Django Templates + Bootstrap 5
- **Testing**: pytest, django-tdd

## 📋 Requisitos

```
Django 6.0+
Python 3.10+
```

## ⚡ Instalación

```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd VIDEOJUEGOS_TIENDA

# 2. Crear entorno virtual
python -m venv .venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate   # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar migraciones
cd tienda_videojuegos
python manage.py migrate

# 5. (Opcional) Cargar datos de ejemplo
python manage.py shell < seed_data.py

# 6. Iniciar servidor
python manage.py runserver
```

## 📁 Estructura del Proyecto

```
VIDEOJUEGOS_TIENDA/
├── tienda_videojuegos/     # Proyecto Django
│   ├── catalogo/         # App de catálogo (productos, géneros)
│   ├── home/            # App de página principal
│   ├── templates/        # Templates base
│   └── manage.py
├── templates/            # Templates del proyecto
├── static/               # Archivos estáticos (CSS, JS)
├── AGENTS.md            # Reglas y configuración de agentes
├── SKILLS.md            # Referencia de skills
├── PRD.md               # Especificaciones del producto
└── CHANGELOG.md         # Historial de cambios
```

## 🌐 Endpoints

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/catalogo/` | Catálogo de productos |
| `/catalogo/producto/<slug>/` | Detalle de producto |
| `/admin/` | Panel de administración |

## 🧪 Testing

```bash
# Ejecutar tests
python manage.py test

# Con pytest
pytest
```

## 📚 Documentación

- [PRD.md](./PRD.md) - Especificaciones del producto
- [AGENTS.md](./AGENTS.md) - Reglas para agentes de IA
- [SKILLS.md](./SKILLS.md) - Skills disponibles

## 🤖 Agentes y Skills

Este proyecto usa el workflow SDD (Spec-Driven Development) con skills específicas por fase:

- **Fase 2**: django-patterns
- **Fase 3**: django-tdd, django-patterns
- **Fase 4**: django-tdd, django-patterns
- **Testing**: python-testing-patterns, pytest
- **E2E**: agent-browser, playwright

Ver [SKILLS.md](./SKILLS.md) para más detalles.

## 👤 Autor

## 📄 Licencia

MIT License

---

Última actualización: Marzo 2026