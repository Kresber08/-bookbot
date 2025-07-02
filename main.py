import sys
from stats import (
    convert_to_list,
    number_of_words, 
    dict_char_count,
)
    

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    num_words = number_of_words(text)
    chars_dict = dict_char_count(text)
    chars_sorted_list = convert_to_list(chars_dict)
    print_report(bookpath, num_words, chars_sorted_list)
    




def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(bookpath, num_words, chars_sorted_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookpath}...')
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for char_dict in chars_sorted_list:
        print(f"{char_dict['char']}: {char_dict['num']}")

    print('============= END ===============')



main()

