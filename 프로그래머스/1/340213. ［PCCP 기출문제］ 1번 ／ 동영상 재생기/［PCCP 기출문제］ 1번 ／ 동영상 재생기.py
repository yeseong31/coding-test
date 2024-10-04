def solution(video_len, pos, op_start, op_end, commands):
    # 초 단위 숫자로 변환
    video_len = _convert_to_seconds(video_len)
    pos = _convert_to_seconds(pos)
    op_start = _convert_to_seconds(op_start)
    op_end = _convert_to_seconds(op_end)
    
    # 시작 위치가 오프닝 구간이면 오프닝 종료 위치로 이동
    if op_start <= pos <= op_end:
        pos = op_end
    
    # 사용자 입력 확인
    for command in commands:
        if command == 'prev':
            pos = pos - 10 if pos >= 10 else 0
        if command == 'next':
            pos = pos + 10 if pos < video_len - 10 else video_len
        if op_start <= pos <= op_end:
            pos = op_end
    
    # 현재 위치를 'mm:ss' 형식으로 변환
    return f'{pos//60:02d}:{pos%60:02d}'


def _convert_to_seconds(time_str):
    minute, second = map(int, time_str.split(':'))
    return minute * 60 + second
