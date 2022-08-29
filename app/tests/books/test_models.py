import pytest

from books.models import Book


@pytest.mark.django_db
def test_book_model():
    book = Book(title="Count of Monte Cristo", genre="fiction", year="1850")
    book.save()
    assert book.title == "Count of Monte Cristo"
    assert book.genre == "fiction"
    assert book.year == "1850"
    assert book.created_date
    assert book.updated_date
    assert str(book) == book.title