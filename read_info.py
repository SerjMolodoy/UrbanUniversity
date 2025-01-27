import multiprocessing
import time
import os


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    # Создаем список названий файлов
    filenames = [f'./file{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейное выполнение: {linear_time} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f"Многопроцессное выполнение: {multiprocess_time} секунд")
