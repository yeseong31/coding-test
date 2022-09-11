import collections


def solution(input_string):
    dic = collections.defaultdict(int)
    left = right = 0
    while left <= right < len(input_string):
        # 단어 뭉치 확인
        while right < len(input_string) and input_string[left] == input_string[right]:
            right += 1
        # 탐색 알파벳 저장
        dic[input_string[left]] += 1
        # 탐색 위치 초기화
        left = right
    # 외톨이 알파벳 확인
    answer = set()
    for d in dic.keys():
        if dic[d] >= 2:
            answer.add(d)
    # 결과
    if not answer:
        return 'N'
    return ''.join(sorted(answer))


input_string = "eeddee"
print(solution(input_string))
