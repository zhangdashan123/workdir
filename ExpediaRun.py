from ExpediaMatplotlib import MatPlotLib
from data_sql import MySql

"""
查询模块;
输入地区和酒店名称
"""


class Run(object):
    def __init__(self):
        self.my = MySql()
        self.mp = MatPlotLib()

    def run(self):
        """[日期列表, 价格列表, '房型', 'r']"""
        # 查询一个城市所有的酒店
        sql = 'select distinct hotel_name from t_cl_expedia_hotelprcie where area = "%s"' % area
        result_hotel = self.my.select_sql(sql)
        list_hotel = list(map(lambda x: str(x[0]), result_hotel))
        print(list_hotel)
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
        self.mp.show_images(total_list)


if __name__ == '__main__':
    area = '杭州'
    hotel_name = '杭州温德姆至尊豪廷大酒店'
    # house_name = '皇冠豪华房'
    r = Run()
    r.run()
