def num_sum(num):
    total = 0
    while True:
        total += num
        return total


for num in range(1, 11):
    print(num_sum(num=num))