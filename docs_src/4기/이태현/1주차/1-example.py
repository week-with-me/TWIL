import time
import asyncio


async def from_hi_to_bye():
    await print(f'{time.ctime()} Hi!')
    asyncio.sleep(1.0)
    await print(f'{time.ctime()} Bye!')
    
    
asyncio.run(from_hi_to_bye())