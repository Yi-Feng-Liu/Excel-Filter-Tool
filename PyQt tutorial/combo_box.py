from PyQt6.QtWidgets import *
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('combo box')
        # self.resize(300, 200) # 可自由縮放視窗大小 但元件也必須跟著相對位置變更
        self.screen = QApplication.screens()[0].size()
        window_w = 500
        window_h = 500
        screen_w = self.screen.width()
        screen_h = self.screen.height()
        self.center_x = int(screen_w/2) - int(window_h/2) # 視窗置中
        self.center_y = int(screen_h/2) - int(window_w/2)
        self.setGeometry(self.center_x, self.center_y, window_w, window_h) # 根據螢幕大小 固定視窗 & 位置
        self.setFixedSize(window_w, window_h)
        self.ui()

    def ui(self):
        self.box = QComboBox(self)   # 加入下拉選單
        self.box.addItems(['A','B','C','D'])   # 加入四個選項
        self.box.setGeometry(10,10,200,30)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())