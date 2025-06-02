# Task: Create Odoo Model

## Purpose
Guide the creation of a new Odoo model for Odoo 17/18, including Python class, fields, security, and basic views.

## Instructions
1. Define the model in Python using Odoo ORM best practices.
2. Add fields, constraints, and docstrings.
3. Update `ir.model.access.csv` for security.
4. Create basic XML views (form, tree, search).
5. Reference Odoo best practices for naming, security, and code style.

## Example Output (List View)
<!-- For Odoo 17.0 -->
<tree string="My List">
    <field name="name"/>
    <field name="active"/>
</tree>

<!-- For Odoo 18.0 -->
<list string="My List">
    <field name="name"/>
    <field name="active"/>
</list>

## Example Output (Form View Chatter)
<!-- For Odoo 17.0 -->
<field name="message_ids" widget="mail_thread"/>
<field name="activity_ids" widget="mail_activity"/>

<!-- For Odoo 18.0 -->
<chatter/>

## Reference
See Odoo ORM examples and best practices in web-build-sample/data.txt.
See Odoo-specific model best practices and version notes in [Odoo KB](../data/odoo-kb.md).

## Related Checklists
- [Odoo Module QA Checklist](../checklists/odoo-module-qa-checklist.md)
- [Odoo Security Checklist](../checklists/odoo-security-checklist.md)
- [Odoo Upgrade Checklist](../checklists/odoo-upgrade-checklist.md) 