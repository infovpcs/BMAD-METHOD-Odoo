# Checklist: Odoo Module Upgrade Checklist for AI Agent

## Purpose
This checklist guides an AI agent through the process of upgrading an Odoo custom module from one version to another (e.g., Odoo 17 to Odoo 18), or performing minor version updates within the same major release. It focuses on identifying required code changes, data migrations, and adherence to new Odoo APIs and best practices.

## Instructions for AI Agent
When performing an Odoo module upgrade, use the following checks. For each item, analyze the existing module's code against the target Odoo version's documentation and propose necessary modifications. If a data migration script is required, outline the steps.

## Checklist Items

### 1. Pre-Upgrade Analysis
- [ ] Identify the target Odoo version (e.g., 18.0) and gather its release notes, migration guides, and API changes.
- [ ] List all custom modules and their dependencies that need to be upgraded.
- [ ] Review `__manifest__.py` files for version compatibility (`'version': '18.0.1.0.0'`).
- [ ] Identify any deprecated modules or features in the new Odoo version that the custom module relies on.
- [ ] Identify any new required dependencies in the target Odoo version.

### 2. Manifest File Update
- [ ] Update the `__manifest__.py` `version` field to the new target version.
- [ ] Review and update `depends` list to reflect any changes in core Odoo dependencies.
- [ ] Add or update `assets` bundles if frontend assets or OWL/QWeb templates have changed structure or requirements in the new version.

### 3. Python Code Migration (Models, Controllers, Wizards)
- [ ] **ORM API Changes**: Check for deprecated ORM methods and update to new equivalents (e.g., `self.env.ref()` vs `self.env['ir.model.data']._xmlid_to_res_id()`).
- [ ] **Field Type Changes**: Review any changes in field definitions (e.g., `fields.Char`, `fields.Html`, `fields.Selection`).
- [ ] **API Decorator Changes**: Verify usage of `@api.model`, `@api.multi`, `@api.one` (migrate `multi`/`one` to modern alternatives if still present and not handled by `odoo-dev-scripts`).
- [ ] **Model Inheritance**: Confirm that inheritance patterns (`_inherit`, `_inherits`, `_name`) are still valid and compatible.
- [ ] **Method Signature Changes**: Update method signatures where core Odoo methods have changed (e.g., `create`, `write`, `unlink`).
- [ ] **Security**: Review and update security rules (`ir.model.access.csv`, `ir.rule`) for any new models or field access changes.
- [ ] **Controller Routes**: Check and update HTTP routes (`@http.route`) if any routing conventions or security attributes have changed.
- [ ] **QWeb/OWL Context Changes**: Identify if `self.env.context` or `self.env.user` behavior has changed in QWeb/OWL contexts.
- [ ] **Translatable Strings**: Ensure all new and modified strings are properly marked for translation.
- [ ] **Refactor Deprecated Code**: Flag and refactor any known deprecated patterns or features from previous Odoo versions that are no longer supported.

### 4. XML View Migration
- [ ] **Root Element Changes**: Replace `<tree>` with `<list>` for tree views in Odoo 18+.
- [ ] **Widget Changes**: Update deprecated widgets to their modern equivalents (e.g., `mail_thread` and `mail_activity` widgets to `<chatter/>` in Odoo 18+).
- [ ] **Attribute Changes**: Review and update attributes that may have been renamed or had their behavior altered (e.g., `column_invisible`, `optional`).
- [ ] **XPaths**: Verify that existing `xpath` expressions are still valid and target the correct elements in the new Odoo version's base views.
- [ ] **QWeb Directives**: Check for any changes in QWeb directives (`t-field`, `t-out`, `t-esc`, `t-if`, `t-foreach`, `t-call`) or new directives that could be leveraged.
- [ ] **Report Templates**: Ensure QWeb report templates adapt to any new structural changes or data exposure in the target Odoo version.

### 5. Data Migration (if applicable)
- [ ] Determine if data migration scripts (`post_init_hook`, `uninstall_hook`, `noupdate` data) are required.
- [ ] Outline data migration steps for changed field types, renamed fields, or data model restructuring.
- [ ] Ensure data integrity is maintained during migration.

### 6. Frontend Asset Migration (JS, SCSS)
- [ ] **OWL API Changes**: Update OWL components for any breaking changes in the OWL framework.
- [ ] **JavaScript Module System**: Adapt to any changes in Odoo's JavaScript module system (e.g., `require` vs `@odoo-module`).
- [ ] **SCSS Variable/Mixins**: Review and update SCSS based on changes in Odoo's default Bootstrap theme variables or mixins.

### 7. Testing & Validation
- [ ] Run all existing Odoo test cases and fix any failures.
- [ ] Create new test cases for upgraded features if necessary.
- [ ] Perform thorough manual functional testing on the upgraded module.
- [ ] Verify that all existing functionalities work as expected in the new Odoo version.

### 8. Documentation Update
- [ ] Update `README.md` and module documentation to reflect the new Odoo version compatibility and any significant changes.
- [ ] Document specific migration steps or considerations for future upgrades.

## Reference
- Odoo Official Documentation (target version migration notes): `https://www.odoo.com/documentation/{TARGET_VERSION}/`
- Odoo Upgrade Guide (e.g., OCA migration guides)
- Odoo changelogs for specific versions.
- See Odoo-specific upgrade best practices and version notes in [Odoo KB](../data/odoo-kb.md). 