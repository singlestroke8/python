with open('greeting.txt', 'r', encoding='utf-8') as file:
    count = 1
    for line in file:
        print('{0:03d}{1}'.format(count, line), end='')
        count += 1