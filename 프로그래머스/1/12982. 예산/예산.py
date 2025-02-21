def solution(d, budget):
    answer = 0
    d_s = sorted(d)
    for i in range(0, len(d_s)):
        if d_s[i]<=budget:
            answer+=1
            budget-=d_s[i]
        else:
            return answer
    return answer