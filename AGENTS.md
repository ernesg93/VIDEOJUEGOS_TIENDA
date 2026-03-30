# Code Review Rules - Tienda Videojuegos

## Python / Django

### Style
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters
- Use snake_case for variables, functions, and methods
- Use PascalCase for class names
- Use UPPER_SNAKE_CASE for constants

### Imports
Order imports as follows (per PEP 8):
1. Standard library
2. Third-party libraries
3. Local application

### Django Models
- Define `__str__` method for all models
- Use explicit `max_length` for CharField
- Add `verbose_name` and `help_text` for user-facing fields
- Use choices with constants for enum-like fields
- Include `Meta` class with `verbose_name`, `verbose_name_plural`, and `ordering`
- Add `created_at` and `updated_at` timestamp fields for auditing
- Use `blank=True` for optional fields, `default` values where appropriate
- Implement custom `save()` methods when needed (e.g., slug generation)
- Use `slugify()` from `django.utils.text` for URL-friendly slugs

### Django Admin
- Use `@admin.register()` decorator for model registration
- Define `list_display` for important fields in list view
- Add `list_filter` for filterable fields (status, dates, categories)
- Include `search_fields` for searchable text fields
- Use `prepopulated_fields` for slug fields
- Add `list_editable` for fields that can be edited inline
- Set appropriate `ordering` for default sort

### Views
- Use function-based views for simple operations
- Use class-based views (CBVs) for complex CRUD operations
- Always return proper HTTP responses
- Handle exceptions appropriately
- Add docstrings explaining view purpose, args, and returns
- Filter querysets appropriately (e.g., `activo=True` for public views)

### Templates
- Store templates in `templates/<app_name>/` structure
- Use template inheritance (base.html)
- Load static files properly with `{% load static %}`

### Testing
- Write tests for all views and models
- Use Django's TestCase
- Follow naming convention: `test_<method_name>_<scenario>`

### Security
- Never hardcode secrets (use environment variables)
- Use Django's CSRF protection
- Validate all user input
- Escape output in templates ({{ var }} handles this automatically)

## HTML / Templates

- Use semantic HTML5 elements
- Include proper meta tags for responsive design
- Use Bootstrap utility classes when possible
- Keep templates DRY (Don't Repeat Yourself)

## CSS

- Use CSS variables for colors and spacing
- Mobile-first responsive design
- Use Bootstrap as base framework
- Add custom styles in style.css for project-specific design

## JavaScript

- Keep JavaScript minimal (use Bootstrap JS when possible)
- Use vanilla JavaScript or Bootstrap's built-in components
- Include proper error handling
