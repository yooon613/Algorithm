def solution(my_string):
    answer = []
    my_list= list(my_string)
    
    for i in range(0, len(my_list)):
        if my_list[i] == 'a':
            continue
        elif my_list[i] == 'e':
            continue
        elif my_list[i] == 'i':
            continue
        elif my_list[i] == 'o':
            continue
        elif my_list[i] == 'u':
            continue
        else:
            answer.append(my_list[i]) 
    
    pp = ''.join(answer)
    return pp