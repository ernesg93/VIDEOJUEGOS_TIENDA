# Política de documentación

## Precedencia (source of truth)

1. Código + tests para comportamiento real.
2. `README.md` para onboarding.
3. `docs/project-state.md` para estado real actual.
4. `PRD.md` para visión y roadmap.
5. `docs/workflow.md` para operación de trabajo.
6. `CHANGELOG.md` para hitos ya integrados.

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
