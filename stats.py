def get_wordcount(book_text):
    return len(book_text.split())

def char_count(book_text):
    book_text = book_text.lower()
    chars = {}
    for char in book_text:
        if (char in chars):
            chars[char] +=1
        else:
            chars[char] = 1
    return chars

def sort_on(d):
    return d["num"]
def get_vro(num_chars_dict):
    ret_list = []
    for ch in num_chars_dict:
        ret_list.append({"char": ch, "num": num_chars_dict[ch]})
    ret_list.sort(reverse=True, key=sort_on)
    return ret_list