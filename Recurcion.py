def get_multipage_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multipage_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multipage_digits(40203)
print(result)
