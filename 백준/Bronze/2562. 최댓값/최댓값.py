n = []
for i in range(9):
    n.append(int(input()))
print('{}\n{}'.format(max(n), n.index(max(n))+1))
