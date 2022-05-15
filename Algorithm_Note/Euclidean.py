"""
유클리드 호제법
- 최대공약수를 구하는 알고리즘
- 두 수 a와 b가 있을 때 a를 b로 나눈 값 mod가 0이 아니라면
  b를 a로, mod를 b로 설정하여 위의 과정을 반복
  최종적으로 mod가 0이 나온다면 그때의 b가 최대공약수가 됨
"""


def euclidean(a, b):
    while True:
        div, mod = divmod(a, b)
        if mod == 0:
            return b
        a, b = b, mod


print(euclidean(78696, 19332))
