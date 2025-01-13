print("hello world")

def count_words(string):
    return len(string.split())

def count_chars(string):
    low = string.lower()

    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for char in low:
        if char not in alphabet.keys():
            continue
        alphabet[char] += 1
    return alphabet
path = "books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()

    print(f"--- Beginning report of {path} ---")
    print(count_words(file_contents))

    dic = count_chars(file_contents)
    for ltr in dic:
        print(f"the \'{ltr}\' character was found {dic[ltr]} times")

    print("--- End report of {path} ---")
