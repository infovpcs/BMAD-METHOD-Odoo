# API Reference (Odoo)

## Example: Custom REST Controller

```python
from odoo import http
from odoo.http import request

class LibraryApiController(http.Controller):
    @http.route('/api/library/books', type='json', auth='user', methods=['GET'])
    def get_books(self):
        books = request.env['library.book'].search([])
        return [
            {
                'id': book.id,
                'name': book.name,
                'author': book.author_id.name,
                'published_date': book.published_date,
                'isbn': book.isbn,
                'is_available': book.is_available,
            }
            for book in books
        ]
```

## Notes
- Use Odoo's `http.Controller` for custom endpoints.
- Use `auth='user'` or `auth='public'` as needed.
- Always validate and sanitize input in controllers.
- For advanced integrations, consider using Odoo's built-in XML-RPC/JSON-RPC APIs. 