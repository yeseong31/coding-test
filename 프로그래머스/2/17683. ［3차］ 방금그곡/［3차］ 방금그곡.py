from math import ceil


def solution(m, musicinfos):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])
    
    answer = None
    sharp = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    
    for sh in sharp:
        m = m.replace(sh, sharp[sh])

    for info in musicinfos:
        start, end, title, melody = info.split(',')
        
        for sh in sharp:
            melody = melody.replace(sh, sharp[sh])
            
        start, end = convert(start), convert(end)
        length = end - start
        melody *= ceil(length / len(melody))
        
        if m not in melody[:length]:
            continue
            
        if answer is None or answer[1] < length or (answer[1] == length and answer[2] > start):
            answer = (title, length, start)
    
    return answer[0] if answer is not None else '(None)'
