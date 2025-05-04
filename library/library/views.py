# library/views.py
import json
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

BOOKS_FILE = 'books.json'

if not os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, 'w') as f:
        json.dump([], f)

def index(request):
    with open(BOOKS_FILE, 'r') as f:
        books = json.load(f)
    return render(request, 'index.html', {'books': books})

def get_books(request):
    with open(BOOKS_FILE, 'r') as f:
        books = json.load(f)
    return JsonResponse(books, safe=False)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        with open(BOOKS_FILE, 'r') as f:
            books = json.load(f)
        new_book = {
            'id': len(books) + 1,
            'title': data['title'],
            'author': data['author'],
            'year': data['year']
        }
        books.append(new_book)
        with open(BOOKS_FILE, 'w') as f:
            json.dump(books, f, indent=4)
        return JsonResponse({'status': 'success'})
    return render(request, 'add_book.html')

def book_detail(request, book_id):
    with open(BOOKS_FILE, 'r') as f:
        books = json.load(f)
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return render(request, 'book_detail.html', {'book': book})
    return HttpResponse('Книга не знайдена', status=404)