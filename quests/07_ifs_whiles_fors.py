# 문제 1 문자열과 f-string 활용
second = "Python is fun."

if "Python" in second:
    print(f"Welcome! {second}")

# 문제 2 while 반복문 응용
first = 5
while first > 0:
    if first == 2:
        print("special")
        first -= 1
    else:
        print(f"Current value: {first}")
        first -= 1

# 문제 3 리스트 합계 및 평균 계산
kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
total_score = []
avg_score = []  
# 1. 각 학생 점수의 총합
for i in range(5):
    total = kor[i] + eng[i]
    total_score.append(total)
print(f"total_score= {total_score}")
    
# 2. 전체 점수의 평균
for i in range(5):
    avg = (kor[i] + eng[i]) / 2
    avg_score.append(avg)
print(f"avg_score= {avg_score}")    

# 문제 4 누적 합과 조건문 결합
kor = [70, 80 ,90, 40, 50]							# 리스트 선언
sum = 0 
for i in range(5):
    if kor[i] >= 60 :
       sum = sum+ kor[i]
print(f"누적합= {sum}")