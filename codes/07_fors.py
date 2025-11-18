kor = [70, 80 ,90, 40, 50]							# 리스트 선언
eng = [90, 80 ,70, 70, 60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0				    # 누적 변수 초기화

# # for 단일변수 in 리스트:
# #     실행문

# for score in kor:									# 국어 점수 출력 및 합계 계산
#     print(score, end=' ')
#     sum1 += score    
# print(f"\n국어 합계 : {sum1}")

# for score in eng:									# 영어 점수 출력 및 합계 계산
#     print(score, end=' ')
#     sum2 += score    
# print(f"\n영어 합계 : {sum2}")

# range(5) -> [0, 1, 2, 3, 4]
for index in range(5):								# 인덱스 이용한 합계 계산
    # kor[index] + eng[index]
    sum3 = kor[index] + eng[index] + sum3
print(f"\n국어+영어 누적값 : {sum3}")