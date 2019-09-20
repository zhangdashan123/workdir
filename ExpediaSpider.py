import datetime
import traceback
from urllib.parse import unquote
import urllib3
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from dateutil.relativedelta import relativedelta
from ExpediaDetail import ExPeDiaDetail

urllib3.disable_warnings()

"""
Expedia网站城市搜索模块;
输入城市,获取城市的所有酒店;
最终得到酒店名称和酒店详情的url
"""


class ExPeDiaSpider(QThread):
    show_data3 = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ExPeDiaSpider, self).__init__(parent=parent)
        self.ed = ExPeDiaDetail()
        self.search_url = 'https://www.expedia.com/Hotel-Search-Data?responsive=true'
        self.headers = {
            "authority": "www.expedia.com",
            "method": "POST",
            "path": "/Hotel-Search-Data?responsive=true",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-length": "207",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.expedia.com",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        self.data = {
            # "destination": area,
            "startDate": "2019/09/17",
            "endDate": "2019/09/18",
            "adults": "2",
            # "regionId": "6084457",
            # "sort": "recommended",
            # "page": "2",  # 页数
            "langid": "2052",
            "hsrIdentifier": "HSR",
            "timezoneOffset": "28800000"
        }

    def get_total_page(self, area):
        self.data['destination'] = area
        try:
            resp = requests.post(url=self.search_url, headers=self.headers, data=self.data, verify=False)
            if resp.status_code == 200:
                resp_data = resp.json()
                total_page = resp_data.get('pagination').get('pageCount')
                print('总页数:', total_page)
                self.show_data3.emit('总页数:' + str(total_page))
                self.get_data(resp_data, area)
                self.get_new_page(total_page, area)
            else:
                print(resp.status_code, '服务器响应错误!!!')

        except Exception as e:
            traceback.print_exc()
            print(e, '搜索酒店服务器错误!!!')

    def get_new_page(self, total_page, area):
        """搜索结果翻页,从第二页开始"""
        for page in range(2, int(total_page) + 1):
            self.data['page'] = str(page)
            self.show_data3.emit('........正在抓取' + area + '第' + str(page) + '页数据.......')
            print('........正在抓取{}第{}页数据.......'.format(area, page))
            try:
                resp = requests.post(url=self.search_url, headers=self.headers, data=self.data, verify=False)
                if resp.status_code == 200:
                    resp_data = resp.json()
                    self.get_data(resp_data, area)
                else:
                    print(resp.status_code, '翻页服务器响应错误!!!')

            except Exception as e:
                traceback.print_exc()
                print(e, '翻页搜索酒店服务器错误!!!')

    def get_data(self, response, area):
        """从json数据中提取数据"""
        now_time = datetime.date.today()
        now_time = now_time - relativedelta(days=-1)
        next_date = now_time - relativedelta(days=-1)
        now_time = str(now_time).replace('-', '/')
        next_date = str(next_date).replace('-', '/')
        search_result = response.get('searchResults')
        hotel_list = search_result.get('retailHotelModels')
        for hotel_data in hotel_list:
            detail_url = hotel_data.get('infositeUrl')  # 酒店详情url
            if 'https://travelads.koddi.com' in detail_url:
                detail_url = 'https://www.expedia.com' + \
                             detail_url.split('www.expedia.com')[-1].split('&candidateHmGuid')[0]
                detail_url = unquote(detail_url)
                detail_url = unquote(detail_url)
                # print('截取的detail_url:', detail_url)
            detail_url = detail_url + 'chkin={}&chkout={}&'.format(now_time, next_date)  # 酒店入住日期
            hotel_name = hotel_data.get('retailHotelInfoModel').get('localizedHotelName')  # 酒店名称
            print(detail_url, hotel_name, area)
            self.show_data3.emit(area + ':' + hotel_name)
            self.ed.get_data(detail_url, hotel_name, area)


if __name__ == '__main__':
    area = '杭州'
    ep = ExPeDiaSpider()
    ep.get_total_page(area)
