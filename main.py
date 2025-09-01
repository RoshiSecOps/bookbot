from stats import word_count, count_charcaters, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    sort_chars(count_charcaters(get_book_text("books/frankenstein.txt")))
    
main()