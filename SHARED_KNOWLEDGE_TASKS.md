# Shared Knowledge System Implementation Tasks

This document breaks down the shared knowledge system design into actionable implementation tasks for the `shared-knowledge` skill.

## Phase 1: Core Functionality (MVP)

### Task 1: Project Setup and Skill Structure
- [ ] Create skill directory: `~/.config/opencode/skills/shared-knowledge/`
- [ ] Create basic skill structure:
  - `SKILL.md` (skill documentation)
  - `shared_knowledge.py` (main implementation)
  - `README.md` (usage instructions)
- [ ] Define skill metadata in SKILL.md:
  - Name: shared-knowledge
  - Description: "Share Engram-like knowledge observations between users and machines"
  - Trigger: When user wants to share or access team knowledge
  - Version: 0.1.0

### Task 2: Configuration and Repository Management
- [ ] Implement configuration loading:
  - Read `SHARED_KNOWLEDGE_REPO` environment variable
  - Default to `./shared-knowledge` if not set
  - Validate path is accessible/writable
- [ ] Implement repository initialization:
  - Create directory structure if missing:
    - `<repo>/projects/`
    - `<repo>/personal/` (optional for future)
  - Create `.gitkeep` files to preserve empty directories in Git
- [ ] Add helper functions for path construction:
  - `get_observations_dir(project_name, scope)`
  - `get_project_metadata_dir(project_name)`
  - Validate project names for filesystem safety

### Task 3: Observation Data Model and Serialization
- [ ] Define Observation data class/structure:
  - id: str
  - title: str
  - type: str (validated against allowed types)
  - scope: str ("project" or "personal")
  - project: str or None
  - timestamp: datetime (UTC)
  - tags: List[str]
  - content: str
- [ ] Implement YAML serialization:
  - Convert Observation to YAML string
  - Preserve content block literal format (using | or >-)
  - Include all metadata fields
- [ ] Implement YAML deserialization:
  - Parse YAML to Observation object
  - Validate required fields
  - Convert timestamp string to datetime object
  - Handle missing optional fields gracefully

### Task 4: Core Save Operation (`shared_mem_save`)
- [ ] Implement parameter validation:
  - title: required, non-empty string
  - type: required, must be in ["decision", "bugfix", "pattern", "discovery", "config", "preference"]
  - content: required, non-empty string
  - project: required when scope="project"
  - scope: optional, defaults to "project"
  - tags: optional, defaults to empty list
- [ ] Implement ID generation:
  - Generate timestamp: YYYYMMDD-HHMMSS (UTC)
  - Check for existing files with same timestamp
  - Increment sequence counter (001, 002, etc.) for collisions
  - Generate slug from title:
    - Convert to lowercase
    - Replace non-alphanumeric with hyphens
    - Remove leading/trailing/h multiple hyphens
    - Limit length (e.g., 50 chars)
  - Format: `{timestamp}-{sequence:03d}-{type_abbr}-{slug}.yaml`
    - Type abbreviations: dec, bug, pat, disc, cfg, pref
- [ ] Implement file writing:
  - Construct full file path
  - Serialize observation to YAML
  - Write file atomically (write to temp, then rename)
  - Return observation ID on success

### Task 5: Core Get Operation (`shared_mem_get_observation`)
- [ ] Implement ID-based lookup:
  - Accept observation ID parameter
  - Validate ID format (basic sanity check)
  - Determine likely file location:
    - If project known from ID or config, construct direct path
    - Else, prepare to search all locations
  - Attempt to read and parse YAML file
  - If not found in expected location, fall back to search
  - Return complete observation object or error
- [ ] Implement error handling:
  - Clear "observation not found" message
  - Distinguish between ID format errors and missing observations
  - Handle YAML parse errors (corrupted file)

### Task 6: Core Search Operation (`shared_mem_search`)
- [ ] Implement search scope determination:
  - If project specified: limit to that project's observations
  - Else if scope specified: limit to that scope
  - Else: search all projects (configurable behavior)
- [ ] Implement file discovery:
  - Recursively find all .yaml files in observations/ directories
  - Skip metadata/ and index/ directories
- [ ] Implement filtering logic:
  - Text search: case-insensitive match in title OR content
  - Type filter: exact match on observation type
  - Scope filter: exact match on scope
  - Project filter: exact match on project name
  - Tags filter: ALL specified tags must be present in observation tags
- [ ] Implement result formatting:
  - For each match, create summary object:
    - id, title, type, scope, project, timestamp, tags
    - snippet: first 200 chars of content with search terms highlighted (optional)
  - Sort by timestamp descending (newest first)
  - Apply limit parameter
  - Return results array

### Task 7: Error Handling and Logging
- [ ] Implement consistent error responses:
  - Validation errors: clear messages about what's wrong
  - Not found errors: distinguish between observation vs repository
  - System errors: permission issues, disk full, etc.
  - All errors include suggested actions when possible
- [ ] Add basic logging:
  - INFO: successful operations
  - WARN: recoverable issues
  - ERROR: failed operations
  - DEBUG: detailed flow information (if enabled)

### Task 8: Basic Documentation and Examples
- [ ] Create comprehensive SKILL.md:
  - Skill description and purpose
  - Installation instructions
  - Usage examples for each operation
  - Configuration options
  - Best practices for teams
- [ ] Create example observations:
  - Based on videojuego tienda project (as explored earlier)
  - Include at least one decision, one bugfix, one pattern
  - Store in skill's `examples/` directory for demonstration
- [ ] Create quick-start guide:
  - How to set up shared repository
  - How to make first knowledge contribution
  - How to search for existing knowledge

## Phase 2: Usability Enhancements

### Task 9: Recent Operations Tracking
- [ ] Implement `shared_mem_list_recent()` operation:
  - Accept limit parameter (default: 5)
  - Return most recent observations across all scopes/projects
  - Sort by timestamp descending
  - Return same summary format as search
- [ ] Consider implementing recent-tracking per project:
  - Optional index file: `<repo>/projects/<project>/index/recent.json`
  - Store last N observation IDs per project
  - Update on each save to that project

### Task 10: Content Format Validation and Assistance
- [ ] Implement content format validation:
  - Check for required sections: **What**, **Why**, **Where**
  - **Learned** is optional
  - Warn if sections missing or malformed
- [ ] Add content template assistance:
  - Provide default template when content is empty:
    ```
    **What**: 
    **Why**: 
    **Where**: 
    **Learned**: 
    ```
  - Optionally validate that sections are filled

### Task 11: Enhanced Search Features
- [ ] Implement search snippet generation:
  - Show content around search matches
  - Highlight matched terms (if output format supports it)
  - Limit snippet length (e.g., 150-200 characters)
- [ ] Add fuzzy/text search improvements:
  - Stemming or basic word matching (optional)
  - Phrase search with quotes (optional)
  - Exclude terms with minus sign (optional)
- [ ] Implement tag-based search improvements:
  - Suggest popular tags during search
  - Allow tag exclusion
  - Show tag frequency in results

### Task 12: Project Metadata Management
- [ ] Implement project info storage:
  - Optional `metadata/project-info.yaml` per project
  - Fields: description, created_by, created_date, tags
  - API to read/update project metadata
- [ ] Implement project listing:
  - Operation to list all projects with observation counts
  - Helpful for discovery in large repositories

## Phase 3: Performance and Advanced Features (Optional)

### Task 13: Search Indexing (For Large Repositories)
- [ ] Implement optional search index:
  - Only activated when repository exceeds threshold (e.g., 1000 observations)
  - Index files: `<repo>/index/tags.json`, `<repo>/index/types.json`
  - Store: term -> list of observation IDs
  - Update index on save/delete operations
  - Use index to speed up tagged/typed searches
- [ ] Implement index maintenance:
  - Rebuild index command (for corruption recovery)
  - Index consistency checking
  - Automatic index enable/disable based on size

### Task 14: Batch Operations
- [ ] Implement import/export functionality:
  - Export: save multiple observations to single YAML/JSON file
  - Import: load observations from file (with deduplication)
  - Useful for backup, migration, or initial population
- [ ] Implement observation cloning:
  - Create copy of existing observation with new ID
  - Useful for templates or variations

### Task 15: Observation Lifecycle Management
- [ ] Implement soft delete/hide functionality:
  - Add `hidden: boolean` field to observations
  - Modify search/get to respect hidden flag
  - Implement `shared_mem_hide_observation()` operation
  - Implement purge/cleanup operations (separate from skill)
- [ ] Implement observation updating:
  - `shared_mem_update_observation()` operation
  - Only allow updating certain fields (title, tags, content)
  - Preserve original ID and timestamp
  - Add `updated_at` field when modified

### Task 16: Advanced Analytics and Reporting
- [ ] Implement statistics gathering:
  - Count observations by type, scope, project
  - Timeline of knowledge contribution
  - Most used tags
  - Contribution frequency by user (if user tracking added)
- [ ] Implement reporting operations:
  - `shared_mem_stats()`: return repository statistics
  - `shared_mem_report()`: generate summary report

## Task Dependencies and Order

### Phase 1 Dependencies:
1. Task 1 → Task 2 → Task 3 → (Task 4, Task 5, Task 6) → Task 7 → Task 8
   - Tasks 4, 5, 6 can be done in parallel after Task 3
   - Task 7 depends on 4, 5, 6
   - Task 8 can start early but should be completed last

### Phase 2 Dependencies:
- Task 9 depends on Task 6 (search infrastructure)
- Task 10 depends on Task 4 (save operation)
- Task 11 depends on Task 6 (search operation)
- Task 12 depends on Task 2 (repository structure)

### Phase 3 Dependencies:
- All Phase 3 tasks depend on completion of Phase 1 core
- Task 13 depends on Task 6 (search) and repository size
- Task 14 depends on Task 4 and Task 5 (save/get)
- Task 15 depends on Task 4, 5, 6
- Task 16 depends on Task 6 (search) and Task 4 (save)

## Estimated Effort (Relative)
- Phase 1 (Core): 60% of total effort
- Phase 2 (Usability): 30% of total effort
- Phase 3 (Advanced): 10% of total effort (optional)

## Definition of Done
A task is considered "Done" when:
- [ ] Implementation is complete and functional
- [ ] Unit tests pass for all new functionality
- [ ] Integration tests verify correct operation
- [ ] Documentation is updated in SKILL.md
- [ ] Example usage is demonstrated (if applicable)
- [ ] Code follows existing style and conventions
- [ ] No obvious bugs or edge cases missed

## Next Steps
After completing these tasks, the skill should be ready for:
1. Internal testing and dogfooding
2. Sharing with early adopters for feedback
3. Iteration based on real-world usage
4. Potential progression to sdd-verify and sdd-apply phases if adopted as a formal change

The tasks above provide a clear path from concept to usable skill while allowing for incremental value delivery.