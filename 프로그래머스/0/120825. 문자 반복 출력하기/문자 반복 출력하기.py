def solution(my_string, n):
    answer = []
    str_list = list(my_string)
    
    for i in range(0, len(my_string)):
        answer.append(str_list[i]*n)
    end = ''.join(answer)
    return end