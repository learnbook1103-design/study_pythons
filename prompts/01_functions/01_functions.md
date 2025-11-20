```{
  "task": "python_arithmetic_implementation",
  "description": "두 개의 숫자 리스트를 받아 사칙연산을 수행하는 함수 구현 및 결과 출력",
  "requirements": {
    "function_name": "calculate_all",
    "naming_convention": "snake_case (소문자 + _)",
    "return_format": "tuple (덧셈, 뺄셈, 곱셈, 나눗셈)",
    "error_handling": {
      "condition": "division by zero (0으로 나누기)",
      "action": "return 'division_error'"
    },
    "data_processing": "제공된 두 리스트(test_a, test_b)를 인덱스별로 순회하며 처리"
  },
  "code_context": {
    "template": "def calculate_all(num1, num2):\n    # TODO: 사칙연산 구현\n    # return (add, sub, mul, div)\n    pass\n\n# 테스트 데이터\ntest_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]\ntest_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]\n\n# 실행 로직\nfor i in range(len(test_a)):\n    # TODO: 함수 호출 및 결과 출력\n    pass"
  },
  "prompt_message": "위의 requirements와 code_context를 바탕으로 Python 코드를 완성해줘. 특히 0으로 나누는 경우의 예외 처리를 정확히 구현해야 해."
}
```