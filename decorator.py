def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        summa = sum(args)
        a = 0
        for i in range(2, summa // 2 + 1):
            if summa % i == 0:
                a = a + 1
        if a <= 0:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(23, 21, 78)
print(result)
