import collections


def solution(gems):
    left = 0
    kind = len(set(gems))
    length = len(gems)

    answer = 0, length
    counter = collections.Counter()

    for right in range(length):
        counter[gems[right]] += 1
        while len(counter) == kind:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            if right + 1 - left < answer[1] - answer[0]:
                answer = left, right + 1

    return answer


gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))


# 효율성 테스트: 시간 초과
# def solution(gems):
#     kind = set(gems)
#     length = len(gems)
#
#     answer = [0, length]
#     left = 0
#
#     for right in range(1, length + 1):
#         target = gems[left:right]
#
#         if set(target) == kind:
#             while set(target) == kind:
#                 left += 1
#                 target = gems[left:right]
#             if answer[1] - answer[0] > right - left:
#                 answer[0] = left
#                 answer[1] = right
#
#     return answer
