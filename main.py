def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    print(book_contents)

main()