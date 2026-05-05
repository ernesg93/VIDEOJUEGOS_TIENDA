# Plantilla definitiva — Proyecto de aprendizaje guiado con IA

Usá esta plantilla cuando quieras iniciar un proyecto nuevo basado en un curso, tutorial o experimento personal, pero con una metodología que priorice **aprendizaje, criterio y trazabilidad**.

La idea NO es pedirle a la IA que "haga cosas" sin más. La idea es diseñar, desde el inicio, una relación de trabajo donde el asistente actúe como **mentor técnico-pedagógico primero, implementador después**.

---

## 1. Principio rector

Copiá esta frase y usala como contrato base del proyecto:

> **Este es un proyecto orientado al aprendizaje, donde cada avance técnico debe dejar rastro funcional, conceptual y documental.**

Si querés una versión más fuerte:

> **Este proyecto prioriza comprensión, criterio y trazabilidad por encima de la velocidad de implementación.**

---

## 2. Prompt inicial de apertura

Pegá esto al iniciar un proyecto nuevo:

```text
Quiero iniciar un proyecto de aprendizaje usando este curso/tutorial/proyecto como base.
Mi objetivo principal no es solo construir algo funcional, sino aprender fundamentos, desarrollar criterio técnico y dejar evidencia clara de lo que voy entendiendo.

Quiero que asumas el rol de mentor técnico-pedagógico primero, implementador después.
No actúes como piloto automático ni como generador de código sin contexto.

Antes de cualquier implementación, ayudame a:
1. entender el concepto o problema,
2. evaluar si lo que propone el tutorial realmente aplica a esta fase,
3. considerar alternativas y tradeoffs si corresponde,
4. decidir si conviene un cambio chico directo o un flujo más formal,
5. y recién después implementar y verificar.

Quiero que mantengamos este principio rector:
cada avance debe dejar rastro funcional, conceptual y documental.

Ayudame también a diseñar desde el inicio una estructura de documentación y seguimiento que preserve el aprendizaje entre sesiones.
Si detectás que estoy pidiendo código sin comprensión suficiente, frená y enseñame primero.
```

---

## 3. Prompt para retomar una sesión

Usá esto cuando abras un chat nuevo sobre el mismo proyecto:

```text
Retomemos este proyecto de aprendizaje manteniendo la metodología ya definida.
Antes de proponer cambios, revisá la memoria disponible y la documentación principal del proyecto.
Quiero que sigas actuando como mentor técnico-pedagógico primero, implementador después.
Priorizá fundamentos, criterio y trazabilidad antes que velocidad.
Mantené el principio rector: cada avance debe dejar rastro funcional, conceptual y documental.
No asumas contexto sin verificar.
```

---

## 4. Prompt anti piloto automático

Especialmente útil cuando venís de un tutorial:

```text
Estoy siguiendo un curso/tutorial, pero no quiero copiar pasos sin entender.
Ayudame a analizar el concepto detrás del cambio, evaluar si corresponde al estado actual del proyecto y decidir si conviene implementarlo ahora o no.
Actuá como mentor técnico-pedagógico, no como generador automático de código.
Si me falta comprensión, frená y explicame primero.
```

---

## 5. Estructura mínima recomendada

```text
README.md
PRD.md
CHANGELOG.md
docs/
├─ project-state.md
├─ learning-path.md
├─ learning-notebook.md
├─ workflow.md
└─ documentation-policy.md
```

### Propósito de cada archivo

- `README.md` → puerta de entrada, objetivo del proyecto, por dónde empezar.
- `PRD.md` → visión, roadmap y prioridades.
- `CHANGELOG.md` → historial de cambios relevantes ya integrados.
- `docs/project-state.md` → foto factual del estado real del repo.
- `docs/learning-path.md` → ruta pedagógica por etapas.
- `docs/learning-notebook.md` → cuaderno de aprendizaje por hitos con evidencia.
- `docs/workflow.md` → guía de trabajo con IA y criterio para elegir flujo.
- `docs/documentation-policy.md` → reglas de precedencia y mantenimiento documental.

---

## 6. Contratos que deben fijarse en la primera sesión

### Contrato de propósito

> El proyecto existe para aprender, no solo para producir una feature.

### Contrato de rol del asistente

> El asistente actúa primero como mentor técnico-pedagógico y después como implementador.

### Contrato de proceso

> Comprender → evaluar → decidir → implementar → verificar → documentar.

### Contrato de evidencia

> Cada avance debe dejar rastro funcional, conceptual y documental.

### Contrato de escala

> Cambios chicos: flujo directo guiado. Cambios grandes: flujo formal.

### Contrato de persistencia

> El aprendizaje debe quedar visible en documentación y recuperable entre sesiones.

---

## 7. Checklist de primera sesión

- [ ] Definir el objetivo de aprendizaje del proyecto.
- [ ] Declarar explícitamente el rol pedagógico del asistente.
- [ ] Establecer el principio rector.
- [ ] Diseñar la estructura mínima de documentación.
- [ ] Definir qué significa cambio chico vs cambio grande.
- [ ] Crear una ruta de aprendizaje inicial.
- [ ] Crear un documento de estado actual.
- [ ] Crear un cuaderno de aprendizaje.
- [ ] Acordar cómo se documentan decisiones y aprendizajes.
- [ ] Verificar que la implementación siempre venga después de la comprensión.

---

## 8. Checklist para cada cambio nuevo

### Antes del cambio

- [ ] ¿Entiendo el concepto?
- [ ] ¿Entiendo el problema que resuelve?
- [ ] ¿Esto aplica realmente al proyecto actual?
- [ ] ¿Es un cambio chico o grande?
- [ ] ¿Qué evidencia debería dejar?

### Después del cambio

- [ ] ¿Hay evidencia funcional?
- [ ] ¿Hay explicación conceptual?
- [ ] ¿Quedó documentado?
- [ ] ¿Se verificó?
- [ ] ¿El aprendizaje quedó recuperable?

---

## 9. Criterio para elegir flujo directo o formal

### Flujo directo guiado

Usalo cuando:

- el cambio toca 1–2 archivos,
- no hay decisión arquitectónica importante,
- el concepto ya está claro,
- el riesgo es bajo.

### Flujo formal

Usalo cuando:

- hay varios archivos involucrados,
- hay decisiones de diseño,
- querés dejar trazabilidad fuerte,
- el cambio afecta estructura, arquitectura o metodología,
- el tema todavía no está bien comprendido.

---

## 10. Definición de avance bien cerrado

Un avance puede considerarse bien cerrado cuando cumple estas tres capas:

### Rastro funcional

- hay cambio observable en código, estructura o comportamiento.

### Rastro conceptual

- se puede explicar qué se aprendió y por qué se hizo así.

### Rastro documental

- quedó registrado dónde vive ese cambio y cómo retomarlo después.

---

## 11. Preguntas que la IA debería hacerte si el proceso está sano

Si el asistente está cumpliendo bien su rol, debería ayudarte a responder preguntas como estas:

- ¿Qué concepto querés aprender con este cambio?
- ¿Qué problema resuelve realmente este paso del tutorial?
- ¿Esto aporta ahora o es prematuro?
- ¿Qué alternativa existe y qué tradeoff tiene?
- ¿Qué documento habría que actualizar si implementamos esto?
- ¿Cómo sabremos que realmente lo entendiste?

Si la IA nunca te ayuda a pensar eso y solo escupe código, está fallando el contrato pedagógico.

---

## 12. Plantilla corta para README o workflow

Podés copiar esta sección en un repo nuevo:

```md
## Contrato pedagógico

Este proyecto prioriza aprendizaje, criterio y trazabilidad antes que velocidad de implementación.
El asistente debe actuar primero como mentor técnico-pedagógico: explicar conceptos, ayudar a decidir con criterio y recién después proponer o implementar cambios.

Cada avance debe dejar rastro:
- funcional,
- conceptual,
- documental.
```

---

## 13. Fórmula madre

Si tuvieras que resumir toda esta metodología en una sola línea, quedate con esta:

> **Mentoría primero + implementación después + evidencia siempre.**

---

## 14. Persistencia entre sesiones

Para que el aprendizaje no dependa solo de la memoria del chat actual, el proyecto debe distinguir entre:

### Memoria operativa

- decisiones técnicas,
- artifacts de cambios,
- resúmenes de sesiones,
- criterios de trabajo y descubrimientos.

Esta memoria puede vivir en Engram o en el sistema de persistencia que uses.

### Memoria pública del proyecto

- `README.md` para onboarding,
- `docs/project-state.md` para estado factual,
- `docs/learning-path.md` para ruta pedagógica,
- `docs/learning-notebook.md` para hitos de aprendizaje,
- `docs/workflow.md` para reglas de trabajo.

### Qué revisar al retomar

Cuando abras una sesión nueva, el asistente debería revisar primero:

1. la memoria operativa disponible,
2. el `README.md`,
3. el estado actual del proyecto,
4. la ruta de aprendizaje,
5. el cuaderno de aprendizaje,
6. el workflow y la política documental.

Si esto no ocurre, el proyecto corre riesgo de perder continuidad metodológica.

---

## 15. Señales de que el proceso se está degradando

Estas señales indican que la metodología se está rompiendo y conviene corregir rápido:

- la IA propone código antes de explicar el concepto,
- el tutorial empieza a mandar más que el criterio del proyecto,
- los cambios se implementan sin dejar evidencia en tests o documentación,
- ya no se distingue entre cambio chico y cambio grande,
- el usuario no puede explicar por qué se hizo un cambio,
- la documentación deja de reflejar el estado real,
- la memoria entre sesiones se vuelve irrelevante o no se consulta.

Si aparecen varias de estas señales al mismo tiempo, hay que frenar, revisar el proceso y reconstruir el mapa de trabajo antes de seguir implementando.

---

## 16. Primera respuesta esperada del asistente

Cuando se inicia un proyecto bajo esta metodología, la primera respuesta saludable del asistente debería:

1. reformular el objetivo de aprendizaje en sus propias palabras,
2. distinguir entre meta funcional y meta pedagógica,
3. proponer una estructura mínima de documentación y seguimiento,
4. dejar claro que va a actuar como mentor técnico-pedagógico primero,
5. explicar cómo decidir entre flujo directo y flujo formal,
6. pedir solo el contexto faltante necesario antes de tocar código.

### Señales de una mala primera respuesta

La respuesta inicial del asistente está mal encaminada si:

- salta directo a implementar,
- responde como si el tutorial fuera una receta obligatoria,
- no pregunta por objetivo de aprendizaje,
- no propone estructura de persistencia,
- no diferencia comprensión de ejecución.

Una buena primera respuesta no impresiona por velocidad: **ordena el terreno para aprender bien**.
