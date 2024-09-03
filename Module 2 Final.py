from random import randint

n = randint(3, 20)
result = ""
for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            result += f'{i} {j}'
print(f'{n} - {result}')


# print()
# import random
#
#
# my_list = [10, 20, 40, 60, 80, 100]
# print(random.choice(my_list))
#
#
# print()
# from random import randint
#
#
# def generate_counts(n):
#     a = randint(1, n + 1)
#     return ((i + 1, 2 - (a == i)) for i in range(n))
#
#
# for b in generate_counts(10):
#     print("%i: %i" % b)
#
#
# print()
#
#
# import random
#
# Player1 = 'Denis'
# Player2 = 'Sergei'
#
# Denis_wins = 0
# Sergei_wins = 0
#
# Row1 = [1, 2, 3, 4, 5, 6]
# Row2 = [1, 2, 3, 4, 5, 6]
#
#
# def game():
#     for i in range(5):
#         random.shuffle(Row1)
#         random.shuffle(Row2)
#     first = random.choice(Row1)
#     second = random.choice(Row2)
#     return first + second
#
#
# print('Toss')
#
# for i in range(3):
#     Denis_number = random.randint(1, 50)
#     Sergei_number = random.randrange(1, 51, 1)
#
#     if Denis_number > Sergei_number:
#         print('Denis win the toss')
#         Denis_wins = game()
#         Sergei_wins = game()
#     else:
#         print('Sergei win the toss')
#         Denis_wins = game()
#         Sergei_wins = game()
#     if Denis_wins > Sergei_wins:
#         print('Denis is the winner, Final score: ', Denis_wins, 'Sergei score', Sergei_wins)
#     else:
#         print('Sergei is the winner, Final score: ', Sergei_wins, 'Denis score', Denis_wins)
# print()
# print('Всё!')
