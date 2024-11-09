def main():
    with open("books/frankenstein.txt") as f: #hardcoded
        file_contents = f.read()
        #print(countWords(file_contents))
        #print(countChars(file_contents.lower()))
        print(printReport(file_contents))

def countWords(book):
    words = book.split()
    return len(words)

def countChars(book):
    result = {}
    for char in book:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def printReport(book):
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    chars_dict = countChars(book)
    openingStatement = "--- Begin report of books/frankenstein.txt ---\n" #as the book is hardcoded, this is hardcoded also
    wordCountStatement = f"{countWords(book)} words found in the document\n\n"
    charsStatement = ""
    for letter in alphabet:
        if letter in chars_dict:
            charsStatement += f"The {letter} character was found {chars_dict[letter]} times\n"
        else:
            charsStatement += f"The {letter} character was not found\n"
    endStatement = "--- End report ---"
    print(openingStatement + wordCountStatement + charsStatement + endStatement)
    return "" #this comes up in STD, so I left it as empty string, so it only creates new line


main()