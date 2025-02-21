def solution(s):
    answer = s.split(" ")
    result =[]
    
    for word in answer:
        new_word ="" # 새로운 단어 만들기
        for i in range(0, len(word)):    
            if i % 2 ==0:
                new_word+=word[i].upper()
            else:
                new_word+=word[i].lower()
        result.append(new_word)
                
    ss = ' '.join(result)
            
    return ss