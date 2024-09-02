
import asyncio

async def start_strongman(name, power):
    print(f'силач {name} начал соревнование')
    k = 5
    delay = k / power
    for i in range(1,6):
        await asyncio.sleep(delay)
        print(f'силач {name} поднял {i} шар')
    print(f'силач {name} закончил соревнование')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())



