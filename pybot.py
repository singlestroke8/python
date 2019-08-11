'''
bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
}
while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break
    if not response:
        response = '何ヲ言ッテイルカ、ワカラナイ'
    print(response)
    if 'さようなら' in command:
        break
'''
'''
    if 'こんにちは' in command:
        print("コンニチハ")
    elif 'ありがとう' in command:
        print("ドウイタシマシテ")
    elif 'さようなら' in command:
        print("サヨウナラ")
        break
    else:
        print("何ヲ言ッテイルカ、ワカラナイ")
'''

from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command

# 長さコマンドの関数
def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列の長さは {} 文字です'.format(length)
    return response

# 平成コマンドの関数を作成
def heisei_command(command):
    heisei, year_str = command.split()
    # 例外処理の場合
    # try:
    #     year = int(year_str)
    #     if year >= 1989:
    #         heisei_year = year - 1988
    #         response = '西暦{}年は、平成{}年です。'.format(year, heisei_year)
    #     else:
    #         response = '西暦{}年は、平成ではありません。'.format(year)
    # except ValueError:
    #     response = '数値を指定してください'
    # if 文で値をチェック
    if year_str.isdigit():
        year = int(year_str)
        heisei = year - 1988
        response = '西暦{}年は、平成{}年です。'.format(year, heisei_year)
    else:
        response = '数値を指定してください'
    return response

command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

while True:
    command = input('pybot> ')
    response = ''
    try:
        for key in bot_dict:
            if key in command:
                response = bot_dict[key]
                break
        if '平成' in command:
            response = heisei_command(command)
        if '長さ' in command:
            response = len_command(command)
        if '干支' in command:
            response = eto_command(command)
        if '選ぶ' in command:
            response = choice_command(command)
        if 'さいころ' in command:
            response = dice_command()
        if '今日' in command:
            response = today_command()
        if '現在' in command:
            response = now_command()
        if '曜日' in command:
            response = weekday_command(command)
        if not response:
            response = '何ヲ言ッテイルカ、ワカラナイ'
        print(response)

        if 'さようなら' in command:
            break
    except Exception as e:
        print('予期せぬ エラーが 発生しました')
        print('* 種類:', type(e))
        print('* 内容:', e)
