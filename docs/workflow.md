# Workflow de trabajo

Esta guía explica cómo usar herramientas de soporte sin perder foco pedagógico.

## Roles

- **Gentleman**: puerta de entrada para diagnóstico, dudas y cambios chicos.
- **SDD-Orchestrator**: para cambios grandes o multiarchivo con fases formales.
- **GGA**: gate de calidad antes de consolidar cambios.
- **Engram**: memoria/trazabilidad de decisiones y artifacts de cambio (detalle en [docs/tooling/engram.md](tooling/engram.md)).

## Cuándo usar cada uno

### Cambio chico (ejemplo)

"Ajustar texto en login":
1. Gentleman analiza.
2. Se aplica cambio puntual.
3. Se valida.
4. Se corre GGA antes de commit.

### Cambio grande (ejemplo)

"Reordenar documentación y roadmap":
1. Escalar a SDD-Orchestrator.
2. Fases: explore → proposal → spec → design → tasks → apply → verify.
3. Registrar decisiones relevantes en Engram.

## Principio pedagógico

El workflow multiagente es **soporte** para aprender mejor, no piloto automático.

## Contrato pedagógico

En este proyecto, el asistente no debe comportarse como generador automático de código sin contexto. Su rol principal es actuar como **mentor técnico-pedagógico**.

Eso implica:

- explicar conceptos antes de implementar,
- ayudar a evaluar si un cambio visto en el tutorial corresponde en esta fase del proyecto,
- señalar alternativas y tradeoffs cuando haga falta,
- corregir malentendidos con evidencia,
- y recién después acompañar la implementación con el flujo adecuado.

### Prioridad de trabajo

1. Comprender el concepto.
2. Evaluar si aplica al proyecto actual.
3. Decidir si conviene flujo directo o SDD.
4. Implementar.
5. Verificar.
6. Registrar aprendizajes y decisiones relevantes.

## Referencias clave

- Estado real del proyecto: [docs/project-state.md](project-state.md)
- Ruta de aprendizaje: [docs/learning-path.md](learning-path.md)
- Cuaderno de aprendizaje (público): [docs/learning-notebook.md](learning-notebook.md)
- Roadmap: [PRD.md](../PRD.md)

## Registro de aprendizaje vs trazabilidad operativa

- Usá [docs/learning-notebook.md](learning-notebook.md) cuando consolidás aprendizaje pedagógico por hito con evidencia verificable.
- Usá [docs/tooling/engram.md](tooling/engram.md) cuando necesitás trazabilidad operativa de decisiones, fases SDD y artifacts internos.
