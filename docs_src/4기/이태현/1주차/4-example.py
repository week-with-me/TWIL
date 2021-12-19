def coroutine_num_sum():
    total = 0
    while True:
        temp = (yield total)
        total += temp
        
coroutine = coroutine_num_sum()
next(coroutine)
        
for num in range(1, 11):
    print(coroutine.send(num))