Django 1o1

My views.py file now includes functions with permission decorators to ensure users have the appropriate permissions before they can add, edit, delete, or list books. The list_books function is also correctly defined.

Here's a quick recap of what has been done:

Imports: I have imported the necessary modules, including render, get_object_or_404, redirect, permission_required, Book, and BookForm.

Permission Decorators: I have used @permission_required decorators with raise_exception=True to enforce permission checks on the add, edit, and delete book functions.

Function Definitions: The add_book, edit_book, and delete_book functions handle adding, editing, and deleting books, respectively. The list_books function fetches all books and renders them in the appropriate template.