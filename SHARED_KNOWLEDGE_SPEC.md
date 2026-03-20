# Shared Knowledge System Specification

## 1. Introduction

This specification defines the requirements for a shared knowledge system that enables teams to share Engram-like memories (decisions, bug fixes, patterns, discoveries) across machines and team members. The system is designed to complement the existing Engram private memory system by providing a file-based, shareable knowledge repository.

## 2. Glossary

- **Observation**: A single unit of knowledge (decision, bug fix, pattern, etc.) stored in the shared system
- **Engram**: The existing private memory system stored in `~/.gemini/antigravity/`
- **Shared Knowledge Repository**: The file-based directory structure where observations are stored for sharing
- **Scope**: Whether knowledge is project-scoped or personal-scoped
- **Type**: Category of observation (decision, bugfix, pattern, discovery, config, preference)

## 3. Functional Requirements

### 3.1 Knowledge Storage
The system SHALL allow users to save observations to the shared knowledge repository with the following metadata:
- Unique identifier (timestamp-based or UUID)
- Title (short, searchable phrase)
- Type (decision | bugfix | pattern | discovery | config | preference)
- Scope (project | personal)
- Project name (when scope is project)
- Timestamp (ISO 8601 format)
- Tags (array of strings for flexible categorization)
- Content in structured format:
  ```
  **What**: [concise description]
  **Why**: [reasoning or motivation]
  **Where**: [affected files/paths]
  **Learned**: [gotchas, decisions, surprises]
  ```

### 3.2 Knowledge Retrieval
The system SHALL support:
- Retrieving a specific observation by its ID
- Searching observations by:
  - Free-text search across title and content
  - Filtering by type
  - Filtering by scope
  - Filtering by project name
  - Filtering by tags
- Returning observations in their complete structured format

### 3.3 Knowledge Organization
The system SHALL organize observations in the following directory structure:
```
<shared-repo-root>/
├── projects/
│   └── <project-name>/
│       ├── observations/
│       │   ├── <observation-id>.yaml
│       │   └── ...
│       ├── metadata/
│       │   └── project-info.yaml
│       └── index/  # Optional for performance
│           ├── tags.json
│           └── recent.json
└── personal/  # For personal-scoped observations if implemented
```

### 3.4 Interoperability
The system SHALL:
- Use YAML format for observation files (human-readable, diff-friendly)
- Preserve the exact structure of Engram's content format (What, Why, Where, Learned)
- Not modify or depend on the existing Engram system
- Work alongside any file synchronization system (Git, Dropbox, Google Drive, etc.)

## 4. Non-Functional Requirements

### 4.1 Usability
- Adding an observation SHALL take less than 2 minutes for familiar users
- Searching SHALL return results in <5 seconds for repositories with <10,000 observations
- File format SHALL be readable and editable with any text editor
- Directory structure SHALL be intuitive for new team members

### 4.2 Reliability
- Observations SHALL be stored atomically to prevent corruption
- The system SHALL handle concurrent access from multiple synchronization clients
- Invalid YAML SHALL be detected and reported clearly

### 4.3 Portability
- The entire knowledge repository SHALL be copyable via standard file operations
- No proprietary database or binary format SHALL be required
- The system SHALL work on Windows, macOS, and Linux

### 4.4 Safety
- The system SHALL NOT modify existing Engram data
- All operations SHALL be read-only on the existing codebase except for the knowledge repository
- Users SHALL maintain full control over what knowledge is shared

## 5. Scenarios (Use Cases)

### 5.1 New Team Member Onboarding
**As a** new developer joining the videojuego tienda team  
**I want to** quickly understand past architectural decisions  
**So that** I can avoid repeating mistakes and align with team conventions  

**Given** the shared knowledge repository contains architectural decisions  
**When** I search for "FBV CBV decision" or browse project observations  
**Then** I should find the decision about mixed FBV/CBV usage based on complexity  
**And** I should be able to read the What, Why, Where, and Learned sections  
**And** I should understand when to use each approach in my work  

### 5.2 Bug Recurrence Prevention
**As a** developer debugging a shopping cart issue  
**I want to** check if we've solved similar session problems before  
**So that** I can apply proven solutions instead of rediscovering them  

**Given** I encounter a session-related bug in the cart functionality  
**When** I search the shared knowledge for "cart session" or "session cookie"  
**Then** I should find the bugfix for Django 4.2 session domain issue  
**And** I should learn about the SESSION_COOKIE_DOMAIN configuration  
**And** I should see that integration tests were added to prevent regression  

### 5.3 Pattern Reuse
**As a** developer implementing a new feature  
**I want to** discover and reuse existing code patterns  
**So that** I can maintain consistency and reduce development time  

**Given** I need to handle user permissions in multiple views  
**When** I search for "permission mixin" or browse pattern observations  
**Then** I should find the reusable permission mixin pattern  
**And** I should be able to see where it's defined and how to use it  
**And** I should apply it in my new view implementation  

### 5.4 Cross-Machine Work Continuity
**As a** developer switching between workstation and laptop  
**I want to** access the same project knowledge on both machines  
**So that** I don't lose context when changing devices  

**Given** I have made architectural decisions on my workstation  
**When** I switch to my laptop and sync the shared knowledge repository  
**Then** I should be able to search and find all the same observations  
**And** I should see identical content to what was on my workstation  
**And** I should be able to continue working without knowledge gaps  

### 5.5 Team Collaboration via Pull Requests
**As a** team member improving our error handling patterns  
**I want to** propose a new pattern for team review  
**So that** we can maintain quality and consistency in shared knowledge  

**Given** I have discovered a better approach to API error handling  
**When** I save it as an observation in a feature branch of the knowledge repo  
**And** I open a pull request to merge it into main  
**Then** team members should be able to review the observation  
**And** we should discuss its merits before merging  
**And** once merged, it should be available to all team members  

## 6. Acceptance Criteria

The implementation will be considered complete when:

### 6.1 Core Functionality
- [ ] Users can save observations with all required metadata using a simple interface
- [ ] Users can retrieve observations by ID
- [ ] Users can search observations by text, type, scope, project, and tags
- [ ] Search results return complete observations with structured content
- [ ] All data is stored as YAML files in the defined directory structure

### 6.2 Usability
- [ ] Saving an observation takes <2 minutes for users familiar with the format
- [ ] Searching returns results in <5 seconds for repositories <10k observations
- [ ] The directory structure is intuitive and self-documenting
- [ ] Example observations from the videojuego tienda project are included

### 6.3 Compatibility & Safety
- [ ] The system does not modify existing Engram data or configuration
- [ ] Observations use the exact same structured format as Engram (What, Why, Where, Learned)
- [ ] The system works alongside Git, Dropbox, Google Drive, etc. without interference
- [ ] No external dependencies beyond standard file operations are required

### 6.3 Videojuego Tienda Specific
- [ ] At least 3 architectural decisions from the videojuego tienda project are documented as examples
- [ ] At least 2 bugfixes from the project's history are included as examples
- [ ] The examples demonstrate clear value for team productivity
- [ ] The specification references actual files and paths from the videojuego tienda codebase

### 6.4 Quality
- [ ] All YAML files are valid and parseable
- [ ] Examples follow the structured content format precisely
- [ ] Tags and categorization are consistent and useful
- [ ] Timestamps are in proper ISO 8601 format
- [ ] Project and scope fields are correctly set

## 7. Interface Definition (for shared-knowledge skill)

The system will be implemented as an Opencode skill named `shared-knowledge` with the following operations:

### 7.1 shared_mem_save
**Purpose**: Save an observation to the shared knowledge repository  
**Parameters**:
- `title`: string (required)
- `type`: one of ["decision", "bugfix", "pattern", "discovery", "config", "preference"] (required)
- `content`: string in structured format (required)
- `project`: string (required when scope is "project")
- `scope`: "project" or "personal" (default: "project")
- `tags`: array of strings (optional)
**Returns**: observation ID on success

### 7.2 shared_mem_get_observation
**Purpose**: Retrieve a specific observation by ID  
**Parameters**:
- `id`: string (required)
**Returns**: complete observation object or error if not found

### 7.3 shared_mem_search
**Purpose**: Search observations with flexible filtering  
**Parameters**:
- `query`: string for free-text search (optional)
- `type`: filter by observation type (optional)
- `scope`: filter by scope (optional)
- `project`: filter by project name (optional)
- `tags`: array of strings to match (optional)
- `limit`: maximum results to return (default: 10)
**Returns**: array of observation summaries matching criteria

### 7.4 shared_mem_list_recent
**Purpose**: List recently added observations  
**Parameters**:
- `limit`: number of observations to return (default: 5)
**Returns**: array of recent observation summaries

## 8. Open Questions & Decisions Needed

### 8.1 Observation ID Strategy
- Option A: Timestamp-based (e.g., `20260320-001-decision-views-architecture`) - simple, sortable
- Option B: UUID (e.g., `550e8400-e29b-41d4-a716-446655440000`) - guaranteed unique
- Recommendation: Timestamp-based with sequential counter for same-second collisions

### 8.2 Indexing for Large Repositories
- For now: linear search through YAML files (acceptable for <10k observations)
- Future consideration: optional search index if performance becomes issue
- Decision: Implement linear search first, add indexing only if needed

### 8.3 Synchronization Mechanism
- The system will NOT implement its own sync; will rely on external tools
- Recommendation: Document Git as preferred method for teams
- Provide example `.gitignore` for knowledge repo if needed

### 8.4 Personal Scope Implementation
- Personal observations stored in `personal/` directory
- May omit project field or set to null
- Low priority feature; can be added later based on demand

## 9. References & Related Resources

- Existing Engram system documentation (in AGENTS.md)
- SDD openspec backend mechanism (file-based artifact storage)
- YAML 1.2 specification
- Conventional Commits format (for inspiration on structured metadata)
- Git best practices for documentation storage

## 10. Conclusion

This specification defines a shared knowledge system that safely complements Engram by providing a file-based, shareable repository for team knowledge. By focusing on simplicity, compatibility, and usability, it addresses the core need for knowledge persistence across machines and collaboration within teams without introducing unnecessary complexity or risk.

The system leverages proven patterns (structured knowledge storage, file-based repositories) and adapts them to the specific needs of development teams working on projects like the videojuego tienda. Implementation as an Opencode skill will make it easily discoverable and usable within the existing agent workflow.

Next steps: Proceed to sdd-design phase to create the technical design document based on this specification.