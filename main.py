from stats import get_wordcount
from stats import char_count
from stats import get_vro
import sys



def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num = get_wordcount(get_book_text(sys.argv[1]))
    dicts = char_count(get_book_text(sys.argv[1]))
    msg = f"{num} words found in the document"
    sorrty = get_vro(dicts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in sorrty:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

    

main()