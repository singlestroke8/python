year_str = input("西暦を4桁で入力してください")
year = int(year_str)
number_of_eto = (year + 8) % 12

# print(number_of_eto)
#タプルで定義
eto_list = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
eto_name = eto_list[number_of_eto]
# print(eto_name)
print('あなたの干支は{}です。'.format(eto_name))
"""
if number_of_eto == 0:
  print("子")
elif number_of_eto == 1:
  print("牛")
elif number_of_eto == 2:
  print("虎")
elif number_of_eto == 3:
  print("兎")
elif number_of_eto == 4:
  print("龍")
elif number_of_eto == 5:
  print("巳")
elif number_of_eto == 6:
  print("馬")
"""