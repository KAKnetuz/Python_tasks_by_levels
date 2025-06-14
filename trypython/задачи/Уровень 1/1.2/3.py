# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
num = abs(int(input("Введите число: ")))
if num < 10:
    print('Число однозначное')
else:
    first_digit = int(str(num)[0])
    last_digit = int(str(num)[-1])
    sum_digits = first_digit + last_digit
    print(f'Сумма первой и последней цифры = {sum_digits}')

"""ИЛИ
num = abs(int(input("Введите число: ")))
last_digit = num % 10
first_digit = num
while first_digit >= 10:
    first_digit //= 10
sum_digits = first_digit + last_digit
print(f'Сумма первой и последней цифры = {sum_digits}')"""