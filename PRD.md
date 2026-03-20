# PRD - Tienda de Videojuegos

## Product Requirements Document
### Versión 1.0 - Marzo 2025

---

## 1. Visión del Producto

### 1.1 Descripción General

**Tienda de Videojuegos** es una plataforma de comercio electrónico especializada en la venta de videojuegos físicos y digitales. El proyecto busca implementar un sistema completo de e-commerce siguiendo las mejores prácticas de desarrollo web con Django, integrando herramientas modernas de control de versiones, revisión de código y despliegue.

### 1.2 Propósito del Documento

Este PRD sirve como:
- **Directiva de especificaciones** para el desarrollo
- **Referencia de referencia** para decisiones técnicas
- **Base para metodologías SDD** (Spec-Driven Development)
- **Guía de aprendizaje** para el desarrollo profesional

### 1.3 Objetivos del Proyecto

| Objetivo | Descripción | Prioridad |
|----------|-------------|-----------|
| E-commerce funcional | Plataforma completa de venta de videojuegos | Alta |
| Responsive Design | Interfaz adaptable a todos los dispositivos | Alta |
| Sistema de usuarios | Registro, autenticación y perfiles | Alta |
| Carrito de compras | Gestión completa del proceso de compra | Alta |
| Catálogo dinámico | Gestión de productos y categorías | Alta |
| Despliegue en producción | Publicación en la nube (PythonAnywhere) | Media |
| Documentación profesional | PRD, CHANGELOG, guías de operación | Media |

---

## 2. Stakeholders

### 2.1 Equipo de Desarrollo

| Rol | Responsabilidad |
|-----|-----------------|
| Desarrollador Principal | Implementación, arquitectura, despliegues |
| Mentor/Reviewer | Code review, guía de mejores prácticas |
| Agente IA (OpenCode) | Asistencia en implementación, SDD workflow |

### 2.2 Herramientas y Tecnologías

| Categoría | Herramienta | Propósito |
|----------|-------------|-----------|
| Framework | Django 6.0+ | Backend y ORM |
| Frontend | Bootstrap 5.3 | CSS responsivo |
| Base de Datos | SQLite (dev) / MySQL (prod) | Almacenamiento |
| Control de Versiones | Git + GitHub | Historial y colaboración |
| Code Review | GGA (Gentleman Guardian Angel) | Revisión automática |
| Metodología | SDD (Spec-Driven Development) | Workflow estructurado |
| Documentación | CHANGELOG, AGENTS.md | Trazabilidad |
| Despliegue | PythonAnywhere | Hosting en producción |

---

## 3. Requisitos Funcionales

### 3.1 Sistema de Catálogo

#### RF-001: Gestión de Productos
```
Como: Administrador
Quiero: Agregar, editar y eliminar videojuegos
Para: Mantener el catálogo actualizado
```

**Campos del Producto:**
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| id | Auto | Sí | Identificador único |
| titulo | CharField(200) | Sí | Nombre del videojuego |
| descripcion | TextField | No | Descripción detallada |
| precio | DecimalField(6,2) | Sí | Precio en USD |
| plataforma | ChoiceField | Sí | PC, PS5, Xbox, Switch |
| genero | ForeignKey | No | Género del juego |
| imagen | ImageField | No | Portada del juego |
| stock | IntegerField | Sí | Cantidad disponible |
| fecha_lanzamiento | DateField | No | Fecha de lanzamiento |
| activo | BooleanField | Sí | Visible en tienda |
| created_at | DateTimeField | Auto | Fecha de creación |
| updated_at | DateTimeField | Auto | Última modificación |

#### RF-002: Gestión de Categorías
```
Como: Administrador
Quiero: Crear y gestionar géneros/categorías
Para: Organizar los productos
```

**Campos de Categoría:**
| Campo | Tipo | Requerido |
|-------|------|-----------|
| nombre | CharField(100) | Sí |
| slug | SlugField | Sí |
| descripcion | TextField | No |
| activa | BooleanField | Sí |

### 3.2 Sistema de Usuarios

#### RF-003: Registro de Usuarios
```
Como: Visitante
Quiero: Crear una cuenta
Para: Acceder a funcionalidades exclusivas
```

**Campos del Usuario:**
| Campo | Tipo | Requerido |
|-------|------|-----------|
| username | CharField | Sí |
| email | EmailField | Sí |
| password | CharField | Sí |
| nombre | CharField | No |
| apellido | CharField | No |
| fecha_nacimiento | DateField | No |
| es_admin | BooleanField | Auto |

#### RF-004: Autenticación
```
Como: Usuario registrado
Quiero: Iniciar sesión
Para: Acceder a mi cuenta
```

**Requisitos:**
- Login con username/email y password
- Logout seguro
- Sesiones persistentes
- Protección contra brute force

#### RF-005: Perfil de Usuario
```
Como: Usuario
Quiero: Ver y editar mi perfil
Para: Mantener mi información actualizada
```

### 3.3 Sistema de Carrito

#### RF-006: Gestión del Carrito
```
Como: Usuario
Quiero: Agregar productos al carrito
Para: Preparar mi compra
```

**Funcionalidades:**
| Funcionalidad | Descripción |
|---------------|-------------|
| Agregar | Añadir producto con cantidad |
| Actualizar | Modificar cantidad |
| Eliminar | Quitar producto del carrito |
| Ver | Listar productos en carrito |
| Persistencia | Guardar carrito entre sesiones |
| Total | Calcular subtotal y total |

#### RF-007: Proceso de Compra
```
Como: Usuario
Quiero: Completar una compra
Para: Adquirir los productos
```

**Flujo de Compra:**
1. Revisar carrito
2. Ingresar dirección de envío
3. Seleccionar método de pago
4. Confirmar pedido
5. Recibir confirmación por email

### 3.4 Frontend

#### RF-008: Página de Inicio
```
Como: Visitante
Quiero: Ver una página de inicio atractiva
Para: Conocer la tienda
```

**Componentes:**
- Hero section con CTA
- Productos destacados (3-6 items)
- Categorías con iconos
- Información de envío/seguridad

#### RF-009: Catálogo/Listado
```
Como: Visitante
Quiero: Ver todos los productos
Para: Explorar el catálogo
```

**Características:**
- Grid responsivo de productos
- Filtros por: categoría, plataforma, precio
- Ordenamiento por: precio, nombre, recientes
- Paginación

#### RF-010: Detalle de Producto
```
Como: Visitante
Quiero: Ver detalles de un producto
Para: Decidir si comprarlo
```

**Información mostrada:**
- Imagen principal
- Título y descripción
- Precio
- Plataforma y género
- Stock disponible
- Botón "Añadir al carrito"

### 3.5 Panel de Administración

#### RF-011: Dashboard de Admin
```
Como: Administrador
Quiero: Gestionar la tienda
Para: Mantener el negocio funcionando
```

**Funcionalidades:**
- CRUD de productos
- CRUD de categorías
- Gestión de pedidos
- Reportes de ventas

---

## 4. Requisitos No Funcionales

### 4.1 Performance

| Métrica | Target |
|---------|--------|
| Tiempo de carga | < 2 segundos |
| TTFB (Time To First Byte) | < 500ms |
| Lighthouse Score | > 90 |

### 4.2 Seguridad

| Requisito | Implementación |
|-----------|----------------|
| HTTPS | Obligatorio en producción |
| CSRF Protection | Django middleware |
| SQL Injection | ORM (no SQL raw) |
| XSS | Template escaping |
| Contraseñas | Django auth (bcrypt) |
| Secrets | Variables de entorno (.env) |

### 4.3 Responsividad

| Dispositivo | Breakpoint | Layout |
|-------------|-----------|--------|
| Mobile | < 576px | 1 columna |
| Tablet | 576px - 992px | 2 columnas |
| Desktop | > 992px | 3-4 columnas |

### 4.4 Accesibilidad

| Criterio | Nivel |
|----------|-------|
| WCAG | 2.1 AA |
| Contraste | 4.5:1 mínimo |
| Navegación por teclado | Completa |

---

## 5. Arquitectura Técnica

### 5.1 Estructura del Proyecto

```
VIDEOJUEGOS_TIENDA/
├── tienda_videojuegos/          # Proyecto Django (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/                        # App: páginas estáticas
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/home/
├── catalogo/                    # App: gestión de productos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/catalogo/
├── usuarios/                    # App: autenticación y perfiles
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/usuarios/
├── carrito/                     # App: carrito de compras
│   ├── models.py
│   ├── views.py
│   └── context.py
├── pedidos/                     # App: gestión de pedidos
│   ├── models.py
│   ├── views.py
│   └── admin.py
├── templates/                   # Templates base
│   └── base.html
├── static/                     # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── img/
├── recursos/                    # Documentación del curso
├── .gga                         # Configuración GGA
├── .gitignore
├── AGENTS.md                    # Reglas de código
├── CHANGELOG.md                 # Historial de cambios
└── requirements.txt             # Dependencias
```

### 5.2 Modelo de Datos (ERD)

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  Categoria  │       │   Producto   │       │   Usuario   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id          │◄──────│ categoria_id│       │ id          │
│ nombre      │       │ id          │       │ username    │
│ slug        │       │ titulo      │       │ email       │
│ descripcion │       │ descripcion │       │ password    │
│ activa      │       │ precio      │       │ nombre      │
└─────────────┘       │ plataforma  │       │ apellido    │
                      │ imagen      │       └─────────────┘
                      │ stock       │              │
                      │ activo      │              │
                      │ created_at  │              │
                      └─────────────┘              │
                             │                     │
                             │              ┌──────┴──────┐
                             │              │  Pedido    │
                             │              ├─────────────┤
                             │              │ id          │
                             │              │ usuario_id  │
                             │              │ total       │
                             │              │ estado      │
                             │              │ fecha       │
                             │              └─────────────┘
                             │                    │
                      ┌──────┴──────┐              │
                      │ LineaPedido │◄─────────────┘
                      ├─────────────┤
                      │ id          │
                      │ pedido_id   │
                      │ producto_id │
                      │ cantidad    │
                      │ precio      │
                      └─────────────┘
```

### 5.3 URL Patterns

```
# URLs principales (tienda_videojuegos/urls.py)
urlpatterns = [
    path('', include('home.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('admin/', admin.site.urls),
]

# Home (home/urls.py)
path('', views.index, name='home'),
path('contacto/', views.contacto, name='contacto'),

# Catálogo (catalogo/urls.py)
path('', views.lista_productos, name='lista_productos'),
path('<slug:producto_slug>/', views.detalle_producto, name='detalle_producto'),
path('categoria/<slug:categoria_slug>/', views.por_categoria, name='por_categoria'),

# Usuarios (usuarios/urls.py)
path('registro/', views.registro, name='registro'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('perfil/', views.perfil, name='perfil'),

# Carrito (carrito/urls.py)
path('', views.ver_carrito, name='ver_carrito'),
path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
path('actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

# Pedidos (pedidos/urls.py)
path('', views.mis_pedidos, name='mis_pedidos'),
path('crear/', views.crear_pedido, name='crear_pedido'),
path('<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
```

---

## 6. User Stories Detalladas

### 6.1 Visitante

| ID | Historia | Criterios de Aceptación |
|----|----------|-------------------------|
| US-001 | Ver página de inicio | Puedo ver productos destacados y navegación |
| US-002 | Explorar catálogo | Puedo ver todos los productos con filtros |
| US-003 | Buscar productos | Puedo buscar por nombre o descripción |
| US-004 | Ver detalle de producto | Veo toda la información del producto |

### 6.2 Usuario Registrado

| ID | Historia | Criterios de Aceptación |
|----|----------|-------------------------|
| US-010 | Registrarme | Puedo crear una cuenta con email válido |
| US-011 | Iniciar sesión | Puedo entrar con mis credenciales |
| US-012 | Ver perfil | Puedo ver y editar mi información |
| US-013 | Añadir al carrito | Puedo agregar productos desde cualquier página |
| US-014 | Gestionar carrito | Puedo ver, modificar y eliminar productos |
| US-015 | Realizar compra | Puedo completar el proceso de compra |
| US-016 | Ver historial | Puedo ver mis pedidos anteriores |

### 6.3 Administrador

| ID | Historia | Criterios de Aceptación |
|----|----------|-------------------------|
| US-020 | CRUD productos | Puedo crear, editar y eliminar productos |
| US-021 | CRUD categorías | Puedo gestionar las categorías |
| US-022 | Ver pedidos | Puedo ver todos los pedidos |
| US-023 | Actualizar estado | Puedo cambiar el estado de un pedido |

---

## 7. Roadmap

### Fase 1: Fundamentos (Completado ✓)
```
Estado: Fundamentos implementados
Entregables:
- ✅ Proyecto Django configurado
- ✅ Estructura de apps
- ✅ Templates base responsivos
- ✅ Sistema de versionado (Git + GGA)
- ✅ Documentación (AGENTS.md, CHANGELOG)
```

### Fase 2: Catálogo de Productos
```
Estado: Pendiente
Entregables:
- ⏳ Modelos Producto y Categoría
- ⏳ CRUD de productos (admin)
- ⏳ Listado con filtros
- ⏳ Detalle de producto
- ⏳ Seed data de ejemplo
```

### Fase 3: Sistema de Usuarios
```
Estado: Pendiente
Entregables:
- ⏳ Extender User model
- ⏳ Registro con validación
- ⏳ Login/Logout
- ⏳ Perfil de usuario
- ⏳ Contraseñas seguras
```

### Fase 4: Carrito de Compras
```
Estado: Pendiente
Entregables:
- ⏳ Modelo Carrito/Items
- ⏳ Context processor para sesión
- ⏳ Vista del carrito
- ⏳ Agregar/Actualizar/Eliminar
- ⏳ Persistencia en base de datos
```

### Fase 5: Proceso de Compra
```
Estado: Pendiente
Entregables:
- ⏳ Checkout flow
- ⏳ Direcciones de envío
- ⏳ Modelos Pedido
- ⏳ Confirmación por email
- ⏳ Historial de pedidos
```

### Fase 6: Despliegue
```
Estado: Pendiente
Entregables:
- ⏳ Configuración producción
- ⏳ Variables de entorno (.env)
- ⏳ Migrar a MySQL
- ⏳ Despliegue en PythonAnywhere
- ⏳ SSL/HTTPS
```

---

## 8. Workflow de Desarrollo

### 8.1 Metodología SDD (Spec-Driven Development)

Para cada feature, seguir el ciclo:

```
1. EXPLORE    → Investigar requisitos, analizar código existente
2. PROPOSE    → Documentar intent, scope, approach, risks
3. SPEC       → Requisitos detallados con Given/When/Then
4. DESIGN     → Diseño técnico, estructuras de archivos
5. TASKS      → Desglose en tareas implementables
6. APPLY      → Implementación siguiendo specs
7. VERIFY     → Comparar implementación vs specs
8. ARCHIVE    → Sincronizar delta specs a main specs
```

### 8.2 Convenciones de Commits

Formato: `<tipo>(<scope>): <descripción>`

| Tipo | Uso |
|------|-----|
| feat | Nueva funcionalidad |
| fix | Bug fix |
| docs | Documentación |
| style | Formateo (sin cambio de lógica) |
| refactor | Refactorización |
| test | Tests |
| chore | Mantenimiento |
| perf | Performance |

**Ejemplos:**
```bash
feat(catalogo): add producto model
fix(carrito): correct total calculation
docs(readme): update installation instructions
```

### 8.3 Proceso de Release

```
1. Implementar cambios (SDD cycle)
2. git add . && git commit -m "feat: descripción"
3. GGA revisa automáticamente (pre-commit hook)
4. git push origin <rama>
5. Pull Request → Code Review
6. Merge a master/main
7. ACTUALIZAR CHANGELOG.md ← OBLIGATORIO
8. git tag v1.0.0
9. git push origin v1.0.0
10. GitHub detecta tag → Crear Release
```

### 8.4 Código de Conducta

| Regla | Descripción |
|-------|-------------|
| No romper master | Solo merge con PR aprobado |
| Tests primero | TDD cuando sea posible |
| Code review | GGA + revisión humana |
| Documentar | Commits descriptivos, docs actualizadas |
| SOLID | Aplicar principios de diseño |

---

## 9. Apéndice

### 9.1 Glosario

| Término | Definición |
|---------|------------|
| ORM | Object-Relational Mapping. Abstracción de base de datos |
| MVT | Modelo-Vista-Plantilla. Patrón de Django |
| SDD | Spec-Driven Development. Metodología de desarrollo |
| GGA | Gentleman Guardian Angel. Code review automatizado |
| PRD | Product Requirements Document |
| ERD | Entity-Relationship Diagram |

### 9.2 Recursos

| Recurso | Ubicación |
|---------|-----------|
| Curso Django | `recursos/Estructura y Contenidos del Curso...xlsx` |
| Guía de Estudio | `recursos/Guía de Estudio...docx` |
| Manual de Operaciones | `recursos/Manual de Operaciones...docx` |

### 9.3 Referencias

- [Documentación Django](https://docs.djangoproject.com/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)

---

## 10. Aprobaciones

| Rol | Nombre | Fecha | Firma |
|-----|--------|-------|-------|
| Desarrollador | [Nombre] | [Fecha] | __________ |
| Mentor | [Nombre] | [Fecha] | __________ |

---

**Documento creado como parte del proyecto de aprendizaje de desarrollo web con Django.**
**Última actualización: Marzo 2025**
