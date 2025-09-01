from stats import word_count, count_charcaters, sort_on
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = word_count(get_book_text(sys.argv[1]))
    counted_characters_list = count_charcaters(get_book_text(sys.argv[1]))
    counted_characters_list.sort(reverse=True, key=sort_on)
    print(f"""============ BOOKBOT ============\n
Analyzing book found at {sys.argv[1]}...\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------""")
    for char in counted_characters_list:
        if char["char"].isalpha() == False:
            continue
        else:
            print(f"{char["char"]}: {char["num"]}\n")
    print("============= END ===============")

main()
