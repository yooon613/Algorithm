def solution(arr):
    answer = 0
    answer = sum(map(int, arr))
    answer = answer / len(arr)
    return answer