from ninja import Schema
from datetime import date

class BookSchema(Schema):
    title: str
    author: str
    published_date: date
    isbn: str
    price: float