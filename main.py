import sys
from stats import split_text
from stats import char_count
from stats import sort_dict

def get_book_text( path ):
    with open( path ) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at { book_path }')
    print('----------- Word Count ----------')
    print('Found', split_text(get_book_text( book_path )), 'total words')
    print('--------- Character Count -------')
    for char in sort_dict(char_count(get_book_text( book_path ))):
        if char['char'].isalpha():
            print(f'{ char['char'] }: { char['num'] }')
    print('============= END ===============')

main()