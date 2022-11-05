from collections import Counter
from dataclasses import replace
from itertools import count, groupby
import string
from urllib.parse import MAX_CACHE_SIZE


text = input(">>>")
op = int(input('\n1 = топ 5 \n2 = повторюючісь слова \n3 = словник \nОберіть операцію>>'))

def longest_word():
    all_words = []
    top_5 = []
    x = -1
    top_5_var = []
    words = text.split()
    for word in words :
        clear_word = remove_puct(word)
        all_words.append(clear_word)    
    all_words = sorted(all_words, key=len , reverse=True)
    while x < 4:
        top_5.append(all_words[x+1])
        x = x+1
        print(f'Топ {x+1}: "{top_5[x]}" довжина: {len(top_5[x])}') 
        #top_5_var.append(f'Топ {x+1}: "{top_5[x]}" довжина: {len(top_5[x])}')       
    #print(top_5_var)
        
def remove_puct(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word = word.replace(punc, '')
        if '—' in word:
            word = word.replace(punc, '')
    return word

def most_com_word():
    all_words = []
    words = text.split()
    for word in words :
        clear_word = remove_puct(word)
        all_words.append(clear_word.lower())    
    all_words = Counter(all_words)
    all_words = all_words.most_common(5)
    print(all_words)
def slovnuk():
    all_words = []
    words = text.split()
    for word in words :
        clear_word = remove_puct(word)
        all_words.append(clear_word.lower())
    y = list(set(all_words))
    print(y)
if op == 1:
    print(longest_word())
if op == 2:
    print(most_com_word())
if op == 3:   
    print(slovnuk())
