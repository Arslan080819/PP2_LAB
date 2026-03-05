import math

length = float(input("Ұзындығы: "))
width = float(input("Ені: "))

perimeter = 2 * (length + width)
divided_by_3 = perimeter / 3
ceil_value = math.ceil(divided_by_3)



print(f"{perimeter:.2f}")
print(f"{divided_by_3:.2f}")
print(f"{ceil_value}")

