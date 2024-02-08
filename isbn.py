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

print(book)
