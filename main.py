from stats import word_count, char_count, sort_dict
import sys
def get_book_test(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    import sys
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    content = get_book_test(file_path)
    dic = char_count(content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt..")
    print("----------- Word Count ----------")
    print(f"Found {word_count(content)} total words ")
    print("--------- Character Count -------")
    dic = sort_dict(dic)
    for row in dic:
        print(f"{row['char']}: {row['cnt']}")




#book_dir = "./books/frankenstein.txt"
main()