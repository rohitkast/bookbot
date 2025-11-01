import sys
from stats import get_book_text, get_num_of_words, get_char_count, sorted

entries = sys.argv

if len(entries) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
# 'books/frankenstein.txt'
def main():
    text = get_book_text(book_path)
    num_words = get_num_of_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    char_count = get_char_count(text)
    
    print("--------- Character Count -------")
    sorted_list = sorted(char_count)
    
    for entry in sorted_list:
        print(f"{entry['name']}: {entry['num']}")
    
    print("============= END ===============")

main()