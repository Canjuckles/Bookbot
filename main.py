
def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


def get_book_text(filepath): 
    try:
        with open(filepath, encoding="utf-8") as f: 
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"ERROR: FILE PATH {filepath} CANNOT BE FOUND")
        return None


def count_words(text):
    words = text.split()
    return len(words)
    

if __name__ == "__main__":     
    main()


