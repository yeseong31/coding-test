def solution(word):
    def make_dictionary(current_word, result):
        result.append(current_word)
        
        if len(current_word) == 5:
            return
    
        for vowel in vowels:
            make_dictionary(current_word + vowel, result)
    
    
    vowels = ('A', 'E', 'I', 'O', 'U')
    result = []
    make_dictionary('', result)
    return result.index(word)
