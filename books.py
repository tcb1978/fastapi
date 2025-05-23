from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
  {
    'title': 'Title One',
    'author': 'Author One',
    'category': 'science'
  },
  {
    'title': 'Title Two',
    'author': 'Author Two',
    'category': 'science'
  },
  {
    'title': 'Title Three',
    'author': 'Author Three',
    'category': 'history'
  },
  {
    'title': 'Title Four',
    'author': 'Author Four',
    'category': 'math'
  },
  {
    'title': 'Title Five',
    'author': 'Author Five',
    'category': 'math'
  },
  {
    'title': 'Title Six',
    'author': 'Author Two',
    'category': 'math'
  }
]


@app.get('/books')
async def read_all_books():
  return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
  for book in BOOKS:
    if book.get('title').casefold() == book_title.casefold():
      return book

@app.get('/books/')
async def read_catergory_by_query(book_category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('category').casefold() == book_category.casefold():
      books_to_return.append(book)
  return books_to_return

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, book_category: str):
  books_to_return = []
  for book in BOOKS:
    if book.get('author').casefold() == book_author.casefold() and \
      book.get('category').casefold() == book_category.casefold():
      books_to_return.append(book)
  return books_to_return

@app.post('/books/create_book')
async def create_book(new_book=Body()):
  BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
  for i in range(len(BOOKS)):
    if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
      BOOKS[i] = updated_book

@app.delete('/books/delete_book')
async def delete_book(book_title: str):
  for i in range(len(BOOKS)):
    if BOOKS[i].get('title').casefold() == book_title.casefold():
      BOOKS.pop(i)
      return BOOKS
  return {'message': 'Book not found'}

@app.delete('/books/delete_all_books')
async def delete_all_books():
  BOOKS.clear()
  return {'message': 'All books deleted'}

@app.delete('/books/delete_all_books_by_author')
async def delete_all_books_by_author(book_author: str):
  books_to_delete = []
  for i in range(len(BOOKS)):
    if BOOKS[i].get('author').casefold() == book_author.casefold():
      books_to_delete.append(BOOKS[i])
      BOOKS.pop(i)
  return books_to_delete

@app.delete('/books/delete_all_books_by_category')
async def delete_all_books_by_category(book_category: str):
  books_to_delete = []
  for i in range(len(BOOKS)):
    if BOOKS[i].get('category').casefold() == book_category.casefold():
      books_to_delete.append(BOOKS[i])
      BOOKS.pop(i)
  return books_to_delete

@app.delete('/books/delete_all_books_by_author_and_category')
async def delete_all_books_by_author_and_category(book_author: str, book_category: str):
  books_to_delete = []
  for i in range(len(BOOKS)):
    if BOOKS[i].get('author').casefold() == book_author.casefold() and \
      BOOKS[i].get('category').casefold() == book_category.casefold():
      books_to_delete.append(BOOKS[i])
      BOOKS.pop(i)
  return books_to_delete

@app.delete('/books/delete_all_books_by_author_or_category')
async def delete_all_books_by_author_or_category(book_author: str, book_category: str):
  books_to_delete = []
  for i in range(len(BOOKS)):
    if BOOKS[i].get('author').casefold() == book_author.casefold() or \
      BOOKS[i].get('category').casefold() == book_category.casefold():
      books_to_delete.append(BOOKS[i])
      BOOKS.pop(i)
  return books_to_delete