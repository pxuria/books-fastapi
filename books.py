from fastapi import FastAPI

app = FastAPI()

BOOKS=[
    {'title':'title 1','author':'author 1','category':'math'},
    {'title':'title 2','author':'author 2','category':'science'},
    {'title':'title 3','author':'author 3','category':'math'},
    {'title':'title 4','author':'author 4','category':'history'},
    {'title':'title 5','author':'author 5','category':'science'},
    {'title':'title 6','author':'author 6','category':'history'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/my_books")
async def read_all_books():
    return {'my_books': "my_books"}

@app.get("/books/{book_title}")
async def read_all_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {'book_title':book_title}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return