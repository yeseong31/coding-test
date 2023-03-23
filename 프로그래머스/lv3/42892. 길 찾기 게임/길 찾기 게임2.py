def preorder(x, y, result):
    node = y[0]
    idx = x.index(node)
    left, right = [], []

    for i in range(1, len(y)):
        if node[0] < y[i][0]:
            left.append(y[i])
        else:
            right.append(y[i])

    result.append(node[2])
    if len(right) > 0:
        preorder(x[:idx], right, result)
    if len(left) > 0:
        preorder(x[idx + 1:], left, result)


def postorder(x, y, result):
    node = y[0]
    idx = x.index(node)
    left, right = [], []

    for i in range(1, len(y)):
        if node[0] < y[i][0]:
            left.append(y[i])
        else:
            right.append(y[i])

    if len(right) > 0:
        postorder(x[:idx], right, result)
    if len(left) > 0:
        postorder(x[idx + 1:], left, result)
    result.append(node[2])


def solution(nodeinfo):
    nodeinfo = [(*v, i + 1) for i, v in enumerate(nodeinfo)]
    x = sorted(nodeinfo)
    y = sorted(nodeinfo, key=lambda k: -k[1])

    pre, post = [], []
    preorder(x, y, pre)
    postorder(x, y, post)

    return pre, post
