if __name__ == '__main__':
    n = int(raw_input())
    numbers = raw_input().strip().split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    T = tuple(numbers)
    print hash(T)
