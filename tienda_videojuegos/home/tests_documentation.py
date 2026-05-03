from pathlib import Path

from django.test import TestCase


class DocumentationRealignmentTests(TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]

    def _read(self, relative_path):
        return (self.repo_root / relative_path).read_text(encoding="utf-8")

    def test_core_docs_exist_with_expected_headings(self):
        expected_files = {
            "docs/project-state.md": "# Estado actual del proyecto",
            "docs/learning-path.md": "# Ruta de aprendizaje",
            "docs/workflow.md": "# Workflow de trabajo",
            "docs/documentation-policy.md": "# Política de documentación",
            "docs/tooling/engram.md": "# Engram en este proyecto",
        }

        for file_path, heading in expected_files.items():
            doc_path = self.repo_root / file_path
            self.assertTrue(doc_path.exists(), f"No existe {file_path}")
            self.assertIn(heading, self._read(file_path))

    def test_readme_prd_and_docs_stub_follow_new_hierarchy(self):
        readme = self._read("README.md")
        prd = self._read("PRD.md")
        docs_stub = self._read("DOCS.md")

        self.assertIn("docs/project-state.md", readme)
        self.assertIn("docs/learning-path.md", readme)
        self.assertIn("Django-first", readme)

        self.assertIn("Roadmap de aprendizaje", prd)
        self.assertIn("Estado real actual", prd)

        self.assertIn("stub de compatibilidad", docs_stub.lower())
        self.assertIn("docs/tooling/engram.md", docs_stub)

    def test_changelog_and_project_state_include_real_apps_and_tests(self):
        changelog = self._read("CHANGELOG.md")
        project_state = self._read("docs/project-state.md")

        for app_name in ["home", "catalogo", "buscador", "usuarios"]:
            self.assertIn(app_name, project_state)

        self.assertIn("tienda_videojuegos/home/tests.py", project_state)
        self.assertIn("tienda_videojuegos/usuarios/tests.py", project_state)
        self.assertIn("tienda_videojuegos/home/tests_documentation.py", project_state)
        self.assertIn("realineamiento documental pedagógico", changelog.lower())

    def test_project_state_has_explicit_requirement_traceability_table(self):
        project_state = self._read("docs/project-state.md")

        self.assertIn("## Trazabilidad de requirements (spec → docs)", project_state)
        self.assertIn("| Requirement (spec) | Archivo | Sección |", project_state)
        self.assertIn("Ruta de aprendizaje Django incremental", project_state)
        self.assertIn("Gobernanza de workflow multiagente", project_state)

    def test_readme_uses_explicit_markdown_links_and_design_order(self):
        readme = self._read("README.md")

        self.assertIn("[docs/project-state.md](docs/project-state.md)", readme)
        self.assertIn("[PRD.md](PRD.md)", readme)
        self.assertIn("[docs/learning-path.md](docs/learning-path.md)", readme)
        self.assertIn("[docs/workflow.md](docs/workflow.md)", readme)

        project_state_index = readme.index("[docs/project-state.md](docs/project-state.md)")
        prd_index = readme.index("[PRD.md](PRD.md)")
        learning_path_index = readme.index("[docs/learning-path.md](docs/learning-path.md)")
        workflow_index = readme.index("[docs/workflow.md](docs/workflow.md)")

        self.assertLess(project_state_index, prd_index)
        self.assertLess(prd_index, learning_path_index)
        self.assertLess(learning_path_index, workflow_index)

    def test_learning_path_has_executable_stage_structure(self):
        learning_path = self._read("docs/learning-path.md")

        for stage_number in [1, 2, 3, 4]:
            self.assertIn(f"## Etapa {stage_number}", learning_path)

        self.assertEqual(learning_path.count("- **Objetivo**:"), 4)
        self.assertEqual(learning_path.count("- **Prerrequisitos**:"), 4)
        self.assertEqual(learning_path.count("- **Resultado observable**:"), 4)

    def test_workflow_clearly_maps_small_and_high_impact_changes(self):
        workflow = self._read("docs/workflow.md")

        self.assertIn("Cambio chico", workflow)
        self.assertIn("Gentleman analiza.", workflow)
        self.assertIn("Se corre GGA antes de commit.", workflow)

        self.assertIn("Cambio grande", workflow)
        self.assertIn("Escalar a SDD-Orchestrator.", workflow)
        self.assertIn("explore → proposal → spec → design → tasks → apply → verify", workflow)

        self.assertIn("soporte", workflow.lower())
        self.assertIn("no piloto automático", workflow.lower())
