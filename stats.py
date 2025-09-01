def word_count(file_contents):
    words_count = file_contents.split()
    return len(words_count)

def count_charcaters(file_contents):
    total_chars = {}
    for word in file_contents:
        word = word.lower()
        for char in word:
            if char in total_chars:
                total_chars[char] += 1
            else:
                total_chars[char] = 1
    return total_chars

def sort_chars(chars_dict):
    chars_list = []
    for char in chars_dict:
        char = {"char": char, "num": chars_dict[char]}
        chars_list.append(char)
  
    print(chars_list)