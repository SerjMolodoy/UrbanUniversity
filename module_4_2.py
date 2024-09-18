def test_function():
    def inner_function():
        print('Я в области видимости функции test_funtion')

    inner_function()


# inner_function()  # Error

test_function()


# def test_function():
#     b = 10
#
#     def inner_function():
#         b = 20
#         print(b)
#
#     inner_function()
#     print('', b)
#
#
# # inner_function()
# # print('', b)
#
# b = 30
# test_function()
# print(' ', b)
