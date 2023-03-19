def counting_sort(data, digit):
    """
    계수 정렬
    데이터가 숫자만으로 이루어져 있고 그 숫자들이 크지 않다면 사용할 수 있는 정렬 방식
    
    :param data:
    - 정렬하고자 하는 데이터
    :param digit:
    - 확인할 자릿수
    """
    n = len(data)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = data[i] // digit
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = data[i] // digit
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1
    
    data[:] = output
    

def radix_sort(data):
    """
    기수 정렬
    자릿수별로 계수를 비교하여 정렬 수행
    
    :param data:
    - 정렬하고자 하는 데이터
    :return:
    - 정렬된 data
    """
    digit = 1
    while max(data) // digit > 0:
        counting_sort(data, digit)
        digit *= 10
    

sample = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(sample)
print(sample)
