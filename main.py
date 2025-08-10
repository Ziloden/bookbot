from stats import count_words, count_chars, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    num_chars = count_chars(book_contents)
    sorted_num_chars = sort_char_count(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_num_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

main()