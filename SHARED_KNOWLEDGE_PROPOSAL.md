# Shared Knowledge System Proposal

## Intent
Create a system that allows sharing Engram-like memories (decisions, bug fixes, patterns, discoveries) between users and machines for collaborative work on the videojuego tienda project.

## Scope
- Enable knowledge persistence across machine changes (PC switches, travel)
- Support team collaboration on the same project
- Maintain compatibility with existing Engram system
- Focus on structured knowledge: architectural decisions, bug fixes, code patterns, learned gotchas
- Not intended to replace Engram, but to complement it for sharing purposes

## Approach
Leverage the existing SDD `openspec` backend mechanism as a foundation, adapting it for general knowledge sharing rather than just SDD artifacts. Create a new skill `shared-knowledge` that provides:
- `shared_mem_save()`: Save knowledge observations to a shared file-based repository
- `shared_mem_search()`: Search through shared knowledge
- `shared_mem_get_observation()`: Retrieve full observation details
- Optional synchronization mechanisms (Git-based or manual)

Key design decisions:
1. Use YAML format for observations (human-readable, good for diffs)
2. Structure mirroring Engram: What, Why, Where, Learned + metadata
3. Project-scoped organization within shared repository
4. Optional indexing for search performance
5. Compatible with existing agent system - can be used alongside Engram