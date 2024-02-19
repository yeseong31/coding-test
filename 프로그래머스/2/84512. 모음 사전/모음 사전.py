def make_dictionary(current_word, vowels, result):
    result.append(current_word)

    if len(current_word) == 5:
        return

    for vowel in vowels:
        make_dictionary(current_word + vowel, vowels, result)


def solution(word):
    result = []
    vowels = ('A', 'E', 'I', 'O', 'U')
    make_dictionary('', vowels, result)
    
    return result.index(word)
