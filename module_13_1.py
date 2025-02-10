import asyncio


# Асинхронная функция для имитации поднятия шаров Атласа
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for ball in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {ball} шар')

    print(f'Силач {name} закончил соревнования.')


# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создаем задачи для трех силачей
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Ожидаем завершения всех задач
    await strongman1
    await strongman2
    await strongman3


# Запуск турнира
asyncio.run(start_tournament())