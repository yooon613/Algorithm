def gcd(a, b):
    while b:
        a, b = b, a%b

    return a
    
def solution(n, m):
    answer = []
    gcd_v = gcd(n, m)
    answer.append(gcd_v)
    lcm_v = (n*m)//gcd_v
    answer.append(lcm_v)
    
    
    return answer