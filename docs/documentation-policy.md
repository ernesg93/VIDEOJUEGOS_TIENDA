# Política de documentación

## Precedencia (source of truth)

1. Código + tests para comportamiento real.
2. `README.md` para onboarding.
3. `docs/project-state.md` para estado real actual.
4. `PRD.md` para visión y roadmap.
5. `docs/workflow.md` para operación de trabajo.
6. `CHANGELOG.md` para hitos ya integrados.

## Complemento pedagógico (fuera de precedencia)

- `docs/learning-notebook.md` es un cuaderno de aprendizaje público por hitos.
- No integra la cadena de source of truth: complementa onboarding/estudio con evidencia y reflexión técnica.
- No reemplaza `docs/learning-path.md`, `CHANGELOG.md` ni `docs/tooling/engram.md`.

## Ownership

- Owner principal: mantenedor/a del proyecto.
- Soporte: agentes según el tamaño del cambio.

## Checklist de alineación doc↔código

- [ ] Verificar apps activas en `INSTALLED_APPS`.
- [ ] Verificar rutas en `urlpatterns`.
- [ ] Verificar evidencia en tests existentes.
- [ ] Actualizar doc dueño en el mismo cambio.
- [ ] Si cambia algo visible, actualizar `CHANGELOG.md`.

## Regla para documentos ambiguos

Documentos fuera de foco (como `DOCS.md`) se dejan como stub/redirect con alcance explícito.
