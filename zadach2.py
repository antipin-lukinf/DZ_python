# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

print(' для выхода нажмите 00')

while True:

    number = int(input('Введите целое, не отрицательное число : '))
    if number == 00:
        break

    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1

    if count > 1:
        print('число составное')

    else:
        print('число простое')