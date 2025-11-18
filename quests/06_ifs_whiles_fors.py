# 문제 1 문자열 포맷 오류 수정하기
second = "Programming"
first = f"Welcome to Python Strings {second}"

print(first)

# 문제 2 while 조건 오류 찾기
first = "Hello Python" 
# 수정된 코드
first = 5

while first > 0:   # 문자열과 정수 비교 불가
    print(first)
    first = first - 1  # 문자열에서 1을 뺄 수 없음

# 문제 3 리스트 누적 합 오류 찾기
kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum_all = 0

for k in kor:
    sum_all = sum_all + k

# 문제 4 for-range 인덱스 문제 해결
kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum_total = 0

for i in range(5):
    sum_total = sum_total + kor[i] + eng[i]