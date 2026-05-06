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


class LearningNotebookDocumentationTests(TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]

    def _read(self, relative_path):
        return (self.repo_root / relative_path).read_text(encoding="utf-8")

    def test_learning_notebook_exists_with_main_heading_and_purpose(self):
        notebook_path = self.repo_root / "docs/learning-notebook.md"
        self.assertTrue(notebook_path.exists(), "No existe docs/learning-notebook.md")

        notebook = self._read("docs/learning-notebook.md")
        self.assertIn("# Cuaderno de aprendizaje", notebook)
        self.assertIn("aprendizaje por hitos", notebook.lower())
        self.assertIn("evidencia", notebook.lower())
        self.assertIn("no es una bitácora automática", notebook.lower())

    def test_learning_notebook_is_linked_from_core_docs(self):
        readme = self._read("README.md")
        learning_path = self._read("docs/learning-path.md")
        workflow = self._read("docs/workflow.md")
        policy = self._read("docs/documentation-policy.md")

        self.assertIn("[docs/learning-notebook.md](docs/learning-notebook.md)", readme)
        self.assertIn("[docs/learning-notebook.md](learning-notebook.md)", learning_path)
        self.assertIn("[docs/learning-notebook.md](learning-notebook.md)", workflow)
        self.assertIn("docs/learning-notebook.md", policy)

    def test_learning_notebook_declares_document_boundaries(self):
        notebook = self._read("docs/learning-notebook.md")

        self.assertIn("docs/learning-path.md", notebook)
        self.assertIn("CHANGELOG.md", notebook)
        self.assertIn("docs/tooling/engram.md", notebook)
        self.assertIn("plan de estudio", notebook.lower())
        self.assertIn("historial de cambios integrados", notebook.lower())
        self.assertIn("trazabilidad operativa", notebook.lower())

    def test_seed_milestones_include_required_seven_block_structure(self):
        notebook = self._read("docs/learning-notebook.md")

        for milestone in [
            "## Hito 0 — Mapa documental y reglas del repo",
            "## Hito 1 — Request/response + URLs/templates",
            "## Hito 2 — Auth básica",
            "## Hito 3 — Evolución segura del catálogo",
        ]:
            self.assertIn(milestone, notebook)

        for required_block in [
            "### Contexto",
            "### Conceptos clave",
            "### Evidencia en código y docs",
            "### Criterio / decisión",
            "### Errores o malentendidos",
            "### Checklist de autoverificación",
            "### Próximo paso",
        ]:
            self.assertEqual(notebook.count(required_block), 4)

    def test_learning_notebook_contains_minimum_concept_index_and_maintenance_rules(self):
        notebook = self._read("docs/learning-notebook.md")

        self.assertIn("## Índice conceptual mínimo", notebook)
        self.assertIn("- [Request/response](#hito-1--requestresponse--urlstemplates)", notebook)
        self.assertIn("- [URLs y templates](#hito-1--requestresponse--urlstemplates)", notebook)
        self.assertIn("- [Autenticación básica](#hito-2--auth-básica)", notebook)

        self.assertIn("## Mantenimiento", notebook)
        self.assertIn("por hito", notebook.lower())
        self.assertIn("no diaria", notebook.lower())
        self.assertIn("evidencia", notebook.lower())
        self.assertIn("checklist", notebook.lower())

    def test_changelog_mentions_learning_notebook_addition(self):
        changelog = self._read("CHANGELOG.md")
        self.assertIn("docs/learning-notebook.md", changelog)

    def test_learning_notebook_hito_1_evidence_paths_are_verifiable(self):
        notebook = self._read("docs/learning-notebook.md")

        self.assertIn("tienda_videojuegos/templates/base.html", notebook)
        self.assertIn("tienda_videojuegos/catalogo/templates/catalogo/", notebook)

        self.assertTrue(
            (self.repo_root / "tienda_videojuegos/templates/base.html").exists(),
            "Debe existir template base en ruta real del repo",
        )
        self.assertTrue(
            (self.repo_root / "tienda_videojuegos/catalogo/templates/catalogo").exists(),
            "Debe existir carpeta templates del catálogo en ruta real del repo",
        )

    def test_learning_path_and_notebook_keep_plan_vs_evidence_boundaries(self):
        learning_path = self._read("docs/learning-path.md")
        notebook = self._read("docs/learning-notebook.md")

        self.assertIn("plan de estudio", learning_path.lower())
        self.assertIn("evidencia", notebook.lower())

    def test_workflow_and_policy_define_notebook_vs_engram_semantics(self):
        workflow = self._read("docs/workflow.md")
        policy = self._read("docs/documentation-policy.md")

        self.assertIn("consolidás aprendizaje pedagógico por hito", workflow.lower())
        self.assertIn("engram", workflow.lower())
        self.assertIn("fuera de precedencia", policy.lower())


class PedagogicalTraceabilityContractTests(TestCase):
    ETAPA_3_FUNCTIONAL_TOKENS = [
        "catálogo paginado",
        "query string",
        "?q=",
        "tienda_videojuegos/catalogo",
        "tienda_videojuegos/buscador",
    ]

    ETAPA_3_CONCEPTUAL_TOKENS = [
        "## Etapa 3",
        "resultado observable",
        "catálogo y buscador",
    ]

    ETAPA_3_DOCUMENTARY_TOKENS = [
        "docs/project-state.md",
        "docs/learning-path.md",
        "complemento pedagógico",
    ]

    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]

    def _read(self, relative_path):
        return (self.repo_root / relative_path).read_text(encoding="utf-8")

    def _assert_contains_tokens(self, document, tokens, message):
        for token in tokens:
            self.assertIn(token, document, f"{message}: falta token '{token}'")

    def test_project_state_contains_explicit_etapa_3_pagination_and_query_evidence(self):
        project_state = self._read("docs/project-state.md")

        self.assertIn("Etapa 3", project_state)
        self._assert_contains_tokens(
            project_state,
            self.ETAPA_3_FUNCTIONAL_TOKENS,
            "La evidencia funcional de Etapa 3 debe estar en project-state",
        )

    def test_learning_notebook_role_is_complementary_not_canonical(self):
        notebook = self._read("docs/learning-notebook.md").lower()

        self.assertIn("complemento pedagógico", notebook)
        self.assertIn("docs/project-state.md", notebook)
        self.assertIn("fuente canónica", notebook)

    def test_learning_path_and_project_state_keep_notebook_role_consistent(self):
        project_state = self._read("docs/project-state.md").lower()
        learning_path = self._read("docs/learning-path.md").lower()

        self.assertIn("complemento pedagógico", project_state)
        self.assertIn("complemento pedagógico", learning_path)
        self.assertIn("fuente canónica", project_state)
        self.assertIn("fuente canónica", learning_path)

    def test_traceability_claims_preserve_functional_conceptual_documentary_evidence_triad(self):
        project_state = self._read("docs/project-state.md").lower()
        learning_path = self._read("docs/learning-path.md").lower()
        notebook = self._read("docs/learning-notebook.md").lower()

        self._assert_contains_tokens(
            project_state,
            [token.lower() for token in self.ETAPA_3_FUNCTIONAL_TOKENS],
            "Falta evidencia funcional",
        )
        self._assert_contains_tokens(
            learning_path,
            [token.lower() for token in self.ETAPA_3_CONCEPTUAL_TOKENS],
            "Falta evidencia conceptual",
        )
        self._assert_contains_tokens(
            notebook,
            [token.lower() for token in self.ETAPA_3_DOCUMENTARY_TOKENS],
            "Falta evidencia documental",
        )

    def test_scope_guard_declares_non_functional_runtime_boundary_for_traceability_change(self):
        project_state = self._read("docs/project-state.md").lower()

        self.assertIn("sin cambios en runtime", project_state)
        self.assertIn("catalogo/views.py", project_state)
        self.assertIn("buscador/views.py", project_state)
