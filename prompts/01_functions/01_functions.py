def calculate_all(num1, num2):
    """
    두 개의 숫자를 받아 사칙연산을 수행하고 결과를 튜플로 반환합니다.
    0으로 나눌 경우, 나눗셈 결과는 'division_error' 문자열을 반환합니다.
    """
    add_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2
    
    if num2 == 0:
        div_result = 'division_error'
    else:
        div_result = num1 / num2
        
    return (add_result, sub_result, mul_result, div_result)

# 테스트 데이터
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 실행 로직
print("사칙연산 결과:")
for i in range(len(test_a)):
    a = test_a[i]
    b = test_b[i]
    results = calculate_all(a, b)
    print(f"입력: a={a}, b={b}")
    print(f"  덧셈: {results[0]}")
    print(f"  뺄셈: {results[1]}")
    print(f"  곱셈: {results[2]}")
    print(f"  나눗셈: {results[3]}")
    print("-" * 20)
