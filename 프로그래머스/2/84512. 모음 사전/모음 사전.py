def solution(word):
    dictionary = []
    vowels = ('A', 'E', 'I', 'O', 'U')
    make_dictionary('', vowels, dictionary)
    return dictionary.index(word) + 1


def make_dictionary(target, vowels, dictionary):
    if len(target) == 5:
        return
    
    for c in vowels:
        word = target + c
        dictionary.append(word)
        make_dictionary(word, vowels, dictionary)
