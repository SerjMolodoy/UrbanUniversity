calls = 0


def counts_calls():
    global calls
    calls += 1


def string_info(string):
    counts_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    counts_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)


#
# def out_space():
#     a = 50
#
#     def in_space():
#         a = 100
#         print('a = ', a)
#
#     in_space()
#     print('a = ', a)
#
#
# a = 150
# out_space()
# print('a = ', a)


# def out_space():
#     global a
#     a = 50
#
#     def in_space():
#         global a
#         a = 100
#         print('a = ', a)
#
#     in_space()
#     print('a = ', a)
#
# a = 150
# out_space()
# print('a = ', a)


# def x():
#     y = 2
#
#     def z():
#         nonlocal y
#         y = 3
#
#     z()
#     print(y)
#
#
# x()


