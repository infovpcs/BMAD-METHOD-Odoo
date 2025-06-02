# Operational Guidelines (Odoo)

## Coding Standards
- Follow PEP8 and Odoo coding guidelines.
- Use type hints where possible (Python 3.10+).
- Organize code into models, views, controllers, and security as per Odoo module structure.
- Use clear, descriptive names for models, fields, and methods.
- Add docstrings to all functions and classes (Google style).

## ORM Usage
- Always use Odoo ORM methods for data access and manipulation.
- Avoid raw SQL unless absolutely necessary (and document why).
- Use computed fields, related fields, and API decorators (`@api.model`, `@api.depends`, etc.) appropriately.
- Use recordsets and environment (`self.env`) idiomatically.

## Security
- Define access rights in `ir.model.access.csv` and record rules in `security.xml`.
- Restrict access to sensitive models and fields.
- Use Odoo's built-in user groups and permissions system.
- Validate user input and sanitize data in controllers.

## Deployment
- Package modules according to Odoo standards.
- Test installation and upgrade paths.
- Use Odoo's test framework for automated testing.
- Document dependencies and setup steps in `README.md`.
- Use CI/CD pipelines (e.g., GitHub Actions, Odoo.sh) for automated testing and deployment. 