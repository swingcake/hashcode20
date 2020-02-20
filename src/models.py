class Context:
    def __init__(self, booksNumber, librariesNumber, daysForScanning):
        self.booksNumber = booksNumber
        self.librariesNumber = librariesNumber
        self.daysForScanning = daysForScanning
        self.books = []
        self.libraries = []


class Library:
    def __init__(self, ID, booksNumber, signupTime, bokSentByDay):
        self.id = ID
        self.signupTime = signupTime
        self.booksNumber = booksNumber
        self.bookSentByDay = bokSentByDay
        self.booksID = []

    def getBooks(self, context):
        return [book for book in context.books if self.booksID.__contains__(book.id)]


class Book:
    def __init__(self, ID, score):
        self.id = ID
        self.score = score
