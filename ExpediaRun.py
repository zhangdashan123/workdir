from data_sql import MySql


class Run(object):
    def __init__(self):
        self.my = MySql()

    def run(self):
        sql1 = 'select house_price from t_cl_expedia_hotelprcie where area="%s" ' \
               'and hotel_name="%s" and house_name = "%s"' % (area, hotel_name, house_name)

        sql2 = 'select begin_date from t_cl_expedia_hotelprcie where area="%s" ' \
               'and hotel_name="%s" and house_name = "%s"' % (area, hotel_name, house_name)
        result_price = self.my.select_sql(sql1)
        result_date = self.my.select_sql(sql2)
        list_price = list(map(lambda x: int(x[0]), result_price))
        list_date = list(map(lambda x: str(x[0]), result_date))
        print(list_price)
        print(list_date)


if __name__ == '__main__':
    area = '杭州'
    hotel_name = '香格里拉酒店'
    house_name = '康莱德套房'
    r = Run()
    r.run()
