# Task: Create QWeb Template

## Purpose
Guide the creation of a new QWeb template for Odoo 17/18, including XML structure, template registration, and best practices for maintainability and reusability.

## Instructions
1. Create a new XML file for the QWeb template in the appropriate `views/` or `static/src/xml/` directory.
2. Define the template with a unique `id` and `name`.
3. Use Odoo QWeb best practices for conditionals, loops, and data binding.
4. Register the template in the module's manifest or asset bundle.
5. Reference Odoo and QWeb best practices for maintainability and reusability.

## Example Output
- `my_template.xml` (QWeb template)
- Asset registration in `__manifest__.py` or `web.assets_frontend`

## Reference
See QWeb template examples and best practices in web-build-sample/data.txt.
See Odoo-specific QWeb best practices and version notes in [Odoo KB](../data/odoo-kb.md).

## Related Checklists
- [Odoo Frontend/Website/OWL Checklist](../checklists/odoo-frontend-website-owl-checklist.md)
- [Odoo Module QA Checklist](../checklists/odoo-module-qa-checklist.md)
- [Odoo Upgrade Checklist](../checklists/odoo-upgrade-checklist.md) 