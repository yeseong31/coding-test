# find() 메서드
# 첫 번째 매개변수: 찾을 문자
# 두 번째 매개변수: 탐색 시작 위치
# 반환값: 해당 문자 인덱스 (없으면 -1)
s = 'abcdefghijklmnopqrstuvwxyz'
print(s.find('i'))

# -----------------------------------------------------------------------
# startswith() 메서드
# 첫 번째 매개변수: 시작하는 문자
# 두 번째 매개변수: 시작 지점
# 반환값: True/False
s = 'abcdefghijklmnopqrstuvwxyz'
print(s.startswith('m'))    # 문자열 s는 'a'로 시작하므로 False 반환

# -----------------------------------------------------------------------
# endswith() 메서드
# 첫 번째 매개변수: 끝나는 문자
# 두 번째 매개변수: 문자열의 시작
# 세 번째 매개변수: 문자열의 끝
# 반환값: True/False
s = 'abcdefghijklmnopqrstuvwxyz'
print(s.endswith('z'))    # 문자열 s는 'z'로 끝나므로 True 반환
