import ctypes
import inspect
import sys
import threading
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from Expedia import Ui_MainWindow
from ExpediaRun import Run


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.setWindowTitle('Expadia酒店')

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)  # 设置背景图
        painter.drawPixmap(0, 0, 704, 693, QPixmap('./4.jpg'))

    def init_ui(self):
        self.r = Run(self)
        data = dict()
        data['num'] = 1
        self.thread = threading.Thread(target=self.r.start_task, args=(data, ))
        self.thread.start()
        self.r.show_data.connect(self.show_c)  # 显示城市
        self.pushButton.clicked.connect(self.start_2)  # 开始爬虫
        self.r.show_data2.connect(self.show_d)  # 显示酒店
        self.pushButton_2.clicked.connect(self.quit_sys)  # 结束

    def show_b(self):
        data = dict()
        data['num'] = 2
        text = self.comboBox.currentText()
        data['text'] = text
        print(text)
        self.thread = threading.Thread(target=self.r.start_task, args=(data, ))
        self.thread.start()
        self.r.show_data1.connect(self.show_a)
        self.pushButton_3.clicked.connect(self.start_1)  # 生成折线图

    def show_a(self, value):
        self.comboBox_2.clear()
        self.comboBox_2.addItems(value)

    def show_c(self, value):
        self.comboBox.addItems(value)
        self.comboBox.currentIndexChanged.connect(self.show_b)

    def show_d(self, value):
        self.textEdit.append(value)

    def start_1(self):
        data = dict()
        city_value = self.comboBox.currentText()
        hotel_value = self.comboBox_2.currentText()
        print(city_value, hotel_value)
        data['num'] = 3
        data['area'] = city_value
        data['hotel_name'] = hotel_value
        self.thread = threading.Thread(target=self.r.start_task, args=(data, ))
        self.thread.start()

    def start_2(self):
        data = dict()
        data['num'] = 4
        area = self.lineEdit.text()
        data['area'] = area
        self.thread = threading.Thread(target=self.r.start_task, args=(data, ))
        self.thread.start()

    def quit_sys(self):
        try:
            if self.thread.isAlive():
                self._asybc_raise(self.thread.ident, SystemExit)
        except:
            pass
        sys.exit()

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
