# 풀이 3 - 일정 그래프 반복
import collections


def findItinerary(tickets: list[list[str]]) -> list[str]:
    dic = collections.defaultdict(list)
    for a, b in sorted(tickets):    # 사전 어휘 순 저장
        dic[a].append(b)

    # 재귀가 아닌 스택으로 반복 처리
    # 한 번 방문했던 곳을 다시 방문하지 않으려면 스택의 pop()으로 제거하는 방법을 이용
    # 경로가 끊어지는 경우를 대비하여 스택의 값을 다시 pop()하여 거꾸로 풀어낼 수 있는 변수를 마련
    route, stack = [], ['JFK']
    while stack:
        while dic[stack[-1]]:
            stack.append(dic[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
# but it is larger in lexical order.
