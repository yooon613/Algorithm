def solution(array, height):
    answer = 0
    for i in range(0, len(array)):
        if height<array[i]:
            answer+=1
        else:
            continue
            
    return answer