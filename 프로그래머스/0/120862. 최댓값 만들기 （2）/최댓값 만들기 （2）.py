def solution(numbers):
    answer =0
    s = sorted(numbers)
    a = s[0]*s[1]
    b = s[-1]*s[-2]
    answer = max(a, b)
    return answer