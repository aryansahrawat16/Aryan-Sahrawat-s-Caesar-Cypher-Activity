# Aryan, Sahrawat, 340878883

#type a word and a number in and then leave a space inbetween them (No comma's)

import string

def cypher(word, num):
    ''' shift the letters in the word to the right of left depending on the positive or negative number

    arguments:
        word : string, the user inputs a word
        num : integer, user inputs a postitve or negative number to shift the letters in the word left or right

    return:
        string, the word would change to the new string, encrypts the given word
    '''
    word = word.replace(',',"")
    alphabet = string.ascii_lowercase
    letters = list(word.lower())
    for i in range(len(letters)):
        variable = alphabet.find(letters[i])
        variable += int(num)
        if variable >= 26:
            variable = variable % 26
            letters[i] = alphabet[variable]
        else:
            letters[i] = alphabet[variable]
    word = "".join(letters)
    return word

def main():
    word, num = input().split()
    print(cypher(word, num))

main()