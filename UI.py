from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import cv2 as cv
import numpy as np


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Excel Filter Toolkit')
        self.screen = QApplication.screens()[0].size()
        palette = self.palette()
        self.background_color = palette.color(QPalette.ColorRole.Window)
        window_w = 800
        window_h = 600
        screen_w = self.screen.width()
        screen_h = self.screen.height()
        self.center_x = int(screen_w/2) - int(window_h/2) # 視窗置中
        self.center_y = int(screen_h/2) - int(window_w/2)
        self.setFixedSize(window_w, window_h)
        self.setGeometry(self.center_x, self.center_y, window_w, window_h) # 根據螢幕大小 固定視窗 & 位置

        # Create menu bar 
        self.menubar = QMenuBar(self)
        self.menu_setting = QMenu('Setting')  

        self.bc = QAction('Background color') 
        self.menu_setting.addAction(self.bc) 

        self.bi = QAction('Background image') 
        self.menu_setting.addAction(self.bi)

        self.fc = QAction('Font color')  
        self.menu_setting.addAction(self.fc) 

        self.ft = QAction('Font type')  
        self.menu_setting.addAction(self.ft)
        self.menubar.addMenu(self.menu_setting)   

        self.rb_a = QRadioButton(self)
        self.rb_a.setGeometry(200, 50, 181, 31)
        self.rb_a.setText('Electronic File')

        self.rb_b = QRadioButton(self)
        self.rb_b.setGeometry(200+250, 50, 181, 31)
        self.rb_b.setText('Manually Entered File')

        copyright_str = 'Copyright © 2023 YF Liu. All rights reserved.'
        self.copyrightlabel = QLabel(self)
        self.copyrightlabel.setGeometry(0, window_h-30, 250, 30)
        self.copyrightlabel.setText(copyright_str)
        self.copyrightlabel.setStyleSheet(
            "font: bold 10px;\n"
        )

        self.update_push_button = QPushButton(self)
        self.update_push_button.setGeometry(window_w-100, window_h-100, 100, 100)
        update_push_button_img = self.resize(".\\Images\\link_img.jpg", 100, 100)
        self.update_push_button.setStyleSheet(
            f"background-image: url({update_push_button_img})"
        )


    def resize(self, imgpath:str, resize_w:int, resize_h:int, changeBG=True):
        image_name = imgpath.split("\\")[-1].split(".")[0]
        
        origin_img = cv.imread(imgpath)
        if changeBG:
            if origin_img.ndim > 0:
                mask = np.logical_and.reduce(origin_img == 255, axis=2)
                origin_img[mask] = [self.background_color.red(), self.background_color.green(), self.background_color.blue()]
        resize_img = cv.resize(origin_img, (resize_w, resize_h))
        save_path = f'Images/{image_name}_resize.jpg'
        cv.imwrite(save_path, resize_img)
        return save_path


    def set_font(self):
        font, ok = QFontDialog.getFont()
        print(font)
        if ok:
            self.label1.setFont(font)
            self.label2.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())