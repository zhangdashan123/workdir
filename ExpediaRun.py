from PyQt5.QtCore import QThread, pyqtSignal
from ExpediaMatplotlib import MatPlotLib
from ExpediaSpider import ExPeDiaSpider
from data_sql import MySql

"""
查询模块;
输入地区和酒店名称
"""


class Run(QThread):
    show_data = pyqtSignal(list)
    show_data1 = pyqtSignal(list)
    show_data2 = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Run, self).__init__(parent=parent)
        self.my = MySql()
        self.ep = ExPeDiaSpider()

    def start_task(self, value):
        self.value = value
        self.start()

    def run(self):
        num = self.value['num']
        if num == 1:
            self.select_city()
        if num == 2:
            city = self.value['text']
            self.select_hotel(city)
        if num == 3:
            area = self.value['area']
            hotel_name = self.value['hotel_name']
            self.runs(area, hotel_name)
        if num == 4:
            area = self.value['area']
            self.show_data2.emit('开始抓取数据...')
            self.ep.show_data3.connect(self.send_data)
            self.ep.get_total_page(area)

    def send_data(self, value):
        self.show_data2.emit(value)

    def select_hotel(self, city):
        # 查询一个城市所有酒店
        hotel_sql = 'select distinct hotel_name from t_cl_expedia_hotelprcie where area = "%s"' % city
        result_hotel = self.my.select_sql(hotel_sql)
        list_hotel = list(map(lambda x: str(x[0]), result_hotel))
        # print(list_hotel)
        self.show_data1.emit(list_hotel)

    def select_city(self):
        # 查询数库中所有的城市
        city_sql = 'select distinct area from t_cl_expedia_hotelprcie'
        result_city = self.my.select_sql(city_sql)
        list_city = list(map(lambda x: str(x[0]), result_city))
        # print(list_city)
        self.show_data.emit(list_city)

    def runs(self, area, hotel_name):
        """[日期列表, 价格列表, '房型', 'r']"""
        # 查询一个城市所有的酒店
        # sql = 'select distinct hotel_name from t_cl_expedia_hotelprcie where area = "%s"' % area
        # result_hotel = self.my.select_sql(sql)
        # list_hotel = list(map(lambda x: str(x[0]), result_hotel))
        # print(list_hotel)
        # 查询一个地区的某个酒店中所有的房价种类
        color = ['r', 'g', 'b', 'w', 'c', 'm', 'y', 'k']
        total_list = []  # 所有房间类型所需参数
        sql1 = 'select distinct house_name from t_cl_expedia_hotelprcie where area="%s"' \
               'and hotel_name="%s"' % (area, hotel_name)
        result_type = self.my.select_sql(sql1)
        list_type = list(map(lambda x: str(x[0]), result_type))  # 查询查来的房间类型列表
        max_date = 0
        max_data = ''
        for color_index, house_type in enumerate(list_type):
            single_list = []  # 当个房间信息列表
            # 查询某个房型价格
            sql2 = 'select house_price from t_cl_expedia_hotelprcie where area="%s" ' \
                   'and hotel_name="%s" and house_name = "%s"' % (area, hotel_name, house_type)
            # 查询房型日期
            sql3 = 'select begin_date from t_cl_expedia_hotelprcie where area="%s" ' \
                   'and hotel_name="%s" and house_name = "%s" order by begin_date' % (area, hotel_name, house_type)

            result_price = self.my.select_sql(sql2)
            result_date = self.my.select_sql(sql3)
            list_price = list(map(lambda x: int(x[0]), result_price))
            list_date = list(map(lambda x: str(x[0]), result_date))
            if len(list_date) > max_date:
                max_date = len(list_date)
                max_data = [list_date, list_price, house_type, color[color_index]]
            single_list.append(list_date)
            single_list.append(list_price)
            single_list.append(house_type)
            single_list.append(color[color_index])
            total_list.append(single_list)
        total_list.remove(max_data)
        total_list.insert(0, max_data)
        print(total_list)
        print('开始调用画图MatPlotLib...')
        MatPlotLib().show_images(total_list)


# if __name__ == '__main__':
#     area = '杭州'
#     hotel_name = '杭州温德姆至尊豪廷大酒店'
#     # house_name = '皇冠豪华房'
#     r = Run()
#     r.runs()
