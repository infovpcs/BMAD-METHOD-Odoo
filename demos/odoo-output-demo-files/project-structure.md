# Project Structure

This project follows the standard Odoo custom module structure. Each module is self-contained and can be installed in an Odoo instance.

## Example Odoo Module Layout

```plaintext
my_module/
├── __manifest__.py         # Module manifest (metadata, dependencies, etc.)
├── __init__.py             # Module Python package initializer
├── models/                 # Python files for business models (Odoo ORM)
│   └── my_model.py
├── views/                  # XML files for UI views, menus, actions
│   └── my_model_views.xml
├── controllers/            # Python files for HTTP controllers (optional)
│   └── main.py
├── security/               # Access control, record rules
│   ├── ir.model.access.csv
│   └── security.xml
├── data/                   # Demo or initial data (XML/CSV)
│   └── demo_data.xml
├── static/                 # Static assets (JS, CSS, images)
│   ├── description/
│   ├── src/
│   └── tests/
├── tests/                  # Python test files (unit/integration)
│   └── test_my_model.py
├── README.md               # Module documentation
└── ...
```

### Directory/Files Explained
- `__manifest__.py`: Declares module metadata, dependencies, version, etc.
- `models/`: Contains Python classes inheriting from `models.Model` (Odoo ORM).
- `views/`: XML files defining forms, lists, menus, and actions.
- `controllers/`: HTTP controllers for custom endpoints (optional).
- `security/`: Access rights and record rules for data security.
- `data/`: Initial/demo data loaded on install.
- `static/`: Web assets (JS, CSS, images, OWL components).
- `tests/`: Unit and integration tests using Odoo's test framework.
- `README.md`: Documentation for the module. 