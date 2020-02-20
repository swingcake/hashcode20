#! /usr/bin/python3


def submit(context, output):
    f = open(output, "w+")
    f.write(f"{context.librariesNumber}\n")
    for library in context.libraries:
        f.write(f"{library.id} {library.booksNumber}\n")
        f.write(" ".join(str(book) for book in library.booksID))
        f.write("\n")
    f.close()
