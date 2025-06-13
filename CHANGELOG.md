# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2024-06-10

### Added
- Initial project structure with `uv`, `ruff`, and `pre-commit`.
- Basic FastAPI application with a `"/"` health check endpoint.
- First test for the health check endpoint using `pytest` and `httpx`.
- Initial `README.md` with setup instructions.
- Jinja2 for HTML templating.
- Base template with HTMX included and an index page.
- Root endpoint now serves an HTML response.

### Changed
- Updated root endpoint test to check for HTML content.