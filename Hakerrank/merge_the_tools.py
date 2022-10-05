def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        target = string[i:i+k]
        print(''.join(dict.fromkeys(target)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)