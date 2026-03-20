¡Mirá, che! Acabas de ver que la delegación **sí funciona**: el agente `general` listó el contenido del directorio y nos devolvió el resultado sin problemas.  
Entonces, el inconveniente que tenías antes no era con el sistema de delegación en sí, sino con **cómo se estaba invocando** o con **qué se le estaba pidiendo al agente**.

A continuación te dejo una guía rápida (en rioplantense, como te gusta) para que tus próximas delegaciones cierren siempre con un resultado y no se queden “colgadas”.

---

## 🔧 ¿Por qué una delegación puede parecer que no termina?

| Posible causa | Qué hacer |
|---------------|-----------|
| **Nombre de agente incorrecto** | Los únicos agentes válidos son: `general`, `explore`, y todos los `sdd-*` (`sdd-apply`, `sdd-design`, `sdd-explore`, `sdd-init`, `sdd-propose`, `sdd-spec`, `sdd-tasks`, `sdd-verify`, `sdd-archive`). Si escribiste `assistant`, `worker` o cualquier otro nombre, el sistema responde `Agent "X" not found`. |
| **Prompt demasiado vago o sin acción clara** | El agente necesita una instrucción concreta: <br>• ❌ “Ayudá con esto” <br>• ✅ “Creá un archivo `src/components/Button.tsx` con un botón reutilizable usando Tailwind y TypeScript”. <br>Si el prompt no pide nada específico, el agente puede terminar sin producir salida. |
| **Falta de skills necesarias** | Algunos agentes (especialmente los `sdd-*`) esperan que ciertas skills estén cargadas antes de ejecutar. El orchestrador suele resolverlas automáticamente, pero si estás delegando manualmente podés añadir al prompt: <br>`SKILL: Load /ruta/a/la/skill.md` <br>Ejemplo: si le pedís escribir un componente de React, asegurate de que cargue `react-19` antes. |
| **Timeout o tarea demasiado pesada** | Si la tarea supera el límite de tiempo o consume demasiados recursos, puede fallar silenciosamente. En ese caso, dividí la tarea en partes más pequeñas (por ejemplo, primero explorar, luego proponer, luego especificar, etc.). |
| **Resultado perdido por compaction** | Si la delegación terminó pero no viste la notificación, usá: <br>`delegation_read(<id>)` <br>donde `<id>` lo obtuviste con `delegation_list`. Así recuperás el output incluso si la notificación se borró por compaction. |
| **Esperando respuesta inmediata (usando `task` en vez de `delegate`)** | `task` es sincrónico y bloquea hasta que termine; `delegate` es asíncrono y sigue trabajando en segundo plano. Si usaste `task` y esperabas que la consola te devuelva algo al instante, quizás el agente todavía esté corriendo. Esperá la notificación o, si realmente necesitás el resultado antes de continuar, usá `task` (pero solo cuando sea estrictamente necesario). |

---

## ✅ Cómo delegar correctamente (paso a paso)

1. **Elegí el agente adecuado**  
   - Para preguntas generales, búsquedas o operaciones simples → `general`.  
   - Para explorar el código rápidamente (buscar archivos, patrones, etc.) → `explore` (con nivel `quick`, `medium` o `very thorough`).  
   - Para cualquier fase de SDD → usar el agente específico (`sdd-design`, `sdd-tasks`, etc.).

2. **Escribí un prompt claro y accionable**  
   - Incluí qué querés que haga, qué archivo o ruta tocar, y qué formato de salida esperás (si lo necesitás).  
   - Ejemplo:  
     ```
     /delegate {
       "prompt": "Buscá todos los archivos .tsx bajo src/components que contengan la palabra 'Button' y devolvé una lista con sus rutas completas.",
       "agent": "explore",
       "thoroughness": "medium"
     }
     ```

3. **(Opcional) Forzar carga de skills**  
   Si sabés que el agente va a necesitar una skill específica, añadíla al prompt:  
   ```
   "prompt": "SKILL: Load /C:/Users/DELL/.claude/skills/react-19/SKILL.md\nCreá un componente React llamado Button.tsx..."
   ```

4. **Ejecutá la delegación**  
   - Desde la línea de comandos (o la barra de chat):  
     ```
     delegate --prompt "Tu prompt aquí" --agent general
     ```  
   - O usando el atajo `/delegate { … }` si tu interfaz lo soporta.

5. **No hagas polling**  
   - Esperá la notificación `<task-notification>`. Cuando llegue, podés leer el resultado con:  
     `delegation_read(<id-de-la-notificacion>)`.

6. **Si no ves la notificación**  
   - Corriste `delegation_list()` y buscás el ID de la delegación que creaste.  
   - Luego `delegation_read(<id>)` para obtener el output.

---

## 📋 Próximos pasos para vos

1. **Fijate si tenés alguna delegación pendiente** con:  
   ```
   delegation_list()
   ```  
   Copiá el ID de aquella que creíste que no terminó y ejecutá:  
   ```
   delegation_read(<ID>)
   ```  
   Así vemos si realmente produjo output o si falló por alguno de los motivos de arriba.

2. **Probá una delegación de prueba** ahora mismo, por ejemplo:  
   ```
   /delegate {
     "prompt": "Listá los archivos .md en la raíz del repositorio.",
     "agent": "general"
   }
   ```  
   Cuando llegue la notificación, compartime el output y vemos que todo está ok.

3. **Si querés delegar algo específico de tu proyecto** (por ejemplo, crear un nuevo endpoint en Django, escribir un test, etc.), decíme exactamente qué necesitás y yo te armo el prompt con las skills correctas.

---

### Resumen rápido

- La delegación **funciona** (lo vimos con el listado de archivos).  
- Los fallos suelen venir de: nombre de agente equivocado, prompt poco claro, falta de skills, o simplemente no esperar la notificación.  
- Seguí los pasos de arriba y tus tareas se van a completar sin problemas.  
