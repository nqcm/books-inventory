import json

import pytest

from books.models import Book


@pytest.mark.django_db
def test_add_book(client):
    books = Book.objects.all()
    assert len(books) == 0

    resp = client.post(
        "/api/books/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    books = Book.objects.all()
    assert len(books) == 1


@pytest.mark.django_db
def test_add_book_invalid_json(client):
    books = Book.objects.all()
    assert len(books) == 0

    resp = client.post(
        "/api/books/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Book.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_book_invalid_json_keys(client):
    books = Book.objects.all()
    assert len(books) == 0

    resp = client.post(
        "/api/books/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    books = Book.objects.all()
    assert len(books) == 0