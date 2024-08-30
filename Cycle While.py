my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break
    if my_list[index] > 0:
        print(my_list[index])
    index += 1


# correct_name = 'Denis'
# a = input('Введите имя преподавателя: ')
# while a != correct_name:
#     a = input('Введите имя преподавателя: ')
# print('Молодец')
# print()
# print('Всё!')
