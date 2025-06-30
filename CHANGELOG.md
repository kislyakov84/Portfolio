# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-06-10
## [0.2.0] - 2025-06-29

### Added
- Initial project structure with `uv`, `ruff`, and `pre-commit`.
- Basic FastAPI application with a `"/"` health check endpoint.
- First test for the health check endpoint using `pytest` and `httpx`.
- Initial `README.md` with setup instructions.
- Jinja2 for HTML templating.
- Base template with HTMX included and an index page.
- Root endpoint now serves an HTML response.
- Docker Compose setup for PostgreSQL.
- SQLAlchemy and `psycopg` for asynchronous database access.
- Pydantic-based settings management.
- Initial `Project` model for portfolio items.
- Repository pattern for data access (`project_repository`).
- Dependency injection for DB sessions (`get_db`).
- `on_startup` event to create DB tables and seed initial data.
- Environment-based configuration with `.env` file for database connection.
- Pydantic schemas for project creation (`ProjectCreate`) and reading (`ProjectRead`).
- API endpoint (`POST /projects/`) to create new projects.
- An HTML form on the main page to add new projects.
- Used HTMX to submit the form asynchronously, adding new projects to the list without a page reload.
- Implemented form data parsing in FastAPI using `Form()` and `python-multipart`.
- Added a small UX improvement: the form now resets after successful submission.
- Basic admin page (`/admin`) to display a list of all projects with edit/delete placeholders.

### Changed
- Updated root endpoint test to check for HTML content.
- Main page now dynamically displays a list of projects from the PostgreSQL database.
- Reworked `index.html` to be a dynamic template with project cards.
- Refactored the project card into a reusable partial template (`partials/project_card.html`).
- The list of projects is now wrapped in a `<div id="project-list">` to serve as a target for HTMX.
- Updated `create_project` endpoint to manually parse form data and validate it with a Pydantic model for better robustness.

### Fixed
- Resolved complex database connection issues related to Docker port conflicts and environment variable loading.