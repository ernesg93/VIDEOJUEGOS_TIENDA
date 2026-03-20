# Shared Knowledge System Technical Design

## 1. Introduction

This document describes the technical design for the `shared-knowledge` skill, which implements a file-based shared knowledge system to complement Engram's private memory. The design is based on the specification in SHARED_KNOWLEDGE_SPEC.md.

## 2. System Architecture

### 2.1 High-Level Components
```
Shared Knowledge System
├── Skill Interface (shared-knowledge skill)
│   ├── shared_mem_save()
│   ├── shared_mem_get_observation()
│   ├── shared_mem_search()
│   └── shared_mem_list_recent()
├── Storage Layer
│   ├── Observation Serializer (YAML)
│   ├── File System Manager
│   └── Search Engine (Linear + Optional Index)
└── Configuration
    └── Knowledge Repository Location
```

### 2.2 Data Flow
1. **Save Operation**: 
   - User calls `shared_mem_save()` with observation data
   - Skill validates input and assigns ID/timestamp if needed
   - Storage layer serializes to YAML and writes to appropriate file
   - Confirmation returned to user

2. **Search Operation**:
   - User calls `shared_mem_search()` with filters
   - Skill translates parameters to storage layer query
   - Storage layer scans relevant files and applies filters
   - Matching observations returned as summaries

3. **Get Operation**:
   - User calls `shared_mem_get_observation()` with ID
   - Storage layer locates and reads specific YAML file
   - Content deserialized and returned to user

### 2.3 Integration Points
- **Opencode Agent System**: Called as a skill via standard skill invocation mechanism
- **File System**: Reads/writes YAML files in shared repository
- **External Sync**: Designed to work with Git/Dropbox/etc. (no direct integration)
- **Existing Codebase**: Zero modification required; purely additive

## 3. Detailed Design

### 3.1 Observation Data Model

An observation consists of:
```yaml
id: <string>                    # Unique identifier (timestamp-based)
title: <string>                 # Short, searchable title
type: <string>                  # decision|bugfix|pattern|discovery|config|preference
scope: <string>                 # project|personal
project: <string|null>          # Project name (null for personal scope)
timestamp: <string>             # ISO 8601 UTC timestamp
tags: <string[]>                # Array of tag strings for categorization
content: <string>               # Structured content with What/Why/Where/Learned
```

### 3.2 Content Format Specification
The `content` field MUST follow this exact structure:
```
**What**: [One sentence describing what was decided/done/learned]
**Why**: [Reasoning, motivation, or problem that caused this]
**Where**: [Files, paths, or components affected]
**Learned**: [Gotchas, specific decisions, surprises - omit if none]
```

### 3.3 Directory Structure
```
<knowledge-repo-root>/          # Configurable location
├── projects/
│   └── <project-name>/         # e.g., VIDEOJUEGOS_TIENDA
│       ├── observations/
│       │   ├── 20260320-001-decision-views-architecture.yaml
│       │   ├── 20260320-002-bugfix-cart-session.yaml
│       │   └── ...             # One file per observation
│       ├── metadata/
│       │   └── project-info.yaml  # Optional: project description, etc.
│       └── index/              # Optional performance indexes
│           ├── tags.json       # Tag frequency for autocomplete
│           └── recent.json     # Recently modified observation IDs
└── personal/                   # For personal-scoped observations
    └── [same structure as projects/]
```

### 3.4 File Naming Convention
Observation files use: `<timestamp>-<sequence>-<type>-<slug>.yaml`
- `timestamp`: YYYYMMDD-HHMMSS (UTC)
- `sequence`: 3-digit counter for same-second collisions (001, 002, etc.)
- `type`: observation type abbreviation (dec, bug, pat, disc, cfg, pref)
- `slug`: URL-friendly version of title (lowercase, hyphens, no special chars)

Example: `20260320-001-dec-views-architecture.yaml`

### 3.5 Algorithms

#### Save Operation (`shared_mem_save`)
```
1. Validate required parameters (title, type, content, project if scope=project)
2. Normalize type to lowercase and validate against allowed values
3. Set scope to "project" if not provided (default)
4. Generate observation ID:
   a. Get current UTC timestamp as YYYYMMDD-HHMMSS
   b. Check if file with this timestamp exists in target directory
   c. If exists, increment sequence counter; else start at 001
   d. Create slug from title (lowercase, alphanumeric + hyphens)
   e. Format: {timestamp}-{sequence:03d}-{type_abbr}-{slug}.yaml
5. Construct observation object with all metadata
6. Serialize to YAML with content block preserved literally
7. Write to file at: <repo>/projects/<project>/observations/{filename}.yaml
8. Return observation ID to caller
```

#### Search Operation (`shared_mem_search`)
```
1. Determine search scope based on parameters:
   - If project specified: search only that project's observations
   - Else if scope=personal: search personal directory
   - Else: search all projects (could be made configurable)
2. Collect candidate files:
   - For each target directory, gather all .yaml files in observations/
3. For each candidate file:
   a. Parse YAML front matter (id, title, type, scope, project, timestamp, tags)
   b. Load content field
   c. Apply filters in order:
      - Text search: if query provided, check if in title OR content
      - Type filter: if provided, must match observation type
      - Scope filter: if provided, must match observation scope
      - Project filter: if provided, must match project name
      - Tags filter: if provided, ALL tags must be present in observation tags
   d. If all filters pass, create summary object:
      { id, title, type, scope, project, timestamp, tags, snippet }
      where snippet is first 150 chars of content with search terms highlighted
4. Sort results by timestamp descending (newest first)
5. Apply limit parameter
6. Return results array
```

#### Get Operation (`shared_mem_get_observation`)
```
1. Validate ID format (basic sanity check)
2. Determine likely location:
   - If project scope known from ID pattern or config, go direct
   - Else search all projects/personal for matching ID
3. Attempt to read and parse YAML file at expected path
4. If not found in expected location, fall back to full search (less efficient)
5. If found, return complete observation object
6. If not found anywhere, return "observation not found" error
```

### 3.6 Error Handling
- **Validation Errors**: Return clear messages about missing/invalid parameters
- **File Not Found**: Distinguish between "observation not found" vs "repository not accessible"
- **YAML Parse Error**: Indicate corrupted observation file with file path
- **Permission Errors**: Report inability to read/write to repository location
- **All errors** include actionable suggestions where possible

### 3.7 Performance Characteristics
- **Save**: O(1) - single file write
- **Search**: O(n) where n = number of observation files in search scope
  - Acceptable for <10,000 files (~500ms on modern SSD)
  - For larger repos: optional index implementation (phase 2)
- **Get**: O(1) with direct path lookup, O(n) with fallback search
- **Memory**: Constant - only loads one observation at a time during search/get

### 3.8 Configuration
The skill will use:
1. **Primary Configuration**: Environment variable `SHARED_KNOWLEDGE_REPO` 
   - Default: `./shared-knowledge` relative to current working directory
   - Must be an absolute or relative path string
2. **Fallback**: If env var not set, use default location
3. **Validation**: On first use, check if directory exists and is writable
   - Create if doesn't exist (with appropriate permissions)
   - Fail with clear message if not writable

### 3.9 Security Considerations
- **Path Safety**: All file operations use sanitized paths; no path injection possible
- **File Permissions**: Created files get default umask (typically 644)
- **Content Safety**: No execution of content; pure storage/retrieval
- **Privacy**: Does not access or transmit data outside file operations
- **Conflict Resolution**: Relies on external sync tools (Git) for handling concurrent edits

## 4. Implementation Approach

### 4.1 Skill Structure
The `shared-knowledge` skill will consist of:
```
shared-knowledge/
├── SKILL.md                  # This skill's documentation
├── shared_knowledge.py       # Main implementation
├── templates/
│   ├── observation.yaml.j2   # Jinja2 template for new observations
│   └── project-info.yaml.j2  # Template for project metadata
└── utils/
    ├── yaml_handler.py       # YAML serialization/deserialization
    ├── file_manager.py       # Safe file operations
    └── search_engine.py      # Search and filtering logic
```

### 4.2 Development Phases

#### Phase 1: Core Functionality (MVP)
- Implement basic save/get/search operations
- Linear search through YAML files
- Timestamp-based ID generation
- Structured content format enforcement
- Default repository location (`./shared-knowledge`)
- Comprehensive error handling and logging

#### Phase 2: Usability Enhancements
- Add `shared_mem_list_recent()` operation
- Implement slug generation from titles
- Add optional project metadata tracking
- Improve search snippets with context highlighting
- Add validation for content format structure

#### Phase 3: Performance Optimizations (Optional)
- Implement optional search index for tags/types
- Add caching of file metadata for large repositories
- Implement batch operations for bulk imports/exports
- Add repository maintenance tools (integrity checks, etc.)

### 4.3 Dependencies
- **Python Standard Library Only**: 
  - `yaml` (PyYAML may be bundled or use built-in if available)
  - `json`, `os`, `pathlib`, `datetime`, `re`
- **No External Dependencies**: Designed to work in vanilla Opencode environment
- **Optional**: Jinja2 for templates (can use string formatting instead)

### 4.4 Testing Strategy
- **Unit Tests**: 
  - YAML serialization/deserialization
  - ID generation logic
  - Search filter combinations
  - File path safety
- **Integration Tests**:
  - End-to-end save/search/get cycles
  - Concurrent access simulation
  - Repository migration scenarios
- **Manual Tests**:
  - Real-world usage scenarios from spec
  - Performance validation with growing repository
  - Cross-platform validation (Windows/macOS/Linux)

## 5. Interface Definition (for Opencode Agent)

The skill will be invoked through the standard Opencode skill mechanism. When loaded, it will provide these operations:

### 5.1 shared_mem_save
**Description**: Save a knowledge observation to the shared repository  
**Invocation**: 
```
/shared-knowledge save --title "Decision: use FBVs for simple forms" 
                      --type decision 
                      --content "**What**: ...\n**Why**: ...\n**Where**: ...\n**Learned**: ..." 
                      --project VIDEOJUEGOS_TIENDA
```
**Returns**: 
```json
{
  "status": "success",
  "observation_id": "20260320-001-dec-simple-forms",
  "message": "Observation saved successfully"
}
```

### 5.2 shared_mem_get_observation
**Description**: Retrieve a specific observation by its ID  
**Invocation**:
```
/shared-knowledge get --id 20260320-001-dec-simple-forms
```
**Returns**:
```json
{
  "status": "success",
  "observation": {
    "id": "20260320-001-dec-simple-forms",
    "title": "Decision: use FBVs for simple forms",
    "type": "decision",
    "scope": "project",
    "project": "VIDEOJUEGOS_TIENDA",
    "timestamp": "2026-03-20T10:30:00Z",
    "tags": ["django", "views", "fbv"],
    "content": "**What**: ...\n**Why**: ...\n**Where**: ...\n**Learned**: ..."
  }
}
```

### 5.3 shared_mem_search
**Description**: Search observations with flexible filtering  
**Invocation**:
```
/shared-knowledge search --query "session cookie" 
                        --type bugfix 
                        --project VIDEOJUEGOS_TIENDA
```
**Returns**:
```json
{
  "status": "success",
  "results": [
    {
      "id": "20260320-002-bugfix-cart-session",
      "title": "Bugfix: Sesiones de carrito se pierden al actualizar Django",
      "type": "bugfix",
      "scope": "project",
      "project": "VIDEOJUEGOS_TIENDA",
      "timestamp": "2026-03-20T14:15:00Z",
      "tags": ["django", "sessions", "cart", "middleware"],
      "snippet": "...al actualizar Django de 4.1 a 4.2\n\n**Why**: Los usuarios reportaban que sus carritos se vaciaban..."
    }
  ],
  "count": 1,
  "query_info": {
    "query": "session cookie",
    "type": "bugfix",
    "project": "VIDEOJUEGOS_TIENDA",
    "scope": null
  }
}
```

### 5.4 shared_mem_list_recent
**Description**: List recently added observations  
**Invocation**:
```
/shared-knowledge list-recent --limit 5
```
**Returns**: Array of observation summaries sorted by timestamp descending

## 6. Deployment and Usage

### 6.1 Installation
The skill will be installed via Opencode's standard skill installation mechanism:
```
/skill install shared-knowledge
```
Or manually copied to `~/.config/opencode/skills/shared-knowledge/`

### 6.2 First-Time Setup
On first use, the skill will:
1. Check for `SHARED_KNOWLEDGE_REPO` environment variable
2. If not set, use default `./shared-knowledge` in current directory
3. Verify directory exists and is writable
4. Create directory structure if needed:
   ```
   ./shared-knowledge/
   └── projects/
   ```
5. Optionally create example observations from the videojuego tienda project

### 6.3 Team Usage Recommendations
For development teams using this system:

#### With Git (Recommended for Teams):
1. Initialize knowledge repo as Git repository:
   ```bash
   cd shared-knowledge
   git init
   ```
2. Create `.gitignore`:
   ```
   # Ignore temporary files
   *.tmp
   .DS_Store
   Thumbs.db
   ```
3. Team members clone/pull the repository
4. To contribute knowledge:
   ```bash
   # Make changes (via skill or manual edits)
   git add observations/
   git commit -m "Add decision about FBV/CBV usage"
   git push origin main
   ```
5. To update from team:
   ```bash
   git pull origin main
   ```

#### With File Sync Services (Dropbox, Google Drive, etc.):
1. Place `shared-knowledge` directory in synced folder
2. Ensure all team members have access to the same folder
3. The service handles synchronization automatically
4. Recommend making changes infrequently to avoid conflicts
5. If conflict occurs, manual resolution of YAML files is straightforward

### 6.4 Migration and Backup
- **Backup**: Copy entire `shared-knowledge` directory
- **Migration**: Copy directory to new location and update `SHARED_KNOWLEDGE_REPO` if needed
- **Versioning**: Handled by external system (Git) or manual copies
- **Export/Import**: Individual observations can be copied as YAML files

## 7. Diagram: Component Interaction

```
User/Agent
    │
    ▼
[Opencode Skill Invoker]
    │
    ▼
Shared-Knowledge Skill
    │
    ┌─────────────────────────────────────┐
    ▼                                     ▼
[Operation Router]              [Configuration Manager]
    │                                     │
    ▼                                     ▼
┌─────────┐  ┌─────────┐  ┌─────────┐      ▼
│  Save   │  │  Get    │  │ Search  │  [Repo Location]
└─────────┘  └─────────┘  └─────────┘      │
    │         │         │                  ▼
    ▼         ▼         ▼            [File System]
┌─────────┐  ┌─────────┐  ┌─────────┘      │
│Serializer│ │Deserializer│ │Filter Engine│
└─────────┘  └─────────┘  └─────────┘      │
    │         │         │                  ▼
    └─────────┴─────────┴──────────────→ [YAML Files]
                                                    │
                                                    ▼
                                        [External Sync: Git/Dropbox/etc.]
                                                    │
                                                    ▼
                                        [Other Team Members/Machines]
```

## 8. Conclusion

This technical design provides a solid foundation for implementing the `shared-knowledge` skill. The approach leverages file-based storage (similar to SDD's openspec backend) to create a shareable knowledge system that complements Engram's private memory.

Key strengths of this design:
- **Simplicity**: Uses plain YAML files and standard file operations
- **Compatibility**: Works with existing synchronization tools (Git, Dropbox, etc.)
- **Safety**: Zero modification to existing codebase or Engram system
- **Usability**: Structured format matches Engram, making knowledge easily consumable
- **Performance**: Adequate for team-sized repositories with potential for optimization
- **Flexibility**: Works for both individual developers and teams

The design adheres to all principles outlined in the AGENTS.md documentation:
- Concepts over implementation details (focus on knowledge sharing pattern)
- AI as a tool (agent directs, skill executes)
- Solid foundations (builds on existing file-based storage paradigms)
- Against immediacy (provides sustainable team knowledge asset)

Next steps: Proceed to the `sdd-tasks` phase to break this design into actionable implementation tasks.