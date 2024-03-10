class Book:
    material = 'бумага'
    have_text = True

    def __init__(self, title, author, pages_count, ISBN, reserved):
        self.title = title
        self.author = author
        self.pages_count = pages_count
        self.ISBN = ISBN
        self.reserved = reserved


book_1 = Book('Идиот', 'Достоевский', 500, 9781774760161, True)
book_2 = Book('Евгений Онегин', 'Пушкин', 224, 9788437618234, False)
book_3 = Book('Мертвые Души', 'Гоголь', 480, 9788446016021, False)
book_4 = Book('Война и Мир', 'Толстой', 960, 9780393966473, False)
book_5 = Book('Горе от Ума', 'Грибоедов', 320, 9783847837312, False)

for book in [book_1, book_2, book_3, book_4, book_5]:
    if book.reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages_count}, материал: {book.material}, '
              f'зарезервированна')
    else:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages_count}, материал: {book.material}, '
              f'незарезервированна')


class SchoolBooks(Book):
    def __init__(self, title, author, pages_count, ISBN, reserved, subject, school_group, have_tasks):
        super().__init__(title, author, pages_count, ISBN, reserved)
        self.subject = subject
        self.school_group = school_group
        self.have_tasks = have_tasks


book_one = SchoolBooks('Алгебра', 'Иванов', 200, 987346666623, True,
                       'Математика', 9, True)
book_two = SchoolBooks('История', 'Петрова', 120, 879991223345, False,
                       'История древнего мира', 7, True)
book_three = SchoolBooks('Химия', 'Зеленов', 34, 333459854693, False,
                         'Химия', 8, True)
book_four = SchoolBooks('Геометрия', 'Матвеева', 40, 12345676788, False,
                        'Геометрия', 9, True)

for book in [book_one, book_two, book_three, book_four]:
    if book.reserved:
        print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages_count}, предмет: {book.subject}, '
              f'класс: {book.school_group}, зарезервированнна')
    else:
        print(
            f'Название: {book.title}, Автор: {book.author}, страниц: {book.pages_count}, предмет: {book.subject}, '
            f'класс: {book.school_group}, незарезервированнна')
