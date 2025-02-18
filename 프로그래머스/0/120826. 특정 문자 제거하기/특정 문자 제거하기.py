def solution(my_string, letter):
    answer = [] 
    my_list = list(my_string) # 문자열을 리스트로 변환
    for i in range(0, len(my_list)):
        if my_list[i] != letter:
            answer.append(my_list[i])
        else:
            continue
    end = ''.join(answer) # 다시 리스트를 문자열로 변환
    return end