# Checklist: Odoo Frontend, Website, and OWL Component QA Checklist

## Purpose
This checklist guides an AI agent through the review and validation of Odoo website, QWeb, and OWL component development (Odoo 17/18), ensuring frontend code quality, maintainability, and best practices.

## Instructions for AI Agent
When reviewing or generating Odoo frontend code, use the following checks. For each item, evaluate the code/configuration and report compliance or propose improvements. If issues are found, suggest concrete code edits or configuration changes.

## Checklist Items

### 1. OWL Component Development
- [ ] OWL components are defined using ES6+ class syntax and `@odoo-module` directive.
- [ ] Component state is managed with `useState` or equivalent OWL hooks.
- [ ] Props are clearly defined and validated.
- [ ] Component templates are placed in `static/src/xml/` and registered in the module's asset bundle.
- [ ] Event handlers and methods are clearly named and documented.
- [ ] Components are modular, reusable, and follow Odoo/OWL best practices.
- [ ] All user-facing strings are translatable using `_t()`.
- [ ] Unit tests are provided for complex components (if applicable).

### 2. QWeb Template Development
- [ ] QWeb templates use `<template id="..." name="...">` and are placed in `static/src/xml/` or `views/` as appropriate.
- [ ] Templates are registered in the module's asset bundle in `__manifest__.py`.
- [ ] Use `t-field`, `t-out`, `t-esc` appropriately for data display and security.
- [ ] Use `t-if`, `t-foreach`, `t-call`, and other QWeb directives for logic and reusability.
- [ ] All user-facing strings are translatable.
- [ ] Templates are modular and avoid duplication.
- [ ] Template IDs are unique and follow a consistent naming convention.

### 3. Website Page Development
- [ ] Website pages are defined with a QWeb template and a Python controller in `controllers/`.
- [ ] Controllers use `@http.route` with appropriate `auth` and `website=True` settings.
- [ ] Data passed to templates is validated and sanitized.
- [ ] Public routes handle input validation and CSRF protection for forms.
- [ ] Website assets (JS, CSS, images) are placed in `static/` and registered in `__manifest__.py`.
- [ ] Website pages are accessible via menu or links and follow Odoo navigation best practices.

### 4. JavaScript & SCSS
- [ ] JS modules use `@odoo-module` and follow Odoo's ES6+ standards.
- [ ] JS code is modular, well-documented, and avoids global scope pollution.
- [ ] SCSS is organized, uses Odoo/Bootstrap variables and mixins, and is included in the asset bundle.
- [ ] No hardcoded colors, fonts, or styles; use variables and theme mixins.

### 5. Accessibility & Responsiveness
- [ ] Templates and components use semantic HTML and ARIA attributes where appropriate.
- [ ] UI is responsive and works on all device sizes.
- [ ] Forms have proper labels, validation, and error handling.

### 6. Performance & Optimization
- [ ] Avoid inline JS/CSS in templates; use asset bundles.
- [ ] Minimize DOM updates and re-renders in OWL components.
- [ ] Use lazy loading for images and heavy assets where possible.

### 7. Testing
- [ ] Frontend/website/OWL features have automated or manual test cases.
- [ ] Tests cover expected use, edge cases, and failure scenarios.

### 8. Documentation
- [ ] Inline comments explain non-obvious code.
- [ ] Complex logic includes `# Reason:` comments.
- [ ] README or developer docs are updated for new frontend features or components.

## Reference
Refer to Odoo's official frontend, OWL, and website documentation for Odoo 17/18, and the main `PLANNING.md` for project-specific guidelines.

See Odoo-specific frontend, website, and OWL best practices in [Odoo KB](../data/odoo-kb.md). 