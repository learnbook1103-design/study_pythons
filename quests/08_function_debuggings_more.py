# 문제 6 함수 내부 변수 오타
def to_celsius(temp):
    celsiu = (temp - 32) * 5 / 9   # 오타
    celsius = (temp - 32) * 5 / 9   # 수정된 코드
    return celsius
print(to_celsius(77))

#문제 7 return 위치 오류
def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
    return    # 잘못된 위치
        celsius
    return celsius  # 수정된 코드
print(to_celsius(95))

# # 문제 8 함수 재사용 시 논리 오류
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95
result2 = to_celsius()  # 인자 누락
result2 = to_celsius(temp)  # 수정된 코드

temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3)

# 문제 9 리스트 값 변환 시 타입 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9

temps = [77, 95, 50] 

value = to_celsius(temps)  # 리스트 전체를 인자로 전달
value = [to_celsius(t) for t in temps]  # 수정된 코드
print(value)

# 문제 10 함수 반환값을 활요한 조건문 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9
if to_celsius > 20:  # 함수 호출 누락
if to_celsius(77) > 20:  # 수정된 코드
    print("warm")
else:
    print("cold")