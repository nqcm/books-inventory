import pytest

from books.models import Book


@pytest.fixture(scope='function')
def add_book():
    def _add_book(title, genre, year):
        book = Book.objects.create(title=title, genre=genre, year=year)
        return book
    return _add_book