from stats import count_words, count_chars

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_contents)
    num_chars = count_chars(book_contents)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()