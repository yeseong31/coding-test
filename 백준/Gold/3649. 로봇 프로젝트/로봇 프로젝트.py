import sys
input = sys.stdin.readline

TARGET_SIZE = int(1e7)

while True:
    try:
        x = int(input()) * TARGET_SIZE
        n = int(input())
        legos = sorted([int(input()) for _ in range(n)])
        
        left, right = 0, len(legos) - 1
        l1 = l2 = -1
        check = False
        
        while left < right:
            _sum = legos[left] + legos[right]
            if _sum == x:
                print(f'yes {legos[left]} {legos[right]}')
                check = True
                break
            if _sum < x:
                left += 1
            else:
                right -= 1
                
        if not check:
            print('danger')
    except:
        break
