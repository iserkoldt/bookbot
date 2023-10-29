with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    def word_count(file_contents):
        words = file_contents.split()
        word_count = len(words)
        print("Number of words:", word_count)
        
