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


@pytest.mark.django_db
def test_get_single_book(client, add_book):
    book = add_book(title="The Big Lebowski", genre="comedy", year="1998")
    resp = client.get(f"/api/books/{book.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/books/foo/")
    assert resp.status_code == 404

@pytest.mark.django_db
def test_get_all_books(client, add_book):
    book_one = add_book(title="The Big Lebowski", genre="comedy", year="1998")
    book_two = add_book("No Country for Old Men", "thriller", "2007")
    resp = client.get(f"/api/books/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == book_one.title
    assert resp.data[1]["title"] == book_two.title