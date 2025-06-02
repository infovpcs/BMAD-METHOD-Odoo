# UX/UI Specification (Odoo)

## General Principles
- Follow Odoo's native UI/UX conventions for consistency.
- Use QWeb for XML-based views (form, tree, kanban, calendar, etc.).
- Use OWL for advanced client-side components (Odoo 14+).
- Keep forms simple and intuitive; group related fields.
- Use smart buttons, statusbars, and kanban views for better usability.
- Ensure all actions are accessible via menus or buttons.
- Use tooltips and help texts for user guidance.
- Ensure mobile responsiveness (Odoo web client is responsive by default).

## Example: Book Form View (QWeb/XML)
```xml
<record id="view_form_library_book" model="ir.ui.view">
    <field name="name">library.book.form</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <form string="Library Book">
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="author_id"/>
                    <field name="published_date"/>
                    <field name="isbn"/>
                    <field name="is_available"/>
                </group>
                <notebook>
                    <page string="Description">
                        <field name="description"/>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
``` 