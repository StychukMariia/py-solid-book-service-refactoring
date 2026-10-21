from app.book import Book


class ConsolePrinter:
    def print_book(self, book: Book, show_title: bool) -> None:
        if show_title:
            print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter:
    def print_book(self, book: Book, show_title: bool) -> None:
        if show_title:
            print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
