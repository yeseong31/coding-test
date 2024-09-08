def is_available_seat(place: list, x: int, y: int, dx: tuple, dy: tuple) -> bool:
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        if i % 2 == 0:
            if place[nx][ny] == 'P':
                return False
            else:
                continue

        if place[nx][ny] != 'P':
            continue

        lnx, lny = x + dx[i - 1], y + dy[i - 1]
        rnx, rny = x + dx[(i + 1) % 8], y + dy[(i + 1) % 8]

        if place[lnx][lny] in ('O', 'P'):
            return False
        if place[rnx][rny] in ('O', 'P'):
            return False

    for i in range(0, 8, 2):
        nx, ny = x + dx[i], y + dy[i]
        dnx, dny = x + dx[i] * 2, y + dy[i] * 2

        if dnx < 0 or dnx >= 5 or dny < 0 or dny >= 5 or place[dnx][dny] != 'P':
            continue

        if place[nx][ny] != 'X':
            return False

    return True


def check(place: list, dx: tuple, dy: tuple) -> int:
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            if not is_available_seat(place, i, j, dx, dy):
                return False

    return True


def solution(places):
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
    return [int(check(place, dx, dy)) for place in places]
