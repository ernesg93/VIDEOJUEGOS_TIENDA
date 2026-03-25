# PRD - Tienda de Videojuegos

## Product Requirements Document
### Versión 2.0 - Marzo 2026

---

## 1. Visión del Producto

### 1.1 Resumen Ejecutivo
Tienda de videojuegos online que permite a los clientes explorar un catálogo de productos, agregaritems al carrito y realizar compras. El sistema soporta múltiples plataformas (PC, PS5, Xbox, Switch) y géneros de juegos.

### 1.2 Objetivos de Negocio
- Permitir la venta de videojuegos físicos y digitales
- Proporcionar navegación fluida por catálogo con filtros
- Gestionar inventario y pedidos desde el panel de administración

### 1.3 Alcance del Proyecto
| Incluido | Excluido |
|----------|-----------|
| Catálogo de productos | Sistema de suscripción |
| Carrito de compras | Marketplace de usuarios |
| Checkout y pagos básicos | Sistema de reseñas |
| Panel de administración | Pasarelas de pago complejas |
| Registro de usuarios | Programa de fidelización |

---

## 2. Definición de Roles

| Rol | Descripción | Permisos |
|-----|-------------|----------|
| Visitante | Usuario sin registrar que navega el catálogo | Ver productos, buscar |
| Cliente | Usuario registrado que puede comprar | Todo lo anterior + carrito, checkout, perfil |
| Administrador | Staff que gestiona el negocio | CRUD total: productos, pedidos, usuarios |

---

## 3. Requisitos Funcionales

### 3.1 Catálogo de Productos (RF-001)

#### RF-001.1: Listado de productos
**Historia:** Como visitante, quiero ver un grid de videojuegos disponibles para explorar el catálogo.

**Criterios de aceptación:**
- Grid de productos con imagen, título, precio, plataforma
- Solo muestra productos activos
- Paginación o scroll infinito (20 productos por página)
- Diseño responsivo (móvil y desktop)

#### RF-001.2: Detalle de producto
**Historia:** Como cliente, quiero ver los detalles completos de un juego para decidir si comprarlo.

**Criterios de aceptación:**
- Muestra: imagen, título, precio, plataforma, género, descripción, fecha lanzamiento
- Botón "Añadir al Carrito" visible
- Productos relacionados al final

#### RF-001.3: Filtrado y búsqueda
**Historia:** Como visitante, quiero filtrar productos por plataforma y género para encontrar lo que busco.

**Criterios de aceptación:**
- Filtro por plataforma (PC, PS5, Xbox, Switch)
- Filtro por género (Acción, RPG, Deportes, etc.)
- Los filtros se aplican sin recargar la página

#### RF-001.4: Gestión de productos (Admin)
**Historia:** Como administrador, quiero agregar, editar y eliminar productos del catálogo.

**Criterios de aceptación:**
- CRUD completo desde Django Admin
- Todos los campos editables
- Slug automático desde título

---

### 3.2 Carrito de Compras (RF-002)

#### RF-002.1: Agregar al carrito
**Historia:** Como cliente, quiero agregar productos al carrito para comenzar una compra.

**Criterios de aceptación:**
- Botón "Añadir al Carrito" en listing y detalle
- Indicador visual de cantidad en header
- Persiste entre sesiones (BD o sesión)

#### RF-002.2: Ver carrito
**Historia:** Como cliente, quiero ver todos los items en mi carrito y su total.

**Criterios de aceptación:**
- Lista de productos con cantidad, precio unitario, subtotal
- Total general de la compra
- Botones para aumentar/disminuir cantidad
- Botón para eliminar item

#### RF-002.3: Actualizar cantidad
**Historia:** Como cliente, quiero modificar la cantidad de un producto en el carrito.

**Criterios de aceptación:**
- Aumentar/disminuir cantidad con botones +/-
- Eliminar producto si cantidad = 0
- Actualización en tiempo real del total

---

### 3.3 Checkout y Órdenes (RF-003)

#### RF-003.1: Proceso de compra
**Historia:** Como cliente, quiero completar una compra para obtener los productos.

**Criterios de aceptación:**
- Formulario: datos de envío (dirección, teléfono)
- Resumen del pedido con todos los items
- Selección de método de pago (solo efectivo contra entrega por ahora)
- Confirmación del pedido con número de orden
- Envío de email de confirmación (opcional)

#### RF-003.2: Gestión de pedidos (Admin)
**Historia:** Como administrador, quiero gestionar los pedidos de los clientes.

**Criterios de aceptación:**
- Lista de pedidos con estado (Pendiente, Enviado, Entregado, Cancelado)
- Cambiar estado del pedido
- Ver detalles completos del pedido
- Historial de pedidos por cliente

---

### 3.4 Sistema de Usuarios (RF-004)

#### RF-004.1: Registro de usuario
**Historia:** Como visitante, quiero crear una cuenta para poder comprar.

**Criterios de aceptación:**
- Formulario: nombre, email, contraseña
- Validación de email (formato válido)
- Contraseña mínima 8 caracteres
- Redirección a página de inicio tras registro

#### RF-004.2: Inicio de sesión
**Historia:** Como usuario registrado, quiero iniciar sesión para acceder a mi cuenta.

**Criterios de aceptación:**
- Formulario: email, contraseña
- Recordarme (checkbox)
- Recuperar contraseña (envío por email - futuro)
- Mensaje de error si credenciales inválidas

#### RF-004.3: Perfil de usuario
**Historia:** Como cliente, quiero editar mi información personal.

**Criterios de aceptación:**
- Ver y editar: nombre, email, teléfono, dirección
- Guardar cambios correctamente

---

### 3.5 Wishlist/Favoritos (RF-005) - Opcional

**Historia:** Como cliente, quiero guardar productos para comprarlos después.

**Criterios de aceptación:**
- Botón "Agregar a favoritos" en productos
- Página de favoritos con lista de productos guardados
- Eliminar de favoritos

---

## 4. Modelo de Datos

### 4.1 Entidades Principales

```
Usuario (extiende Django User)
├── teléfono (optional)
├── dirección (optional)
└── fecha_registro (auto)

Género
├── nombre
├── slug
├── descripción
└── activo

Producto
├── título
├── slug
├── descripción_corta
├── descripción_larga
├── precio
├── precio_oferta (optional)
├── stock
├── activo
├── plataforma
├── género (FK)
├── fecha_lanzamiento (optional)
├── edad_minima (optional)
├── created_at (auto)
└── updated_at (auto)

Orden
├── usuario (FK)
├── estado (Pendiente/Enviado/Entregado/Cancelado)
├── total
├── dirección_envío
├── teléfono_contacto
├── notas (optional)
├── created_at (auto)
└── updated_at (auto)

OrdenItem
├── orden (FK)
├── producto (FK)
├── cantidad
├── precio_unitario
└── subtotal

Carrito (sesión o DB)
├── sesión o usuario
├── producto (FK)
└── cantidad
```

### 4.2 Estados de Orden

| Estado | Descripción |
|--------|-------------|
| Pendiente | Orden creada, esperando confirmación |
| Confirmado | Pago verificado, preparando envío |
| Enviado | Producto en camino |
| Entregado | Cliente recibió el producto |
| Cancelado | Orden cancelada |

---

## 5. Roadmap y Priorización

### Fase 1: Fundamentos (Semana 1)
**Objetivo:** Base técnica del proyecto

| Código | Entregable | Prioridad |
|--------|------------|-----------|
| F1.1 | Proyecto Django configurado | Must |
| F1.2 | Base de datos y modelos | Must |
| F1.3 | Templates base + static files | Should |
| F1.4 | App home (landing page) | Should |

### Fase 2: Catálogo (Semana 2)
**Objetivo:** Catálogo navegable de productos

| Código | Entregable | Prioridad |
|--------|------------|-----------|
| F2.1 | Modelos Producto y Género | Must |
| F2.2 | Lista de productos | Must |
| F2.3 | Detalle de producto | Must |
| F2.4 | Filtros por plataforma/género | Should |
| F2.5 | Admin CRUD de productos | Should |

### Fase 3: Carrito y Checkout (Semana 3)
**Objetivo:** Proceso de compra completo

| Código | Entregable | Prioridad |
|--------|------------|-----------|
| F3.1 | Carrito de compras | Must |
| F3.2 | Checkout | Must |
| F3.3 | Modelo de Orden | Must |
| F3.4 | Lista de pedidos (Admin) | Should |
| F3.5 | Detalle de orden | Should |

### Fase 4: Usuarios (Semana 4)
**Objetivo:** Sistema de autenticación

| Código | Entregable | Prioridad |
|--------|------------|-----------|
| F4.1 | Registro de usuarios | Must |
| F4.2 | Login/Logout | Must |
| F4.3 | Perfil de usuario | Should |
| F4.4 | Historial de pedidos (cliente) | Should |

### Fase 5: Extras (Semana 5+)
**Objetivo:** Funcionalidades adicionales

| Código | Entregable | Prioridad |
|--------|------------|-----------|
| F5.1 | Wishlist/Favoritos | Could |
| F5.2 | Mejora de búsqueda | Could |
| F5.3 | Reseñas de productos | Won't |

---

## 6. Supuestos y Restricciones

### 6.1 Supuestos
- El proyecto usará Django Templates (no SPA/API separada)
- Base de datos SQLite para desarrollo, PostgreSQL para producción
- Método de pago inicial: efectivo contra entrega
- No se manejan pagos con tarjeta (futuro)
- Productos físicos (no claves digitales)

### 6.2 Restricciones
- Un solo administrador (no multi-tenancy)
- Sin internacionalización (solo español inicial)
- Sin API pública (solo frontend server-side)

---

## 7. Riesgos Identificados

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Carrito no persiste entre sesiones | Medio | Alta | Guardar en DB asociado a usuario |
| Performance con muchos productos | Bajo | Baja | Paginación + select_related |
| Gestión de stock en compras concurrentes | Alto | Media | Transacciones atómicas |
| UX de checkout compleja | Medio | Media | Wireframes antes de implementar |

---

## 8. Glosario

| Término | Definición |
|---------|------------|
| SKU | Stock Keeping Unit - identificador interno del producto |
|slug | URL amigable del producto (ej: zelda-breath-of-wild) |
| Checkout | Proceso de finalizar la compra |
| Wishlist | Lista de productos guardados para comprar después |
| Orphan | Visitante sin sesión ni usuario |

---

## 9. Métricas de Éxito

| Métrica | Target |
|---------|--------|
| Tiempo de carga de página | < 2 segundos |
| Productos en catálogo | Mínimo 20 en launch |
| Checkout completion rate | > 60% |
| Errors en producción | 0% |

---

## 10. Próximos Pasos

1. Revisar y aprobar este PRD
2. Crear wireframes de páginas principales
3. Iniciar implementación de Fase 1
4. Primer demo interno al final de Fase 2

---

**Documento creado:** Marzo 2026
**Versión:** 2.0
**Estado:** Borrador para revisión