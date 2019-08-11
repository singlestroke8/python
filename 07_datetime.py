from datetime import date
from datetime import datetime

# 今日の日付
today = date.today()
print(today)

# 今
now = datetime.now()
print(now)

# 任意の日付
day = date(2019, 8, 1)

# 曜日を取得
print(day.weekday())
weekday_str = '月火水木金土日'
print(weekday_str[day.weekday()])