from datetime import date
from dateutil.relativedelta import relativedelta

# now_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
# print(now_time)
# next_date = now_time - relativedelta(days=+1)
# print(next_date)
str1 = '2019-9-20'
str2 = '2019-10-21'
if date(str1) < date(str2):
    print('hehe')