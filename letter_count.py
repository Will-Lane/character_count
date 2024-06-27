# wget https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt

import string
from operator import itemgetter

min_length = 4
max_length = 6

def get_words(a, b):
    with open('words_alpha.txt') as f:
        all_words = f.read().splitlines()
        words_4_5_6 = ([i.upper() for i in all_words if len(i)>= a and len(i) <= b])
        return words_4_5_6
    
words = get_words(min_length,max_length)
words.sort()
print(words)

alpha = string.ascii_uppercase

print(alpha)


for wordlen in range(min_length, max_length+1):
    print(f'Count for {wordlen} letter words!')
    worddict = {idx : {letter : set() for letter in alpha} for idx in range(wordlen)}

    for word in words:
        if len(word) == wordlen and all(letter in alpha for letter in word):
            for idx, letter in enumerate(word):
                worddict[idx][letter].add(word)

    lens = [[(len(worddict[idx][letter]), idx, letter) for letter in worddict[idx]] for idx in worddict]


    for item in lens:
        sort = sorted(item,key=itemgetter(0), reverse=True)
        top_5 = sort[:5]
        # print(top_5)
        rank=1
        for num, idx, letter in top_5:
            print(f"Position: {idx+1}    Letter: {letter}    Total: {num}    Rank: {rank}")
            rank+=1