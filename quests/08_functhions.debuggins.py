# 문제 1 return 누락 오류
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius

result = to_celsius(77)
print(result)

# 문제 2 매개변수 이름 오류
def convert(temp):
    return (temps - 3) * 5 / 9   # 오타: temps
    return (temp - 3) * 5 / 9   # 수정된 코드
print(convert(95))

# 문제 3 함수 호출 인자 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9

value = to_celsius()   # temp 인자가 빠졌습니다.
value = to_celsius(50) # 올바른 인자 호출
print(value)

#문제 4 타입 오류(TypeError)
def to_celsius(temp):
    return (temp - 32) * 5 / 9

print(to_celsius("100F"))  # 문자열 인자 오류
print(to_celsius(100))     # 올바른 인자 호출

# 문제 5 반복 구조 + 함수 사용 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9

temps = [77, 95, 50]
results = []

for t in temps:
    # result = to_celsius(temp)   # 잘못된 변수 이름 사용
    results = results + [to_celsius(t)]  # 올바른 변수 이름 사용
print(results)

## for문의 함수화
def to_celsius(temp):
    return (temp - 32) * 5 / 9

temps = [77, 95, 50]

def convert_temps(temps):
    results = []
    for t in temps:
        results = results + [to_celsius(t)]
    return results
result_fin = convert_temps(temps)
print(result_fin)
