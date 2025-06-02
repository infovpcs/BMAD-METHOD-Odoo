# Task: Create Odoo Module

## Purpose
Guide the scaffolding of a new Odoo module for Odoo 17/18, including manifest, module structure, and initial files.

## Instructions
1. Create a new directory for the module under `addons/`.
2. Add `__manifest__.py` with module metadata, dependencies, and data files.
3. Add `__init__.py` to initialize Python packages.
4. Create subfolders: `models/`, `views/`, `security/`, `data/` as needed.
5. Add a sample model and view.
6. Reference Odoo best practices for module structure and manifest fields.

## Example Output
- `__manifest__.py`
- `__init__.py`
- `models/`
- `views/`
- `security/ir.model.access.csv`

## Reference
See Odoo module structure and best practices in web-build-sample/data.txt.
See Odoo-specific module structure and version notes in [Odoo KB](../data/odoo-kb.md).

## Related Checklists
- [Odoo Module QA Checklist](../checklists/odoo-module-qa-checklist.md)
- [Odoo Security Checklist](../checklists/odoo-security-checklist.md)
- [Odoo Upgrade Checklist](../checklists/odoo-upgrade-checklist.md) 