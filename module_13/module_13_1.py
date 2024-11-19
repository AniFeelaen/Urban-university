import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял шар №{i}")
        
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    tasks = (
        asyncio.create_task(start_strongman('Pasha', 1)),
        asyncio.create_task(start_strongman('Denis', 8)),
        asyncio.create_task(start_strongman('Apollon', 4))
    )
    # task1 = asyncio.create_task(start_strongman('Pasha', 3)),
    # task2 = asyncio.create_task(start_strongman('Denis', 4)),
    # task3 = asyncio.create_task(start_strongman('Apollon', 5)) 
    # await task1
    # await task2
    # await task3
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(start_tournament())