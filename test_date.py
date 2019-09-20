from datetime import date
from dateutil.relativedelta import relativedelta

# now_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
# print(now_time)
# next_date = now_time - relativedelta(days=+1)
# print(next_date)
str1 = 'MC1=GUID=c5af0e72ed394922b54266aefae94230'
str_li = str1.split('=', 1)
print(str_li)