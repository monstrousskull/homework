import random
num = random.randint(1, 100)
print(num)
levels = {0: 100, 1: 10, 2: 5, 3: 3}
level = int(input('difficulty level? (0 - 3)\n'))
max_att = levels[level]
user_num = None
user_count = int(input('number of users?\n'))
users = []
for i in range(user_count):
    user_name = input(f'username of player №{i+1}\n')
    users.append(user_name)
is_winner = False
winner_name = None
att = 0
while not is_winner:
    att += 1
    if att > max_att:
        print('you lost :P')
        print(f'the number was {num}')
        break
    for user in users:
        print(f"{user}'s turn")
        user_num = int(input('guess the number\n'))
        if user_num == num:
            is_winner = True
            winner_name = user
            break
        if user_num > num:
            print('my number is lower')
        elif user_num < num:
            print('my number is higher')
else:
    print(f'correct! {winner_name} won')
    print(f'(attempts: {att})\n')


a = 1
b = 100
x = None
att = 0
print('my turn!')
while x != '=':
    att += 1
    y = random.randint(a, b)
    x = input(f'{y}?\n')
    if x == '<':
        b = y - 1
    elif x == '>':
        a = y + 1
print('~yay:3')
print(f'attempts: {att}')
