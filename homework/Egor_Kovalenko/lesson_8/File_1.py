def fibo():
    a = 1
    b = 1
    while True:
        yield a
        a = b
        b = a + b


count = 0

for num in fibo():
    if count == 5:
        print(num)
    if count == 200:
        print(num)
    if count == 1000:
        print(num)
    if count == 100000:
        break

    count += 1
