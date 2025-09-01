def word_count(file_contents):
    words_count = file_contents.split()
    return len(words_count)

def count_charcaters(file_contents):
    total_chars = {}
    chars_list = []
    for word in file_contents:
        word = word.lower()
        for char in word:
            if char in total_chars:
                total_chars[char] += 1
            else:
                total_chars[char] = 1
    for char in total_chars:
        char = {"char": char, "num": total_chars[char]}
        chars_list.append(char)
    return chars_list

def sort_on(items):
    return items["num"]


  
