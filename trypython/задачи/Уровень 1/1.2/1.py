# Дано число. Выведите в консоль первую цифру этого числа.
num = abs(int(input("Введите число: ")))
first_digit = int(str(num)[0])
print(f"Первая цифра числа: {first_digit}")
