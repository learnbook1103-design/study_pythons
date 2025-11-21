# class class_name():
#     # 속성(변수)

#     # 메서드(함수)
class FourCal():
    def __init__(self):
        pass
    def add(self, a, b):
        return self.first + self.second

    def sub(self, a, b):
        return self.first - self.second

    def mul(self, a, b ):
        return self.first * self.second

    def div(self, a, b):
        if self.second == 0:
            return "0으로 나눌 수 없습니다."
        return self.first / self.second

if __name__ == "__main__":
    cal = FourCal()
    print(f"3 + 5 = {cal.add(3, 5)}")
    print(f"10 - 4 = {cal.sub(10, 4)}")
    print(f"6 * 7 = {cal.mul(6, 7)}")
    print(f"20 / 4 = {cal.div(20, 4)}")