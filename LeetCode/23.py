# Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')

        answer = []
        for current in path.split('/'):
            if current == '..':
                if answer:
                    answer.pop()
            elif current == '.' or current == '':
                continue
            else:
                answer.append(f'/{current}')

        if len(answer) == 0:
            return '/'
        return ''.join(answer)
