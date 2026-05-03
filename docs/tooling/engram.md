# Engram en este proyecto

Engram se usa como memoria persistente para decisiones, artifacts SDD y trazabilidad.

## Alcance

- Sí: guardar proposal/spec/design/tasks/apply-progress por cambio.
- Sí: registrar descubrimientos, decisiones y riesgos.
- No: reemplazar documentación pública del repo.

## Relación con la documentación principal

- Ruta principal de lectura: `README.md` + `docs/` + `PRD.md` + `CHANGELOG.md`.
- Engram queda como soporte operativo e histórico.

## Uso recomendado

1. Guardar artifacts por topic_key `sdd/<change>/...`.
2. Actualizar apply-progress por batch.
3. Usar verify para cerrar trazabilidad requisito → evidencia.
