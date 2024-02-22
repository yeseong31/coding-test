from heapq import heappush, heappop


def find_mid_numbers(numbers):
    mid = numbers[0]
    result = [mid]
    min_heap, max_heap = [], []

    for index, number in enumerate(numbers[1:], 1):
        if number < mid:
            heappush(max_heap, -number)
        else:
            heappush(min_heap, number)

        if index % 2 == 1:
            continue

        if len(min_heap) < len(max_heap):
            heappush(min_heap, mid)
            mid = -heappop(max_heap)
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -mid)
            mid = heappop(min_heap)

        result.append(mid)

    return result


for _ in range(int(input())):
    m = int(input())
    numbers = []

    for i in range(m // 10 + 1):
        numbers.extend(list(map(int, input().split())))

    print(m // 2 + 1)
    
    for i, v in enumerate(find_mid_numbers(numbers)):
        if i != 0 and i % 10 == 0:
            print()
        
        print(v, end=' ')
    
    print()
