# VIDEOJUEGOS_TIENDA

Proyecto Django para aprender construyendo una tienda de videojuegos.

## Empezá por acá (Django-first)

1. [README.md](README.md) (este archivo)
2. [docs/project-state.md](docs/project-state.md) (estado real actual)
3. [PRD.md](PRD.md) (roadmap)
4. [docs/learning-path.md](docs/learning-path.md) (ruta de aprendizaje)
5. [docs/workflow.md](docs/workflow.md) (cómo trabajar con soporte multiagente)

## Setup mínimo

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python tienda_videojuegos\manage.py migrate
python tienda_videojuegos\manage.py runserver
```

## Estado rápido

- Apps activas: `home`, `catalogo`, `buscador`, `usuarios`
- Rutas clave: `/`, `/catalogo/`, `/buscador/`, `/usuarios/login/`

## Calidad y documentación

- Convenciones: [AGENTS.md](AGENTS.md)
- Historial: [CHANGELOG.md](CHANGELOG.md)
- Política documental: [docs/documentation-policy.md](docs/documentation-policy.md)
- Referencia secundaria de tooling: [docs/tooling/engram.md](docs/tooling/engram.md)

> Este repositorio sigue un enfoque **Django-first**: fundamentos primero, features después.
