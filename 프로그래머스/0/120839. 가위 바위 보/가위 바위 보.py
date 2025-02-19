def solution(rsp):
    answer = []
    r_list = list(rsp)
    for i in range(0, len(r_list)):
        if r_list[i] == "2":
            answer.append("0")
        elif r_list[i] == "0":
            answer.append("5")
        elif r_list[i] == "5":
            answer.append("2")
    pp = ''.join(answer)
    return pp