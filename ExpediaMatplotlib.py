import random
import matplotlib.pyplot as plt


def show_draw(x, y_haohua):
    # 创建一个figure
    plt.figure(figsize=(20, 8), dpi=80)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 准备x, y坐标的数据,酒店类型
    xx = range(len(x))
    # y_haohua = [random.uniform(15, 18) for i in x]
    # y_putong = [random.uniform(9, 13) for i in x]

    # 构造中文列表的字符串
    x_ch = xx
    y_ticks = range(5000)
    # 修改x,y坐标的刻度
    plt.xticks(x_ch[::1])  # 第一个参数是刻度间隔距离,第二个是刻度标识间隔
    plt.yticks(y_ticks[::500])
    # 增加xy轴的描述信息
    plt.xlabel('日期')
    plt.ylabel('价格')

    # 画酒店的折线图
    plt.plot(x, y_haohua, label="豪华")
    # plt.plot(x, y_putong, color='r', linestyle='-', label='普通')
    # 添加图形注释
    plt.legend(loc="best")
    plt.show()


list_price = [1540, 1940, 4890, 1390, 1390, 1540, 1390, 1640, 2890, 1940]
list_date = ['2019/09/19', '2019/09/20', '2019/09/21', '2019/09/22', '2019/09/23', '2019/09/24', '2019/09/25',
             '2019/09/26', '2019/09/27', '2019/09/28']
show_draw(list_date, list_price)
