my_dict = {'BTC': 70000, 'Eth': 3400, 'Sol': 182, 'Ton': 6}
print('Курсы криптовалют:', my_dict)
print('Курс Eth:', my_dict['Eth'])
print('Курс Ltc:', my_dict.get('Ltc', 'курс не добавлен'))
my_dict.update({'Bnb': 572, 'Xmr': 160})
removed_price = my_dict.pop('Ton')
print('Ненужный курс \'Ton\':', removed_price)
print('Нужные курсы:', my_dict)

print()
print()

my_set = {38, 5, 2, 38, 2, 'Sergei', 'Sasha', 'Sasha', True, True}
print('Множество:', my_set)
my_set.add('Alex')
print('Добавили Лёху:', my_set)
my_set.add('Vova')
print('Добавили Вову:', my_set)
my_set.discard(56)  # удалили несуществующий
print('Ничего не изменилось:', my_set)
my_set.remove(2)  # удалили существующий
print('Удалили 2:', my_set)
print()
print('Всё!')

