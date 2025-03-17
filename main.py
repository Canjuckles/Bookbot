from stats import count_words, letter_counter, sort_dict_by_value
import sys



def main():

    # file path: "books/frankenstein.txt"
    try: 
        filepath = sys.argv[1]
        book_str = get_book_text(filepath)
        print(f"{count_words(book_str)} words found in the document")
        
        counted = letter_counter(book_str)

        display(sort_dict_by_value(counted),count_words(book_str),filepath)
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        
    
    

def get_book_text(filepath): 
    try:
        with open(filepath, encoding="utf-8") as f: 
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"ERROR: FILE PATH {filepath} CANNOT BE FOUND")
        return None

def display (char_count, word_count,filepath): 
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for i in char_count:
        print(f"{i}: {char_count[i]}")
    print("============= END ===============")

    pass






if __name__ == "__main__":     
    main()


