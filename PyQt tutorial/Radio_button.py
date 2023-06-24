from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test_radio_button')
        self.resize(320, 240)
        self.ui()


    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 30, 100, 20)

        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(30, 60, 100, 20)
        self.rb_a.setText('aa')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setGeometry(150, 60, 100, 20)
        self.rb_b.setText('bb')
        self.rb_a.toggled.connect(lambda: self.showState(self.rb_a))  # 綁定函式

        self.group = QtWidgets.QButtonGroup(self)
        self.group.addButton(self.rb_a)
        self.group.addButton(self.rb_b)
        self.rb_b.toggled.connect(lambda: self.showState(self.rb_b))  # 綁定函式


    def showState(self, rb):
        self.label.setText(rb.text() + ':' + str(rb.isChecked()))  # 取得按鈕狀態

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())