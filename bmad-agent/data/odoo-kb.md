# Odoo Knowledge Base (Odoo KB)

This file contains Odoo-specific best practices, code snippets, version notes, and reference material for use by BMAD agents/personas working on Odoo 17/18 projects.

---

## 1. Odoo Module Structure

- Each module should have:
  - `__manifest__.py` (module metadata)
  - `__init__.py` (Python package init)
  - `models/` (Python models)
  - `views/` (XML views, QWeb templates)
  - `security/` (access rights, record rules)
  - `data/` (initial data, demo data)
  - `static/` (JS, CSS, images)
  - `controllers/` (Python HTTP controllers, if needed)

---

## 2. Odoo ORM Best Practices

- Use Odoo ORM methods (`search`, `create`, `write`, `unlink`) instead of raw SQL.
- Always add docstrings to models and methods.
- Use computed fields and constraints for business logic.
- Use `_sql_constraints` for database-level constraints.
- Use `@api.model`, `@api.multi`, `@api.depends`, `@api.constrains` decorators appropriately.

**Example:**
```python
class MyModel(models.Model):
    _name = 'my.model'
    name = fields.Char(required=True)
    value = fields.Float()
    @api.constrains('name')
    def _check_name(self):
        if self.search([('name', '=', self.name), ('id', '!=', self.id)]):
            raise ValidationError("Name must be unique.")
```

---

## 3. Security & Access Rights

- Define all access rights in `security/ir.model.access.csv`.
- Use record rules for row-level security.
- Avoid using `sudo()` unless absolutely necessary.
- Never hardcode credentials or secrets in code.

---

## 4. QWeb & Views

- Use unique `id` and `name` for each template.
- Use `t-if`, `t-foreach`, `t-esc` for logic and data binding.
- Register templates in the manifest or asset bundles.

**Example:**
```xml
<template id="my_template" name="My Template">
    <t t-if="record">
        <span t-esc="record.name"/>
    </t>
</template>
```

---

## 5. Odoo 17 vs 18 Notes

- Odoo 18 introduces new view types and changes to chatter integration.
- Some XML tags and JS APIs may be deprecated or renamed.
- Always check the official Odoo documentation for version-specific changes.

---

## 6. Testing

- Use Odoo's built-in test framework (`tests/` folder).
- Write tests for models, controllers, and business logic.
- Cover at least: expected use, edge case, and failure case.

---

## 7. References

- [Odoo 17 Documentation](https://www.odoo.com/documentation/17.0/)
- [Odoo 18 Documentation](https://www.odoo.com/documentation/18.0/)
- [Odoo Developer Best Practices](https://www.odoo.com/documentation/17.0/developer/howtos)

---

*Expand this file as your project grows!* 