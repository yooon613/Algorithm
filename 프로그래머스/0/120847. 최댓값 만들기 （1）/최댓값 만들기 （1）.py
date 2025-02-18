def solution(numbers):
    answer = 0
    a = []
    a = sorted(numbers, reverse = True)
    answer = a[0] *a[1]
    return answer