def solution(array):
    answer = 0
    num = len(array)//2
    s_array = sorted(array)
    answer = s_array[num]
    return answer