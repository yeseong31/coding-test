"""
조이스틱
https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""


def solution(name):
    cnt = 0
    n = len(name)
    step = n - 1

    # 기본 진행 방향은 '오른쪽'
    for i, v in enumerate(name):
        cnt += min(int(ord(v)) - int(ord('A')), int(ord('Z')) - int(ord(v)) + 1)
        # 다음 A의 위치를 파악함
        p = i + 1
        while p < n and name[p] == 'A':
            p += 1
        # 오른쪽, 왼쪽→오른쪽→오른쪽, 오른쪽→왼쪽→왼쪽 비교
        step = min(step, 2 * i + n - p, i + 2 * (n - p))

    return cnt + step


'''
def solution(name):
    def check(i: int, arr: list) -> int:
        left_idx, right_idx = i - 1, i + 1
        step_left = step_right = 1

        if left_idx < 0:
            left_idx = len(arr) - 1
        if len(arr) <= right_idx:
            right_idx = 0

        # 왼쪽 확인
        while left_idx != i and arr[left_idx] == 'A':
            left_idx = left_idx - 1 if left_idx > 0 else len(arr) - 1
            step_left += 1
        # 오른쪽 확인
        while right_idx != i and arr[right_idx] == 'A':
            right_idx = right_idx + 1 if right_idx < len(arr) - 1 else 0
            step_right += 1

        print(f'left_idx: {left_idx}, right_idx: {right_idx}')
        print(f'step_left: {step_left}, step_right: {step_right}')

        if step_left < step_right:
            return -step_left
        return step_right

    # 이미 'A'로만 이루어진 문자열이라면 return
    if name == 'A' * len(name):
        return 0

    cnt = 0
    idx = 0
    target = list(name)
    while True:
        print('------------------------------')
        print(f'현재 target: {target}')
        print(f'idx: {idx}')
        print(f'cnt: {cnt}')
        # 현재 위치한 문자를 'A'로 변환
        if target[idx] < 'N':
            cnt += int(ord(target[idx])) - int(ord('A'))
        else:
            cnt += int(ord('Z')) - int(ord(target[idx])) + 1
        target[idx] = 'A'
        # 변환 완료 시 종료
        if target == ['A'] * len(target):
            return cnt
        # 좌우로 A의 길이를 파악하여 더 짧은 곳으로 이동
        step = check(idx, target)
        if step < 0:
            for _ in range(abs(step)):
                idx -= 1
                if idx < 0:
                    idx = len(name) - 1
        else:
            for _ in range(abs(step)):
                idx += 1
                if idx >= len(name):
                    idx = 0
        cnt += abs(step)
'''

print(solution("AJAANA"))
print(solution("JAN"))
