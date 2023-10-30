def word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def letter_count(file_contents):
    letter_count_dictionary = {}
    for character in file_contents:
        if character.isalpha():
            letter = f"{character}".lower()
        if letter in letter_count_dictionary:
            letter_count_dictionary[letter] += 1
        else:
            letter_count_dictionary[letter] = 1 
    sorted_dict = dict(sorted(letter_count_dictionary.items()))
    return sorted_dict
            
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = word_count(file_contents)
    letter_dict = letter_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for key in letter_dict:
        print(f"The '{key}' character was found {letter_dict.get(key)}")
    print("--- End report ---")

    
        