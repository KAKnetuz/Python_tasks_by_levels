# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
num1 = abs(int(input("Введите первое число: ")))
num2 = abs(int(input("Введите второе число: ")))


def get_first_digit(num):
    while num >= 10:
        num //= 10
    return num


first_digit1 = get_first_digit(num1)
first_digit2 = get_first_digit(num2)

if first_digit1 == first_digit2:
    print("Первые цифры совпадают")
else:
    print("Первые цифры не совпадают")

"""ИЛИ
num1 = abs(int(input("Введите первое число: ")))
num2 = abs(int(input("Введите второе число: ")))

first_digit1 = str(num1)[0]
first_digit2 = str(num2)[0]

if first_digit1 == first_digit2:
    print("Первые цифры совпадают")
else:
    print("Первые цифры не совпадают")"""