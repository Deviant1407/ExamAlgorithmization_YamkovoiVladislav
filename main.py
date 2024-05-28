# Билет 22
import math


class Calc:
    def __init__(self, len_nums):
        self.len_nums = len_nums


    def Calculete(self):

        Num_list = []
        for i in range(self.len_nums):
            Num_list.append(int(input("Введите число: ")))

        SR = sum(Num_list) / len(Num_list)
        F_SR = math.floor(SR)
        C_SR = math.ceil(SR)

        return [F_SR, SR, C_SR]


Calc1 = Calc(int(input("Количество чисел: ")))
Result = Calc1.Calculete()
print(f'{Result[0]} {Result[1]} {Result[2]}')

