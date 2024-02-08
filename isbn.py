from sys import argv
from urllib3 import request

book_ISBN = argv[1]
book = (
    request(
        "GET",
        f"https://openlibrary.org/api/books?bibkeys=ISBN:{book_ISBN}&jscmd=data&format=json",
    )
    .json()
    .get(f"ISBN:{book_ISBN}")
)

if book:
    book_title = book.get("title")
    book_subtitle = f" - {book.get('subtitle')}" if "subtitle" in book else ""
    book_publish_year = book.get("publish_date")[-4:]
    book_full_title = f"{book_title}{book_subtitle} ({book_publish_year})".replace(
        ":", " -"
    )

    print(book_full_title)
