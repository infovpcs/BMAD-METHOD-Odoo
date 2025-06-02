# Product Requirements Document (PRD) - Odoo Library Management

## 1. Goal & Objective
Develop a custom Odoo module to manage a library's books, authors, and borrowing process.

## 2. Functional Requirements
- Add, edit, and remove books and authors.
- Track book availability and borrowing status.
- Allow users to borrow and return books.
- Provide list, form, and kanban views for books.
- Restrict book management to librarians (user group).
- Record borrowing history for each book.

## 3. Non-Functional Requirements
- Follow Odoo coding and security best practices.
- Ensure compatibility with Odoo 17/18.
- Provide unit tests for all business logic.
- Document the module in README.md.

## 4. User Stories
- As a librarian, I want to add new books so that the library catalog is up to date.
- As a user, I want to borrow a book so that I can read it.
- As a librarian, I want to see which books are currently borrowed.

## 5. Acceptance Criteria
- All features are accessible via the Odoo web client.
- Only librarians can manage books/authors.
- Borrowing/returning updates book status in real time.
- All code passes Odoo's test framework. 