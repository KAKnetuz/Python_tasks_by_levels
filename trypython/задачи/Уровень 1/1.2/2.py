# Дано число. Выведите в консоль последнюю цифру этого числа.
num = abs(int(input("Введите число: ")))
last_digit = int(str(num)[-1])
print(f"Последняя цифра числа: {last_digit}")

""" ИЛИ
num = abs(int(input("Введите число: ")))
last_digit = num % 10 
print(f"Последняя цифра числа: {last_digit}")"""