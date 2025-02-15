def solution(t, p):
    count =0
    length = len(p)
    
    for i in range(len(t)- length +1):
        a = t[i:length+i]
        if int(a)<=int(p):
            count+=1
    
    return count  