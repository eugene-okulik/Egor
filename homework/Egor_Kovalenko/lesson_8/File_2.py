import random

salary = int(input())
bonus = random.choice([True, False])
if bonus:
    salary += bonus

print(f'{bonus} - ${salary}')
