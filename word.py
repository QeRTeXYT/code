from dataclasses import replace
import string
from urllib.parse import MAX_CACHE_SIZE


text = input(">>>")

def longest_word():
    max_word1 = ''
    max_word2 = ''
    max_word3 = ''
    max_word4 = ''
    max_word5 = ''
    words = text.split()
    for word in words :
        clear_word = remove_puct(word)
        if len(clear_word) > len(max_word1):
            max_word1 = clear_word
        if len(max_word1) > len(clear_word) > len(max_word2):
            max_word2 = clear_word
        if len(max_word2) > len(clear_word)> len(max_word3):
            max_word3 = clear_word
        if len(max_word3) > len(clear_word)> len(max_word4):
            max_word4 = clear_word
        if len(max_word4) >> len(clear_word)> len(max_word5):
            max_word5 = clear_word
        
    return max_word1,max_word2,max_word3,max_word4,max_word5       


def remove_puct(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word = word.replace(punc,'')
    return word

print(longest_word())