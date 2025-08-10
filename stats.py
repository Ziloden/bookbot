def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in char_count:
            char_count[lower_case_char] += 1
        else:
            char_count[lower_case_char] = 1
    return char_count