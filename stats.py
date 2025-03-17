

def count_words(text):
    words = text.split()
    return len(words)
    
def letter_counter(text): 
    characters = list(text)
    count = {}
    for i in characters:
        if not(i.lower() in count) and i.isalpha():
            count[f"{i.lower()}"] = 1 
        elif i.isalpha(): 
            count[i.lower()] += 1
    return count

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))


    
