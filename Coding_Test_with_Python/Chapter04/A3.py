input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)

# 조금 더 까다롭게 문제를 출제한다면 입력 문자가 열과 행이 아닌 1a와 같은 행과 열 형태로 들어왔을 때의 예외 처리를 요구할 수도 있다.
# 이런 다양한 구현 유형에 대비하기 위해서 파이썬 문법을 자유롭게 사용할 수 있도록 훈련하는 것이 중요하다.
