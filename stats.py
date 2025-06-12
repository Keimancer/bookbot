def split_text( book ):
    words_list = book.split()
    return len(words_list)

def char_count( book ):
    lower_book = []
    for char in book:
        lower_book.append(char.lower())
    count_dict = {}
    for char in lower_book:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def sort_dict( count_dict ):
    unsorted_list = []
    for letter in count_dict:
        unsorted_list.append({ "char": letter, "num": count_dict[letter] })
    unsorted_list.sort(key=sort_on, reverse=True)
    return unsorted_list