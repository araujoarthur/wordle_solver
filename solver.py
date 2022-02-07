from collections import Counter

word_list = list()
with open('D:\\Users\\arthu\\Documents\\Bookservice\\sgb-words.txt') as words:
    for word in words:
        eval_word = word.rstrip('\n').replace('.','').replace(',','').replace('/','').replace('-','').replace('\'','').upper()
        if len(eval_word) == 5 and not(eval_word in word_list):
            word_list.append(eval_word)
    print(len(word_list))
 
alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
solver = list()
log = list()

for word in word_list:
    split_word = list(word.upper())
    remove_letters = list()
    _isin_or_hasdup = False
    for letter in split_word:
        if Counter(split_word)[letter]>1:
            _isin_or_hasdup = True;
        if not letter in alphabet:
            _isin_or_hasdup = True;
            break
        else:
            remove_letters.append(letter)
    if _isin_or_hasdup:
        continue
    else:
        solver.append(word.upper())
        for letter in remove_letters:
            alphabet.pop(alphabet.index(letter))
            print(alphabet,len(alphabet))
print(solver)
