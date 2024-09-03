numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print('Primes: ', primes)
print('Not primes: ', not_primes)


# print()

# for i in range(3):
#     print('Hi')

# print()
#
# for i in 'Sergei':
#     print(i)

# print()
# a = ['BTC', 'ETF', 'BNB', 'TON', 'DOGE']
# b = ['1', '2', '3', '4', '5']
# for i in a:
#     for j in b:
#         print(i + ' - ' + j)
#

# print()
# a = 'c5o3)(*^%450^&^23f7%^5f0876-85dpgri&#&&($'
# for i in a:
#     if not i.isalpha():
#         continue
#     else:
#         print(i)


# print()
# my_dict = {'лето': 'прошло', 'настала': 'осень', 'школа': 'домашка'}
# for a, b in my_dict.items():
#     print(f'{a} : {b}')

# print()
# for i in range(1, 18, 4):
#     print('*' * i)

# print()
# my_dict = {'Сложить': 'a + b', 'Вычесть': 'a - b', 'Умножить': 'a * b', 'Разделить': 'a / b'}
# # a, b = int(input('Введите значение а: ')), int(input('Введите занчение b: '))
# # sign = input('Что хотите сделать? ')
# # if sign in my_dict.keys():
# #     print(eval(my_dict[sign]))
# # else:
# #     print('Неверное действие')
# for k, v in my_dict.items():
#     print(f'{k} - {v}')
# print()
# print('Всё!')




