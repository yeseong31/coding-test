def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) // 2 + 1):
        result = 0
        # 중복 카운트
        count = 1
        # 이전 문자
        prev = ''

        # 길이 n씩 자르면서 확인
        for i in range(0, len(s) + 1, n):
            word = s[i:i+n]
            # 이전에 등장한 문자라면 중복 카운트
            if prev == word:
                count += 1
            # 새로운 문자라면 result에 반영
            elif prev != '':
                if count != 1:
                    result += len(str(count))
                result += len(prev)
                count = 1
            
            prev = word
            i += n
        
        if count != 1:
            result += len(str(count))
        
        result += len(prev)
        answer = min(answer, result)
    
    return answer
