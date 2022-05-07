def solution(s):
    # 결과: 압축된 문자열의 최소 길이
    result = len(s)

    # 자르는 문자열의 길이는 1부터 최대 s의 길이의 절반
    for n in range(1, len(s) // 2 + 1):
        # 토큰화 된 문자열을 비교하기 위해 변수 선언
        prev, sub = '', ''
        # 문자열 시작 인덱스, 중복 카운트(초기값 1)
        idx, cnt = 0, 1

        # 문자열 토큰화
        while idx <= len(s):
            token = s[idx:idx + n]

            # 토큰화 된 문자열이 이전 문자열과 같은 경우 카운트 +1
            if token == prev:
                cnt += 1

            # 그렇지 않으면 결과 문자열에 추가 및 카운트 초기화
            elif cnt == 1:
                sub += token
            else:
                sub += str(cnt) + token
                cnt = 1

            # 이전 문자열 초기화
            prev = token
            idx += n

        # 반복문 이후 남은 문자열에 대한 처리
        sub += s[idx:]
        result = min(result, len(sub))

    return result