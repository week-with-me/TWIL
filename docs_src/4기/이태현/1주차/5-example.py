import time


def find_user_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
        

def main():
    start = time.time()
    
    find_user_sync(5)
    find_user_sync(7)
    find_user_sync(3)
    
    end = time.time()
    
    print(f'> {end - start} 소요')


main()