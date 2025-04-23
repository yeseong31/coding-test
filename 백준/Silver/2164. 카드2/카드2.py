lst = list(range(1, int(input()) +1))
while True:
    length = len(lst)
    if length <= 2:
        print(lst[-1])
        break
    if length % 2 == 0:
        lst = [lst[i] for i in range(length) if i % 2 == 1]
    else:
        lst = [lst[-1]] +[lst[i] for i in range(length) if i % 2 == 1]
# 배열 원소의 수가 홀수이면... [맨끝 + 짝수번 인덱스들]
# 배열 원소가 짝수이면...[짝수번 인덱스들]
# 배열 원소가 짝수이면서 길이가 2라면... return 배열[1]