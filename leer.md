Tengo el siguiente resultado:



Para lograr una implementación alineada con los objetivos de rigor arquitectónico y eficiencia multiagente, debes seguir este ciclo de vida de cinco fases:


Fase 1: Establecimiento de la "Constitución del Proyecto"


Antes de generar código, debes definir el "ADN arquitectónico" que todos los agentes deben respetar sin excepciones.


Prompt Sugerido: "Actúa como Agente Coordinador. Genera un archivo constitution.md que defina los principios inmutables del proyecto. Incluye:Principio de Biblioteca Primero: Cada funcionalidad debe nacer como una biblioteca independiente.


Mandato de Interfaz CLI: Toda funcionalidad debe ser accesible y testeable vía texto.


Imperativo de Test-First: Prohibido generar implementación antes de los tests.


Simplicidad: Priorizar soluciones directas sobre abstracciones prematuras."


Fase 2: Captura de Intención (Fase de Especificación)


En esta etapa, el enfoque es el "Qué" y el "Por qué", eliminando cualquier detalle técnico o de stack tecnológico para evitar restricciones prematuras.


Prompt Sugerido (Comando /speckit.specify): "Genera una especificación funcional detallada para [Funcionalidad X]. La IA debe actuar como Analista de Negocio (persona 'Mary'). El documento debe contener:Historias de Usuario: En formato 'Como [rol], quiero [acción], para [beneficio]'.


Criterios de Aceptación: Definidos en sintaxis EARS (Easy Approach to Requirements Syntax) o formato GIVEN/WHEN/THEN.


Restricciones Explícitas: Detalla qué no debe construir el sistema para evitar el 'vibe coding' y el drift arquitectónico."


Fase 3: Alineación Arquitectónica (Fase de Planificación)


Aquí se traduce la intención en una arquitectura técnica. Es donde el agente Arquitecto ('Winston') define el "Cómo".


Prompt Sugerido (Comando /speckit.plan): "Basado en la especificación aprobada, genera un plan.md. Identifica:Stack tecnológico y justificación de cada decisión.


Modelos de datos y contratos de API (OpenAPI/JSON Schema).


Análisis de Investigación: Los agentes de investigación deben validar la compatibilidad de librerías y dependencias antes de finalizar el plan.


Puertas de Complejidad: El agente debe justificar cualquier capa de abstracción adicional según los artículos de la Constitución."


Fase 4: Descomposición en Unidades Atómicas (Fase de Tareas)


Para que el sistema multiagente sea eficiente, el plan debe romperse en tareas tan pequeñas que quepan en la ventana de contexto del agente ejecutor.


Prompt Sugerido (Comando /speckit.tasks): "Descompón el plan.md en un archivo tasks.md. Cada tarea debe ser una unidad revisable, independiente y testeable.Usa marcadores [P] para tareas que pueden ejecutarse en paralelo por múltiples agentes.


Ordena las tareas por prioridad de historia de usuario (P1=MVP, P2=Importante).


Incluye la ruta exacta del archivo para cada tarea para evitar desorden en el escritorio contextal de la IA."


Fase 5: Ejecución Dirigida y Validación Continua


El agente Programador ('Devon') implementa mientras el agente Verificador asegura la fidelidad al contrato.


Prompt Sugerido (Comando /speckit.implement): "Ejecuta las tareas de tasks.md siguiendo estrictamente el flujo: Test -> Implementación -> Validación.El agente no puede marcar una tarea como completada si los tests no pasan al 100%.


Cualquier discrepancia encontrada no se arregla en el código, sino que debe propagarse de vuelta a la especificación original (Depuración de Especificaciones).


Usa un 'Agente Verificador' para validar el resultado contra el plan.md antes de permitir un Pull Request."



Quiero implemantarlo en mi agente orquestador. Que pasos debo seguir?

Para implementar este ciclo de vida de cinco fases en tu agente orquestador siguiendo el ecosistema de Gentleman AI, debes seguir estos pasos estructurados:
1. Preparación del Entorno (Gentle AI Stack)
El primer paso es instalar el núcleo del ecosistema que permite la orquestación y la memoria persistente
.
Instala el Gentle AI Stack ejecutando el comando brew install Gentleman-Programming/tap/gentle-ai (o el script correspondiente para tu OS) para configurar Engram y Agent Teams Lite de forma automática
.
Asegúrate de que tu agente principal (como Claude Code u OpenCode) esté configurado para actuar como un orquestador ligero que delega el trabajo real a sub-agentes
.
2. Configuración de la "Constitución" (Fase 1)
En el ecosistema sugerido, la "Constitución" reside en el archivo de contexto del proyecto
.
Crea o edita el archivo AGENTS.md (o CLAUDE.md/GEMINI.md según el agente) en la raíz de tu proyecto para definir los principios inmutables y la estructura de carpetas
.
Utiliza este archivo para imponer el "ADN arquitectónico", como el mandato de interfaz CLI y el imperativo de Test-First que mencionaste
.
Configura este archivo como el "enrutador" que indica al orquestador qué herramientas y convenciones seguir en cada etapa
.
3. Creación de Skills para cada Fase (Fases 2 a 4)
Debes transformar los prompts sugeridos en Skills específicas para que el orquestador pueda invocarlas bajo demanda
.
Crea una carpeta skills/ y dentro de ella subcarpetas para cada rol: spec-writer/ (Mary), architect/ (Winston) y task-planner/
.
En cada skill.md, incluye la metadata necesaria (trigger, scope y herramientas) junto con las instrucciones detalladas que definiste para las historias de usuario EARS y los modelos de datos
.
Registra estas skills en el AGENTS.md principal para que el orquestador sepa cuándo autoinvocarlas
.
4. Implementación de la Memoria Persistente con Engram
Para que el sistema sea eficiente y los sub-agentes no pierdan el hilo entre fases, debes usar Engram
.
Configura el MCP de Engram en tu agente para que cada decisión de la Fase 2 (especificación) y Fase 3 (plan) se guarde automáticamente en la base de datos SQLite local
.
Esto garantiza que cuando el sub-agente "Devon" (Fase 5) entre en escena, lo haga con una "página en blanco" en su ventana de contexto pero recupere las señales críticas desde Engram, evitando alucinaciones por exceso de ruido
.
5. Ejecución Dirigida y Validación (Fase 5)
La ejecución debe seguir el flujo de Spec-Driven Development (SDD)
.
Utiliza el comando /sdd-apply (o tu prompt de ejecución) para que el sub-agente implementador procese las tareas de tasks.md siguiendo estrictamente el flujo Test -> Implementación -> Validación
.
Para la validación final, integra Gentleman Guardian Angel (GGA) como un paso de pre-commit o CI, asegurando que el código cumpla con los estándares de la "Constitución" antes de permitir el Pull Request
.
Si se encuentra una discrepancia, el orquestador debe usar la función de "Depuración de Especificaciones", propagando el cambio hacia atrás y actualizando la memoria en Engram
.