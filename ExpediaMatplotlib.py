import random
import matplotlib.pyplot as plt


class MatPlotLib(object):
    def __init__(self):
        print('画布初始化中...')
        # 创建一个figure
        plt.figure(figsize=(14, 8), dpi=80)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # 准备x, y坐标的数据,酒店类型
        # y_haohua = [random.uniform(15, 18) for i in x]
        # y_putong = [random.uniform(9, 13) for i in x]

        # 准备x, y坐标的数据,酒店类型
        x_ch = range(30)
        y_ticks = range(5000)
        # 修改x,y坐标的刻度
        plt.xticks(x_ch[::1])  # 第一个参数是刻度间隔距离,第二个是刻度标识间隔
        plt.yticks(y_ticks[::500])
        # 增加xy轴的描述信息
        plt.xlabel('日期')
        plt.ylabel('价格')
        # self.show_images(x, y_haohua)

    def show_images(self, total_list):
        # 画酒店的折线图
        # color = ['r', 'g', 'b', 'w', 'c', 'm', 'y', 'k']
        # line_num = len(total_list)  # 折线的数量
        # plt.plot(x, y_haohua, label="豪华")
        # plt.plot(x, y_putong, color='r', linestyle='-', label='普通')
        for line in total_list:
            print(line[0], line[1], line[3], line[2])
            plt.plot(line[0], line[1], color=line[3], label=line[2])
        # 添加图形注释
        plt.legend(loc="best")
        plt.show()


if __name__ == '__main__':
    mp = MatPlotLib()
    total_list = [[['2019/09/18', '2019/09/19', '2019/09/20'], [521, 439, 534], '尊贵客房', 'r'], [['2019/09/18', '2019/09/19', '2019/09/20'], [614, 774, 934], '皇冠豪华房', 'g']]
    mp.show_images(total_list)
