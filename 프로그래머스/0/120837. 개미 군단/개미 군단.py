#그리디 알고리즘(탐욕법으로 해결)
def solution(hp):
    answer = 0
    answer = answer+(hp//5) # 장군개미 사용
    hp = hp%5
    
    answer = answer+(hp//3) #병정개미 사용
    hp = hp%3
    
    answer = answer+hp
    return answer