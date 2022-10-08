import math

x, y = int(input()), int(input())
print(f'{round(math.degrees(math.atan2(x, y)))}' + '\u00b0')
