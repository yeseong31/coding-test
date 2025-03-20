from datetime import datetime, timedelta


def convert_time(time_str):
    time_str = f'{time_str:04d}'
    target_time = datetime.strptime(time_str, '%H%M')
    return target_time.strftime('%H%M')
    
def get_deadline_time(time_str):
    deadline = datetime.strptime(time_str, '%H%M') + timedelta(minutes=10)
    return deadline.strftime('%H%M')


def solution(schedules, timelogs, startday):
    answer = 0
    startday -= 1
    
    for schedule, timelog in zip(schedules, timelogs):
        scuedule_time = convert_time(schedule)
        deadline = get_deadline_time(scuedule_time)
        
        count = 0
        for day, log in enumerate(timelog, startday):
            day %= 7
            if day >= 5:
                continue
            
            if convert_time(log) <= deadline:
                count += 1
                
        if count == 5:
            answer += 1
    
    return answer