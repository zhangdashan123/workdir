import random
import re
import traceback
import time
from lxml import etree
import urllib3
import requests
from selenium import webdriver
from BloomFilter import BloomFilter
from data_sql import MySql

urllib3.disable_warnings()

"""
根据提供的详情url去提取酒店房间的信息
"""


class ExPeDiaDetail(object):
    def __init__(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://www.expedia.com/Hotel-Search?destination=%E6%9D%AD%E5%B7%9E&startDate=&endDate=&rooms=1&adults=2')
        self.bf = BloomFilter()
        self.my = MySql()
        self.headers = {
            "authority": "www.expedia.com",
            "method": "GET",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "cookie": "currency=CNY; linfo=v.4,|0|0|255|1|0||||||||2052|0|0||0|0|0|-1|-1; MC1=GUID=c5af0e72ed394922b54266aefae94230; DUAID=c5af0e72-ed39-4922-b542-66aefae94230; stop_mobi=yes; AB_Test_TripAdvisor=A; rlt_marketing_code_cookie=; s_ecid=MCMID%7C01116474014119894191197528242685779445; __gads=ID=842872e0aa64ecd7:T=1567129172:S=ALNI_Mah0EHJxmerMTdqe1-DekW2IMtLDg; _gcl_au=1.1.1634494261.1567129173; intent_media_prefs=; xdid=78770b2d-1c4a-4a05-bc5d-ee5acd813e09|1567129176|expedia.com; tpid=v.1,1; iEAPID=221002; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; s_cc=true; qualtrics_sample=false; qualtrics_SI_sample=false; _ctpuid=88a221ef-5ddc-4979-ad49-33cbf279b98f; lastConsentChange=1568614374619; aspp=v.1,0|cn.b.baidu.bt-zh.hotel|||||||||SEM|20191017||; JSESSION=692a229f-e816-4a84-a109-915a54246a1c; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=-179204249%7CMCIDTS%7C18156%7CMCMID%7C01116474014119894191197528242685779445%7CMCAAMLH-1569291877%7C11%7CMCAAMB-1569313947%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1568716347s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0; cesc=%7B%22marketingClick%22%3A%5B%22false%22%2C1568715343087%5D%2C%22hitNumber%22%3A%5B%2222%22%2C1568715343087%5D%2C%22visitNumber%22%3A%5B%227%22%2C1568709144621%5D%2C%22sem%22%3A%5B%22SEM.cn.b.baidu.bt-zh.hotel.ZzZz.5050000001167.4b36cf4b-29a4-4e36-a70c-75d5b91c7c0e.k_user_id.%22%2C1568686693229%5D%2C%22entryPage%22%3A%5B%22page.Hotels.Infosite.Information%22%2C1568715343087%5D%2C%22semdtl%22%3A%5B%22a1.b1.d1%7Bcreative%7D.e1.f1.g1%7Bkeywordid%7D.h1%7Bmatchtype%7D.i1.j1.k1.l1.m1.n1%7Bplacement%7D%22%2C1568686693229%5D%2C%22cid%22%3A%5B%22SEM.cn.b.baidu.bt-zh.hotel%22%2C1568686693229%5D%7D; JSESSIONID=AF5FE56AEC7E85778639F897B6013D61; CONSENTMGR=ts:1568715343016%7Cconsent:true; utag_main=v_id:016ce02d7791002362acb2e064000307300ec06b00bd0$_sn:7$_ss:0$_st:1568717143031$ses_id:1568709147182%3Bexp-session$_pn:11%3Bexp-session; s_ppvl=page.Hotels.Infosite.Information%2C32%2C32%2C1537%2C1920%2C937%2C1920%2C1080%2C1%2CP; HMS=6ef80df1-d148-4392-882e-10c2c0efe275; s_ppv=page.Hotels.Infosite.Information%2C52%2C31%2C2737%2C1920%2C357%2C1920%2C1080%2C1%2CP"
        }
        self.cookies = 'GUID=c5af0e72ed394922b54266aefae94230;DUAID=c5af0e72-ed39-4922-b542-66aefae94230;JSESSIONID=AF5FE56AEC7E85778639F897B6013D61'
        # if os.path.exists(r'HotelPrice.csv'):
        #     list_info = ['房型', '价格', '入住日期', '退房日期', '酒店名称', '地区']
        #     with open(r'HotelPrice.csv', 'a+', encoding='utf-8-sig', newline='') as file:
        #         writer = csv.writer(file, dialect='excel')
        #         writer.writerow(list_info)

    def get_data(self, detail_url, hotel_name, area):
        # time.sleep(random.uniform(8, 12))  # 访问每个酒店的间隔时间
        try:
            resp = requests.get(url=detail_url, headers=self.headers, verify=False)
            if resp.status_code == 200:
                regex = re.compile(r'chkin=(.*?)&chkout=(.*?)&', re.S)
                date_info = regex.findall(detail_url)
                print('日期信息:', date_info)
                str_data = resp.text
                # print(str_data)
                if 'infosite.offersData' in str_data:
                    print('进入offersData....')
                    regex = re.compile(r'infosite\.offersData(.*?)roomsAndRatePlans\.rooms', re.S)
                    str_data1 = regex.findall(str_data)
                    # print(str_data1)
                    if len(str_data1) > 0:
                        print('.............')
                        str_data = str_data1[0]
                    regex1 = re.compile(r'"roomTypeCode":.*?"(.*?)".*?"name":.*?"(.*?)"', re.S)
                    resp1 = regex1.findall(str_data)  # 房子类型
                    print(resp1)
                    regex2 = re.compile(r'"hotelID":.*?"roomTypeCode":.?"(.*?)".*?"displayPrice":.?"(.*?)"', re.S)
                    # regex2 = re.compile(r'"hotelID".*?"roomTypeCode": "(.*?)".*?"displayPrice": "(.*?)"', re.S)
                    resp2 = regex2.findall(str_data)  # 房子价格
                    print(resp2)
                    resp_dict = dict()
                    for tuple_data in resp2:
                        if tuple_data[0] not in resp_dict.keys():
                            resp_dict[tuple_data[0]] = tuple_data[1]
                    for resp_data in resp1:
                        house_num = resp_data[0]
                        house_price = resp_dict.get(house_num, '')
                        house_name = resp_data[1].strip()
                        if house_price and house_price != '0' and '房' in house_name:
                            item = dict()
                            house_price = house_price.replace('CNY', '').replace(',', '')
                            begin_date = date_info[0][0]
                            end_date = date_info[0][1]
                            print(house_name, house_price, begin_date, end_date, hotel_name, area)
                            item['house_name'] = house_name
                            item['house_price'] = house_price
                            item['begin_date'] = begin_date
                            item['end_date'] = end_date
                            item['hotel_name'] = hotel_name
                            item['area'] = area
                            # house_info = [house_name, house_price, begin_date, end_date, self.hotel_name, self.area]
                            if self.bf.isContains(
                                                                            house_name + house_price + begin_date + end_date + hotel_name + area):  # 判断字符串是否存在
                                print('exists!')
                            else:
                                print('not exists!')
                                self.bf.insert(
                                    house_name + house_price + begin_date + end_date + hotel_name + area)
                                self.my.insert_sql(item)


                        else:
                            pass
                            # print(house_num, resp_data[1], '无价格!!!')
                else:
                    print('进入无offersData....')
                    regex = re.compile(r'"roomTypeCode":.*?".*?".*?"name":.*?"(.*?)".*?"displayPrice":.*?"(.*?)"', re.S)
                    resp = regex.findall(str_data)  # 房子类型
                    print(resp)
                    for resp_data in resp:
                        item = dict()
                        house_name = resp_data[0].strip()
                        house_price = resp_data[1].strip()
                        house_price = house_price.replace('CNY', '').replace(',', '')
                        begin_date = date_info[0][0]
                        end_date = date_info[0][1]
                        print(house_name, house_price, begin_date, end_date, hotel_name, area)
                        if house_price != '0':
                            item['house_name'] = house_name
                            item['house_price'] = house_price
                            item['begin_date'] = begin_date
                            item['end_date'] = end_date
                            item['hotel_name'] = hotel_name
                            item['area'] = area
                            if self.bf.isContains(
                                                                            house_name + house_price + begin_date + end_date + hotel_name + area):  # 判断字符串是否存在
                                print('exists!')
                            else:
                                print('not exists!')
                                self.bf.insert(house_name + house_price + begin_date + end_date + hotel_name + area)
                                self.my.insert_sql(item)
                                # house_info = [house_name, house_price, begin_date, end_date, hotel_name, area]

            else:
                print(resp.status_code, '服务器响应错误!!!!!!!!')

        except Exception as e:
            traceback.print_exc()
            print(e, '搜索酒店服务器错误!!!')

    def selenium_data(self, url, hotel_name, area):
        self.driver.get(url)
        cookie_dict = self.stringToDict(self.cookies)
        self.driver.delete_all_cookies()
        print('cookies删除完成...')
        self.driver.add_cookie(cookie_dict)
        print('cookies添加完成...')
        regex = re.compile(r'chkin=(.*?)&chkout=(.*?)&', re.S)
        date_info = regex.findall(url)
        print('日期信息:', date_info)
        html_resp = self.driver.page_source
        resp_elem = etree.HTML(html_resp)
        elem_list = resp_elem.xpath('//thead[@id="rooms-header"]/following-sibling::*[@data-provider]')
        for elem in elem_list:
            item = dict()
            house_name = elem.xpath('//h3[@class="room-name"]/text()')
            house_price = elem.xpath('.//*[@class="room-price-value"]/text()')
            # house_price = house_price.replace('CNY', '').replace(',', '')
            begin_date = date_info[0][0]
            end_date = date_info[0][1]
            print(house_name, house_price, begin_date, end_date, hotel_name, area)
            # item['house_name'] = house_name
            # item['house_price'] = house_price
            # item['begin_date'] = begin_date
            # item['end_date'] = end_date
            # item['hotel_name'] = hotel_name
            # item['area'] = area
            # if self.bf.isContains(house_name + house_price + begin_date + end_date + hotel_name + area):  # 判断字符串是否存在
            #     print('exists!')
            # else:
            #     print('not exists!')
            #     self.bf.insert(house_name + house_price + begin_date + end_date + hotel_name + area)
            #     self.my.insert_sql(item)

    def stringToDict(self, cookie_string):
        itemDict = {}
        items = cookie_string.split(';')
        for item in items:
            key = item.split('=', 1)[0].replace(' ', '')
            value = item.split('=', 1)[1]
            itemDict[key] = value
        print("*" * 90)
        print(itemDict)
        print("*" * 90)
        return itemDict


if __name__ == '__main__':
    # url = 'https://www.expedia.com/cn/Hangzhou-Hotels-Atour-Light-Hotel-Westlake-Fengqi-Road-Hangzhou.h33204043.Hotel-Information?rm1=a2&hwrqCacheKey=6461d39b-5077-4061-83ca-a2d93e81a4c9HWRQ1568869729085&cancellable=false&regionId=6084457&vip=false&c=e79d9e11-bfc1-41ab-9dc3-0968ef1fc986&chkin=2019/09/20&chkout=2019/09/21&'
    url = 'https://www.expedia.com/cn/Hotels-Crowne-Plaza-Hangzhou-Heda.h22949395.Hotel-Information?rm1=a2&hwrqCacheKey=a995f173-aae0-48f9-9c60-bfd1b591f854HWRQ1568703523167&cancellable=false&regionId=6084457&vip=false&c=e95dcb76-9c3b-4f5e-9994-85bb9f38624e&chkin=2019/09/19&chkout=2019/09/20&'
    area = '杭州'
    hotel_name = '香格里拉酒店'
    ed = ExPeDiaDetail()
    # ed.selenium_data(url, hotel_name, area)
