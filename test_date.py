import re
from datetime import date
from dateutil.relativedelta import relativedelta

# now_time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
# print(now_time)
# next_date = now_time - relativedelta(days=+1)
# print(next_date)
str1 = 'cny1334'
regex = re.compile(r'\d+', re.S)
price_list = regex.findall(str1)
house_price = ''.join(price_list)
print(house_price)