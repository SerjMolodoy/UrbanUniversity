immutable_var = 1234, 5678, "Banana", True
print(immutable_var)  # кортеж неизменяемый, иначе вылетают ошибки
mutable_list = ['Sergei', 37, True, 'Diablo']
print(mutable_list)
mutable_list[0] = 'Student'
mutable_list[1] = 38
mutable_list[2] = False
mutable_list[3] = 'Angel'
print(mutable_list)
print()
a = 'Sergei', 37, True, 'Diablo'
b = 16, 64, 'Kronenburg'
c = list(a)
d = tuple (b)
c[0] = 48
c[1] = 12
c[2] = 'Bud'
c[3] = False
print(c)
print(d)  # кортеж неизменяемый, иначе вылетают ошибки
print()
print('Всё!')