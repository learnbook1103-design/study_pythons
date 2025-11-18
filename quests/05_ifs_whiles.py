# 문제 1 변수 이름 오류 찾기

first = 5

while   first> 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제 2 들여쓰기(Indentation) 오류 찾기

first = 5

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1

# 문제 3 논리적 오류(조건문) 찾기
first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first == 3:
        print("break 실행.")
        break
    first = first - 1