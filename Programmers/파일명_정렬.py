def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        flag = True
        for i, v in enumerate(file):
            if flag and (v.isalpha() or v in ['-', ' ', ',']):
                head += v
            elif v.isdigit():
                flag = False
                number += v
            else:
                tail += file[i:]
                break
        answer.append([head, number, tail])

    return [''.join(v) for v in sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
