# 일일 온도(252p)

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    q = []
    answer = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        # 큐가 비어 있거나, 큐의 숫자가 현재 숫자보다 작을 경우
        while q and q[-1][1] < t:
            now = q.pop()[0]
            answer[now] = i - now
        q.append((i, t))

    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))

temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))

temperatures = [30, 60, 90]
print(dailyTemperatures(temperatures))
