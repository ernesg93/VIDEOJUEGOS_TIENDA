# PRD - Tienda de Videojuegos (Versión Mejorada)

## Product Requirements Document
### Versión 1.1 - Marzo 2025 (Mejorado para claridad y priorización)

---

## 3. Requisitos Funcionales (Versión Mejorada)

### 3.1 Sistema de Catálogo

#### RF-001: Gestión de Productos
**Historia:** Como administrador, quiero gestionar el catálogo de videojuegos (agregar, editar, eliminar productos) para mantener la tienda actualizada y atractiva para los clientes.

**Enfoque de implementación:** Desarrollaremos esta funcionalidad de forma incremental, entregando valor temprano a través de un producto mínimo viable antes de añadir complejidad.

**Campos del Producto (agrupados por propósito lógico):**

| Categoría | Campo | Tipo | Requerido | Descripción | Fase de implementación |
|-----------|-------|------|-----------|-------------|------------------------|
| **Identificación** | `id` | AutoField | Sí | Identificador único del producto (PK) | Fase 2.1 |
| | `slug` | SlugField | Sí | URL amigable (ej: zelda-breath-of-wild) | Fase 2.2 |
| **Contenido Esencial** | `titulo` | CharField(200) | Sí | Nombre completo del videojuego | Fase 2.1 |
| | `descripcion_corta` | CharField(300) | No | Descripción breve para listados | Fase 2.3 |
| | `descripcion_larga` | TextField | No | Descripción detallada del juego | Fase 2.3 |
| **Información de Comercio** | `precio` | DecimalField(8,2) | Sí | Precio en USD (ej: 59.99) | Fase 2.1 |
| | `precio_oferta` | DecimalField(8,2) | No | Precio con descuento aplicado | Fase 2.4 |
| | `stock` | IntegerField | Sí | Cantidad disponible en inventario | Fase 2.1 |
| | `activo` | BooleanField | Sí | Visible y disponible para compra | Fase 2.1 |
| **Clasificación** | `plataforma` | CharField(20) | Sí | Plataforma objetivo (PC, PS5, XBOX, SWITCH) | Fase 2.2 |
| | `genero` | ForeignKey(Género) | No | Categoría de juego (Acción, RPG, Deportes, etc.) | Fase 2.3 |
| | `edad_minima` | IntegerField | No | Edad mínima recomendada (ej: 12, 16, 18) | Fase 2.4 |
| **Metadatos y Auditoría** | `fecha_lanzamiento` | DateField | No | Fecha oficial de lanzamiento | Fase 2.2 |
| | `created_at` | DateTimeField | Auto | Fecha de creación del registro | Fase 2.1 |
| | `updated_at` | DateTimeField | Auto | Última fecha de modificación | Fase 2.1 |

> 💡 **Notas de implementación:**
> - **Fase 2.1 (MVP Catálogo):** Solo campos marcados como "Fase 2.1" son necesarios para lanzar una versión básica funcional
> - **Fase 2.2:** Añadimos experiencia de usuario (slug, plataforma, fecha de lanzamiento)
> - **Fase 2.3:** Enriquecemos contenido (descripciones, género)  
> - **Fase 2.4:** Funcionalidades avanzadas de comercio y clasificación
> - Todos los campos mantienen sus tipos y restricciones originales, solo se implementan progresivamente

#### RF-002: Gestión de Categorías/Géneros
**Historia:** Como administrador, quiero organizar los videojuegos por género/categoría para facilitar la navegación y descubrimiento por parte de los clientes.

**Campos de Género (implementación completa en Fase 2.3):**
| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| `id` | AutoField | Sí | Identificador único |
| `nombre` | CharField(100) | Sí | Nombre del género (ej: "Acción", "RPG") |
| `slug` | SlugField | Sí | URL amigable (ej: accion, rpg) |
| `descripcion` | TextField | No | Descripción del género |
| `activo` | BooleanField | Sí | Género visible en filtros |

---

## 6. Roadmap Mejorado con Priorización Interna

### Fase 2: Catálogo de Productos (Detallado con Priorización)

**Objetivo de la fase:** Tener un catálogo navegable donde los clientes puedan ver productos, filtrarlos básicamente y ver detalles individuales.

**Priorización interna usando método MoSCoW (dentro de la fase):**

| Prioridad | Código | Entregable | Dependencia | Valor para Usuario | Esfuerzo Relativo | Comentario de Implementación |
|-----------|--------|------------|-------------|-------------------|-------------------|------------------------------|
| **Must** | M2.1 | Modelos Producto y Género | Ninguna | Alta (base de todo) | Baja | Crear migraciones y ejecutar |
| **Must** | M2.2 | Vista Detalle de Producto | M2.1 | Alta (impacto directo en conversión) | Media | Template con imagen, título, precio |
| **Should** | S2.1 | Vista Lista de Productos (sin filtros) | M2.1, M2.2 | Media (descubrimiento de productos) | Baja-Media | Grid simple de productos activos |
| **Could** | C2.1 | Filtros básicos por plataforma | S2.1 | Baja (mejora de experiencia) | Media | Dropdown de plataformas en lista |
| **Could** | C2.2 | CRUD completo de admin para Productos | M2.1 | Baja (solo para administradores) | Baja | Usar Django admin o vistas custom |
| **Won't** | W2.1 | Sistema de reseñas y calificaciones | M2.2 | Baja (valor diferido) | Alta | Dejar para Fase 3 o 4 |
| **Won't** | W2.2 | Búsqueda full-text avanzada | S2.1 | Baja (sobrecargo inicial) | Alta | Implementar con PostgreSQL Search o Haystack posteriormente |

**Flujo de implementación recomendado para Fase 2:**
```
1. M2.1 → Crear modelos Producto y Género (migraciones)
2. M2.2 → Implementar vista y template de detalle de producto
3. S2.1 → Crear vista lista de productos (grid básico)
2. C2.1 → Añadir filtros simples por plataforma (opcional, depende de tiempo)
4. C2.2 → Implementar CRUD de admin (puede ser Django admin out-of-the-box)
```

**Definición de Done para Fase 2 (MVP Catálogo):**
- [ ] Modelo Producto creado con campos mínimos (id, titulo, precio, stock, activo, plataforma, slug)
- [ ] Modelo Género creado y poblado con valores iniciales (Acción, RPG, Deportes, Estrategia)
- [ ] Vista detalle de producto accesible en `/producto/<slug:slug>/` mostrando imagen, título, precio, plataforma
- [ ] Vista lista de productos accesible en `/catalogo/` mostrando grid de productos activos
- [ ] Navegación básica desde lista → detalle funcionando
- [ ] Diseño responsivo que se ve bien en móvil (<576px) y desktop
- [ ] Al menos 3 productos de ejemplo cargados en la base de datos
- [ ] Sin errores 500 en las vistas principales
- [ ] Tests básicos de modelos pasando (creación, lectura, actualización)

### Fase 3: Sistema de Usuarios (Ejemplo de aplicación de priorización)
*(Mostrando cómo aplicar el mismo principio a otras fases)*

**Objetivo de la fase:** Permitir a los usuarios crear cuentas, iniciar sesión y mantener perfiles personalizados.

**Priorización interna:**
| Prioridad | Código | Entregable | Valor para Usuario | Comentario |
|-----------|--------|------------|-------------------|------------|
| **Must** | M3.1 | Modelo Usuario extendido (perfil básico) | Alta | Heredar de AbstractUser, añadir campos esenciales |
| **Must** | M3.2 | Sistema de registro y login | Alta | Funcionalidad crítica para conversión |
| **Should** | S3.1 | Vista de perfil de usuario | Media | Permite edición de datos personales |
| **Could** | C3.1 | Recuperación de contraseña por email | Baja-Media | Mejora experiencia, no bloqueante |
| **Won't** | W3.1 | Autenticación social (Google, Facebook) | Baja | Valor alto pero esfuerzo alto para Fase 4 |

---

## 11. Apéndice Mejorado: Guía de Escritura de Requisitos

### 11.1 Cómo escribir buenas Historias de Usuario (User Stories)

**Formato estándar:** 
```
Como [tipo de usuario], 
Quiero [acción o funcionalidad] 
Para [beneficio o valor que se obtiene]
```

**Ejemplos buenos vs malos:**

❌ **Mal:** "Quiero un botón de compra"
✅ **Bien:** "Como visitante, quiero un botón 'Añadir al carrito' visible en cada producto para poder agregar artículos fácilmente a mi compra"

❌ **Mal:** "Necesito mejor seguridad"  
✅ **Bien:** "Como administrador, quiero que el sistema bloquee automáticamente tras 5 intentos fallidos de login para proteger contra ataques de fuerza bruta"

### 11.2 Técnica de Escritura en Capas (Layered Writing)

Para evitar especificaciones demasiado densas, usar este enfoque:

**Capa 1: Esencia (Qué y Por qué)**
> Como [usuario], quiero [funcionalidad] para [beneficio]

**Capa 2: Detalles esenciales (Cómo mínimo)**
- Lista de 3-5 elementos críticos que definen lo indispensable
- Señalar claramente qué se puede dejar para fases futuras

**Capa 3: Detalles de implementación (Opcional)**
- Técnicas específicas, patrones de diseño, consideraciones técnicas
- Solo incluir si es crítico para la toma de decisiones

**Ejemplo aplicado a un filtro de precio:**

> **Capa 1:** Como visitante, quiero filtrar productos por rango de precio para encontrar opciones dentro de mi presupuesto.
> 
> **Capa 2:** 
> - Rango mínimo y máximo seleccionable por el usuario
> - Resultado actualizado en tiempo real (sin recarga completa de página)
> - Mostrar cantidad de resultados encontrados
> 
> **Capa 3:** 
> - Implementar con JavaScript vanilla (evitar dependencias adicionales)
> - Usar eventos de entrada con debounce (300ms) para evitar sobrecarga
> - Almacenar preferencia en localStorage para persistir entre sesiones

Este enfoque permite que diferentes lectores obtengan el nivel de detalle que necesitan:
- **Stakeholders de negocio:** Leen solo Capa 1
- **Desarrolladores:** Lee Capas 1 y 2 para entender qué construir
- **Arquitectos técnicos:** Revisan todas las capas para evaluar implicaciones técnicas

---

## 12. Próximos Pasos Sugeridos (Basado en esta mejora)

Si quisiera aplicar esta mejora a todo el PRD ahora mismo:

1. **Seleccione una sección densa** (ej: los campos de cualquier modelo)
2. **Aplique la agrupación por propósito** (Identificación, Contenido, Comercio, etc.) 
3. **Añada una columna de "Fase de implementación"** o "Prioridad" 
4. **Incluya una nota explicativa** sobre el orden recomendado de implementación
5. **Para roadmaps existentes, agregue una tabla de priorización interna** usando el formato mostrado arriba

**Ejercicio práctico:** Tome la sección de "Sistema de Usuarios" (RF-003 al RF-005) y reesgrúpela siguiendo estos principios. Notará cómo inmediatamente se vuelve más actionable y menos abrumador de leer.

Esta técnica de mejora no cambia qué se está construyendo - solo hace que la especificación sea más útil como herramienta de trabajo diario para el equipo de desarrollo. El verdadero valor está en poder mirar el documento y saber exactamente *qué hacer primero* para entregar valor temprano mientras se aprende y se avanza hacia la visión completa. 

¿Le gustaría que aplique esta mejora a otra sección específica del PRD para ver el contraste antes y después? Puedo tomar la sección de Sistema de Usuarios o Carrito de Compras y mostrarle el transformación completa. 

En caso contrario, el PRD en su estado actual ya cumple excelente mente con su propósito como directiva de especificaciones, y estas son simplemente sugerencias para elevarlo de excelente a ejemplar en términos de usabilidad como herramienta de trabajo diario. 

**Nota final:** La versión actual del PRD (antes de esta mejora) ya era de alta calidad (4.7/5 en mi evaluación inicial). Esta versión mejorada busca alcanzar el 5/5 abordando específicamente los dos puntos que usted mismo identificó como oportunidades de crecimiento: claridad/legibilidad y priorización dentro de fases. Ambas son habilidades que se desarrollan con la práctica, y el hecho de que usted las haya identificado muestra un excelente juicio profesional. 

¿Hay alguna otra sección que le gustaría que mejore siguiendo estos mismos principios? Estoy aquí para ayudar. 

**Product Requirements Document - Tienda de Videojuegos**
**Versión 1.1 - Marzo 2025 (Mejorado para claridad y priorización)**

[El resto del PRD permanece igual que en la versión anterior, con solo las secciones mejoradas según se muestra arriba]
