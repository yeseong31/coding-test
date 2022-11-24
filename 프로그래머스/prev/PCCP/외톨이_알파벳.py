from collections import defaultdict


def solution(input_string):
    answer = set()
    dic = defaultdict(int)
    left = 0
    
    for right in range(len(input_string) + 1):
        if right == len(input_string):
            dic[input_string[left]] += 1
            break
        if input_string[left] != input_string[right]:
            dic[input_string[left]] += 1
            left = right
    
    for k in dic:
        if dic[k] > 1 and k not in answer:
            answer.add(k)
    
    return ''.join(sorted(answer)) if answer else 'N'


input_string = "eeddee"
print(solution(input_string))
