
from urllib.parse import urlencode

import re
str = '我的个人邮箱是cqc@cuiqingcai.com，个人博客是cuiqingcai.com，个人公众号是进击的Coder'
result = re.search('(?<=，)(?<!。)个人博客是(.*?)(?=，)', str)
print('整句结果：' + result.group(), '第一个匹配结果：' + result.group(1), sep='\n')
'''这是第四版'''
