text = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']


def count(my_str):
    for items in text:
        print(int(items[items.index(':') + 2:]) + 10)


count(text)
