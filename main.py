from stats import word_count, count_charcaters, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

num_words = word_count(get_book_text("./books/frankenstein.txt"))
counted_characters_list = count_charcaters(get_book_text("books/frankenstein.txt"))
counted_characters_list.sort(reverse=True, key=sort_on)

def main():
    print(f"""============ BOOKBOT ============\n
Analyzing book found at books/frankenstein.txt...\n
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
