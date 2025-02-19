def solution(n):
    answer = 0
    n_str = str(n)
    for i in range(0, len(n_str)):
        answer+=int(n_str[i])
        
    return answer