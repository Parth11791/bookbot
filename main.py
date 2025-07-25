import sys
from stats import get_num_words,get_count_characters


if len(sys.argv)==1:
   print(f"Usage: python3 main.py <path_to_book>")
   sys.exit(1)


def get_book_text(s):
    with open(s) as f:
         file_contents = f.read()
    return file_contents


def main():
    result = get_book_text(sys.argv[1])
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    get_num_words(result)
    print(f"--------- Character Count -------")
    get_count_characters(result)
    print(f"============= END ===============")


main()
