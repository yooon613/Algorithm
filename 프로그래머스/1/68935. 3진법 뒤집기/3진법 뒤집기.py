def solution(n):
    answer = 0
    t = ''
    
    
    while n>0:
        a = n%3
        n = n//3
        t += str(a)
    
    answer = int(t, 3)
    return answer