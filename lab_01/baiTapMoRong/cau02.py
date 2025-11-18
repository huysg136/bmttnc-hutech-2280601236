import re

s = input("Nhập chuỗi: ")
numbers = re.findall(r'-?\d+', s)
numbers = [int(num) for num in numbers]

sum_positive = sum(num for num in numbers if num > 0)
sum_negative = sum(num for num in numbers if num < 0)

print("Tổng các số dương là:", sum_positive)
print("Tổng các số âm là:", sum_negative)