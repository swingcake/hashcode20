#! /usr/bin/python3
from models import Context
from models import Book
from models import Library


def parse(filePath):
    file = open(filePath, "r")
    lines = [i for i in file.read().split('\n') if i]
    context = Context(*[int(j) for j in lines[0].split(' ')])

    for i, score in enumerate(lines[1].split(' ')):
        context.books.append(Book(i, int(score)))
    for i in range(2, len(lines), 2):
        library = Library(int((i-2)/2), *[int(j) for j in lines[i].split(' ')])
        library.booksID = [int(ID) for ID in lines[i + 1].split(' ')]
        context.libraries.append(library)
    return context

