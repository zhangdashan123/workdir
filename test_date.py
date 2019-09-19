import datetime
import time

from dateutil.relativedelta import relativedelta

# now_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
# print(now_time)
# next_date = now_time - relativedelta(days=+1)
# print(next_date)

now_time = datetime.date.today()
next_date = now_time - relativedelta(days=-1)
now_time = str(now_time).replace('-', '/')
next_date = str(next_date).replace('-', '/')
print(now_time)
print(next_date)