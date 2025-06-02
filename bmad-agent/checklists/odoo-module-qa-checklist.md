# Checklist: Odoo Module QA Checklist

## Purpose
This checklist guides an AI agent through the quality assurance process for a new or updated Odoo module (versions 17/18), ensuring it meets functional, technical, and best practice standards.

## Instructions for AI Agent
When performing a QA review of an Odoo module, use the following checks. For each item, evaluate the code/configuration and report compliance or identify areas for improvement. If improvements are needed, propose concrete code edits or configuration changes.

## Checklist Items

### 1. Module Structure & Manifest
- [ ] `__manifest__.py` is correctly formatted with all required fields (`name`, `summary`, `version`, `depends`, `data`, `assets`, `license`).
- [ ] `version` field is incremented appropriately.
- [ ] `depends` lists all necessary module dependencies.
- [ ] `data` lists all XML and CSV files that define views, security, and demo data.
- [ ] `assets` section correctly bundles all frontend (JS, SCSS, OWL/QWeb XML) and backend assets.
- [ ] Standard Odoo module folder structure is followed (`models/`, `views/`, `security/`, `controllers/`, `static/`, `data/`).

### 2. Models (Python)
- [ ] Models follow Odoo ORM best practices (`_name`, `_description`, `_inherit`).
- [ ] Fields are correctly defined with appropriate types, `string`, `help`, `required`, `readonly`, `store`, `compute`, `inverse`, `search` attributes.
- [ ] All methods (API, `compute`, `constrains`, `onchange`) have clear docstrings using Google style.
- [ ] `api.constrains` and `_sql_constraints` are used for data integrity.
- [ ] `ensure_one()` is used when a method expects a single record.
- [ ] No direct SQL queries without `self.env.cr.execute` and proper sanitization.
- [ ] Proper use of `_` for translatable strings.
- [ ] Code adheres to PEP8 guidelines and is formatted with `black`.

### 3. Views (XML)
- [ ] Views are correctly defined with `id`, `name`, `model`, and `arch`.
- [ ] Tree views use `<list>` (Odoo 18+) or `<tree>` (Odoo 17) and include essential fields.
- [ ] Form views include `<sheet>`, `<group>`, `<notebook>`, and chatter (`<chatter/>` for Odoo 18, or `mail_thread` and `mail_activity` widgets for Odoo 17).
- [ ] Search views include relevant fields, filters, and group-by options, leveraging `<searchpanel>` where appropriate.
- [ ] Views use `inherit_id` and `xpath` correctly for extensions.
- [ ] All IDs are unique and follow a consistent naming convention (e.g., `module_name.view_id`).
- [ ] Frontend XML (QWeb) uses `t-field`, `t-out`, `t-esc` appropriately for data display and security.

### 4. Security
- [ ] All new models have corresponding `ir.model.access.csv` entries (read, write, create, unlink).
- [ ] Record rules (`ir.rule`) are defined for multi-company, multi-user, or data segregation needs.
- [ ] Access rights are assigned to groups, not individual users.
- [ ] `sudo()` is used sparingly and only when necessary, with clear justifications.
- [ ] Sensitive operations are protected by security groups.
- [ ] No hardcoded credentials or secrets in code.

### 5. Internationalization (i18n)
- [ ] All user-facing strings in Python, XML, and JS are marked for translation (`_()` in Python, `t-esc` / `t-out` with translation in XML, `_t()` in JS).

### 6. Performance & Scalability
- [ ] Avoid N+1 queries by using `sudo().search().read()` with `load='_classic_read'` or `browse()`. 
- [ ] Efficient use of ORM methods (e.g., `create`, `write`, `unlink`, `search`, `read_group`).
- [ ] Database indexes are considered for frequently searched or sorted fields.

### 7. Testing
- [ ] Appropriate Odoo test cases are created for new features and bug fixes.
- [ ] Test cases cover expected use, edge cases, and failure scenarios.
- [ ] Tests are run and pass successfully.

### 8. Documentation
- [ ] `README.md` is updated with new features, dependencies, or setup instructions.
- [ ] Non-obvious code sections have inline comments.
- [ ] Complex logic includes `# Reason:` comments explaining the rationale.
- [ ] Version compatibility notes are included in docstrings or comments where behavior differs between Odoo versions.

## Reference
Refer to the main `PLANNING.md` and Odoo official documentation for detailed best practices specific to Odoo 17 and 18.

See Odoo-specific module QA best practices and version notes in [Odoo KB](../data/odoo-kb.md). 