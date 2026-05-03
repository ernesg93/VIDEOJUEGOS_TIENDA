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

## Referencias clave

- Estado real del proyecto: [docs/project-state.md](project-state.md)
- Ruta de aprendizaje: [docs/learning-path.md](learning-path.md)
- Roadmap: [PRD.md](../PRD.md)
