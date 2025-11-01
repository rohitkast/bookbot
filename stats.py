def get_book_text(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    with open(file_path) as f:
        content = f.read()
        return content

def get_num_of_words(string):
    arr = string.split()
    return len(arr)

def get_char_count(string):
    count_dict = {}

    for char in string:
        lowerChar = char.lower()
        if lowerChar in count_dict:
            count_dict[lowerChar] += 1
        else:
            count_dict[lowerChar] = 1  
    return count_dict

def sort_on(items):
    return items["num"]

def sorted(char_counts):
    list_of_char_count = []

    for char,value in char_counts.items():
        if not char.isalpha():
            continue
        
        list_of_char_count.append({'name': char, "num": value})

    list_of_char_count.sort(reverse="True", key=sort_on)
    return(list_of_char_count)