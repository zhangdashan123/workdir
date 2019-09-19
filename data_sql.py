import threading
import traceback

import pymysql


class MySql(object):
    def __init__(self):
        self.db = pymysql.connect(host='192.168.1.5', port=3306, user='root', password='root', db='db_bby_expedia')
        self.cursor = self.db.cursor()

    def insert_sql(self, data_dict, table='t_cl_expedia_hotelprcie'):
        data = dict(data_dict)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        self.db.ping(reconnect=True)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            print('存储成功!!!')
        except Exception as e:
            traceback.print_exc()
            print(e, sql)
            self.db.rollback()
            # self.db.close()

    def delete_sql(self, stop_date, table='t_cl_expedia_hotelprcie'):
        """删除一个月之前的数据"""
        sql = 'delete from %s where data_date<="%s"' % (table, stop_date)
        self.db.ping(reconnect=True)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('删除一个月前数据成功!!!')
        except Exception as e:
            traceback.print_exc()
            print(e, sql)

    def select_sql(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
