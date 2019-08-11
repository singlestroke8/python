import random

def choice_command(command):
    data = command.split()
    # choiced = random.choice(data)
    # 「選ぶ」を対象外にし、リストの1番目以降が対象となる
    choiced = random.choice(data[1:])
    response = '「{}が選ばれました」'.format(choiced)
    return response

def dice_command():
    num = random.randrange(1, 7)
    response = '「{}が出ました」'.format(num)
    return response