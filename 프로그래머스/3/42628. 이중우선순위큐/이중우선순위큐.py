from heapq import heappush, heappop, heapify, nsmallest


def solution(operations):
    max_heap = []
    min_heap = []
    count = 0
    
    for operation in operations:
        op, num_str = operation.split()
        num = int(num_str)
        
        if op == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
            count += 1
            
        if count == 0:
            continue
        
        if op == 'D':
            if num == 1:
                heappop(max_heap)
                min_heap = nsmallest(len(max_heap), min_heap)
                heapify(min_heap)
                count -= 1
            elif num == -1:
                heappop(min_heap)
                max_heap = nsmallest(len(min_heap), max_heap)
                heapify(max_heap)
                count -= 1
                
            if count == 0:
                max_heap.clear()
                min_heap.clear()
    
    if count == 0:
        return 0, 0
    
    return -max_heap[0], min_heap[0]
