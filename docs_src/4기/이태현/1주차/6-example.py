import time
import asyncio


async def find_user_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)


async def main():
    start = time.time()
    
    await asyncio.wait([
        find_user_async(5),
        find_user_async(7),
        find_user_async(3),
    ])
    
    end = time.time()
    
    print(f'> {end - start} 소요')
    
    
asyncio.run(main())