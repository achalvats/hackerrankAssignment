def runner_up(n, arr):
    high = arr[0]
    low = arr[0]
    for i in range(n):
        if arr[i] > high:
            high = arr[i]
        if arr[i] < low:
            low = arr[i]
    second_high = low
    for j in range(n):
        if arr[j] > second_high and arr[j] < high: second_high = arr[j]

    # print(high)
    print(second_high)
    # return second_high


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runner_up(n, arr)
