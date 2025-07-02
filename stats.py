def number_of_words(book_text):
    words_in_book = (book_text).split()
    return len(words_in_book)


def dict_char_count(book_text):
    char_count = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count


def sort_on(dict):
    return dict["num"]


def convert_to_list(full_dictionary):
    list_of_char_num = []

    for char_dict in full_dictionary:
        char_num_dict = {}
        if char_dict.isalpha():
            char_num_dict["char"] = char_dict
            char_num_dict["num"] = full_dictionary[char_dict]
            list_of_char_num.append(char_num_dict)
    
    """
    Or optional loop method for possible optimization

    for char_dict in list_of_dict:
        list_of_char_num.append({"char": char_dict, "num": list_of_dict[char_dict]})
    """

    list_of_char_num.sort(reverse=True, key=sort_on)
    return list_of_char_num
               

