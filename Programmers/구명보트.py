def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1

    cnt = 0
    while left <= right:
        cnt += 1
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1

    return cnt