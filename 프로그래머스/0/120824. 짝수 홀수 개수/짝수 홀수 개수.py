def solution(num_list):
    answer = []
    a =0
    b =0
    
    for i in range (len(num_list)):
        if num_list[i]%2 ==0:
            a+=1
        elif num_list[i]%2!=0:
            b+=1
    answer.append(a)
    answer.append(b)
    return answer