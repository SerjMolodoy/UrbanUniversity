def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        q = [value] * m
        matrix.append(q)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# print()
#
#
# def get_matrix(ir, tu, eth, kr):
#     print(f'Майнинг фермы - {ir} {tu} {eth} {kr}')
#
#
# a, b, c, d = 'Bitriver', 'Intellion', 'Bitcluster', 'Stella'
# get_matrix(a, b, c, d)
# get_matrix(b, b, d, d)
# get_matrix(a, c, d, d)
# get_matrix(a, c, a, d)


# print()
#
#
# def sales(price, disc=5):
#     return price - price * disc / 100
#
#
# print(sales(20000))
# print(sales(2345))
# print(sales(2487.56))
# print
# print('Всё!')



