# 첫 번째 숫자가 두 번째 숫자의 약수라면 'factor'

def check(a, b, c):
    if a and not b:
        if c == 0:
            print('multiple')
        elif c == 1:
            print('factor')
    else:
        print('neither')


while True:
    a, b = map(int, input().split())
    if not a or not b:
        break
    if a > b:
        div, mod = divmod(a, b)
        check(div, mod, 0)
    else:
        div, mod = divmod(b, a)
        check(div, mod, 1)

