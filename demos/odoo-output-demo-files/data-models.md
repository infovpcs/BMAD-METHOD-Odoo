# Data Models (Odoo)

## Example Model: Library Book

```python
from odoo import models, fields, api

class LibraryBook(models.Model):
    """
    Represents a book in the library.
    """
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('res.partner', string='Author')
    published_date = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')
    description = fields.Text(string='Description')
    is_available = fields.Boolean(string='Available', default=True)

    @api.model
    def create(self, vals):
        # Reason: Ensure ISBN is unique before creating a book
        if 'isbn' in vals and self.search([('isbn', '=', vals['isbn'])]):
            raise ValueError('ISBN must be unique!')
        return super().create(vals)
```

## Relationships Example
- `Many2one`: Each book has one author (`res.partner`).
- `One2many`: An author can have many books.
- `Many2many`: Books can have multiple tags (not shown). 