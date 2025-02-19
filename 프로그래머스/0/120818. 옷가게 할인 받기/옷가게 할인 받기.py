def solution(price):
    
    if price >= 500000: #조건문의 순서 주의
        return int(price*0.8) # 정수를 리턴하라고 했으므로 int 변환해줘야 함
    elif price >=300000:
        return int(price*0.9)
    elif price>=100000:
        return int(price*0.95)
    else: #10만원 이하는 할인 없음
        return price
        