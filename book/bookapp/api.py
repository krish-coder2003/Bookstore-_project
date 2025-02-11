from ninja import NinjaAPI
from .models import Book
from .schemas import BookSchema

api = NinjaAPI()

@api.get("/books", response=list[BookSchema])
def list_books(request):
    return Book.objects.all()

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    return Book.objects.get(id=book_id)

@api.post("/books", response=BookSchema)
def create_book(request, book: BookSchema):
    new_book = Book.objects.create(**book.dict())
    return new_book

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, book: BookSchema):
    existing_book = Book.objects.get(id=book_id)
    for key, value in book.dict().items():
        setattr(existing_book, key, value)
    existing_book.save()
    return existing_book

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    Book.objects.get(id=book_id).delete()
    return {"success": True}