# def to_celsius_list(temps):
#     celsius_list = []
#     for t in temps:
#         c = (t - 32) * 5 / 9
#         celsius_list.append(round(c, 1))
#     return celsius_list

# # 테스트 데이터
# temp_lists = [
#     [32, 212],       # 0도, 100도
#     [77, 95, 50],    # 랜덤 온도
#     [100, 0, -40]    # 고온/저온
# ]

# print("\n--- 문제 5 실행 결과 ---")
# for temps in temp_lists:
#     result = to_celsius_list(temps)
#     print(f"화씨 {temps} -> 섭씨 {result}")


def dummy_function(name):
    dummy_result = f"Hello, {name}!"
    return dummy_result
print(dummy_function("World"))