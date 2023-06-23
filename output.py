# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.font_type = 'Bahnschrift SemiBold'
        self.font_size = '12pt'
        self.border_radius = '11px'
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        MainWindow.setStyleSheet(
            "background-color: rgb(225, 228, 255);\n"""
        )
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 620, 100, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(101, 41))
        self.pushButton.setStyleSheet(
            "background-color: rgb(255, 229, 167);\n"
            "font: italic 30pt \"Palace Script MT\";\n"
            "color: rgb(0, 0, 0);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            "border-width: 2px;\n"
            "font: bold 30px;\n"
            "\n"
            ""
        )
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(220, 100, 181, 31))
        self.radioButton.setStyleSheet(
            f"font: {self.font_size} \"Arial\";\n"
            f"font: 600 {self.font_size} \"{self.font_type}\";"
        )
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(660, 100, 181, 31))
        self.radioButton_2.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 160, 621, 411))
        self.stackedWidget.setMinimumSize(QtCore.QSize(551, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 110, 141, 31))
        self.pushButton_4.setStyleSheet(
            f"font: 600 {self.font_size} \"{self.font_type}\";\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            ""
        )
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_5 = QtWidgets.QTextEdit(parent=self.page)
        self.textEdit_5.setGeometry(QtCore.QRect(210, 370, 231, 31))
        self.textEdit_5.setStyleSheet(
            "background-color: rgb(255, 248, 221);\n"
            f"border-radius: {self.border_radius};"
        )
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_11 = QtWidgets.QLabel(parent=self.page)
        self.label_11.setGeometry(QtCore.QRect(70, 370, 91, 31))
        self.label_11.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.page)
        self.label_12.setGeometry(QtCore.QRect(70, 180, 500, 31))
        self.label_12.setStyleSheet(
            f"font: 600 {self.font_size} \"{self.font_type}\";\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;"
        )
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.page)
        self.label_13.setGeometry(QtCore.QRect(70, 250, 121, 31))
        self.label_13.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.page)
        self.label_14.setGeometry(QtCore.QRect(70, 310, 121, 31))
        self.label_14.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_14.setObjectName("label_14")
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_5.setGeometry(QtCore.QRect(210, 250, 231, 31))
        self.comboBox_5.setStyleSheet(
            "border-style: outset;\n"
            "background-color: rgb(255, 248, 221);\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;"
        )
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_15 = QtWidgets.QLabel(parent=self.page)
        self.label_15.setGeometry(QtCore.QRect(220, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily(f"{self.font_type}")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(
            f"font: 600 16pt \"{self.font_type}\";\n"
            "\n"
            ""
        )
        self.label_15.setObjectName("label_15")
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_6.setGeometry(QtCore.QRect(210, 60, 251, 25))
        self.comboBox_6.setStyleSheet(
            "border-style: outset;\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;"
        )
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(0, "")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.page)
        self.comboBox_7.setGeometry(QtCore.QRect(210, 310, 231, 31))
        self.comboBox_7.setStyleSheet(
            "border-style: outset;\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;\n"
            "background-color: rgb(255, 248, 221);"
        )
        self.comboBox_7.setObjectName("comboBox_7")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 255, 81, 23))
        self.pushButton_5.setStyleSheet(
            f"font: 600 {self.font_size} \"{self.font_type}\";\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            "background-color: rgb(255, 251, 212);\n"
            "\n"
            ""
        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 250, 231, 31))
        self.comboBox_2.setStyleSheet(
            "border-style: outset;\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;\n"
            "background-color: rgb(255, 248, 221);"
        )
        self.comboBox_2.setObjectName("comboBox_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(210, 310, 231, 31))
        self.textEdit.setStyleSheet(
            "background-color: rgb(255, 248, 221);\n"
            f"border-radius: {self.border_radius};"
        )
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.page_2)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 370, 231, 31))
        self.textEdit_2.setStyleSheet(
            "background-color: rgb(255, 248, 221);\n"
            f"border-radius: {self.border_radius};"
        )
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 111, 31))
        self.label_3.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 81, 31))
        self.label_4.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        self.label_5.setGeometry(QtCore.QRect(70, 370, 91, 31))
        self.label_5.setStyleSheet(f"font: 600 {self.font_size} \"{self.font_type}\";")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(parent=self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(210, 60, 251, 25))
        self.comboBox.setStyleSheet(
            "border-style: outset;\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;"
        )
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setGeometry(QtCore.QRect(220, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily(f"{self.font_type}")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(
            f"font: 600 16pt \"{self.font_type}\";\n"
            "\n"
            ""
        )
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 141, 31))
        self.pushButton_2.setStyleSheet(
            f"font: 600 {self.font_size} \"{self.font_type}\";\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            ""
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 500, 31))
        self.label_2.setStyleSheet(
            f"font: 600 {self.font_size} \"{self.font_type}\";\n"
            "background-color: rgb(255, 251, 212);\n"
            f"border-radius: {self.border_radius};\n"
            "border-width: 1.5px;"
        )
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 730, 281, 21))
        self.label_16.setStyleSheet("font: 8pt \"Lucida Fax\";")
        self.label_16.setObjectName("label_16")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 620, 100, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(101, 41))
        self.pushButton_6.setStyleSheet(
            "background-color: rgb(255, 229, 167);\n"
            "font: italic 30pt \"Palace Script MT\";\n"
            "color: rgb(0, 0, 0);\n"
            "border-style: outset;\n"
            "border-radius: 10px;\n"
            "border-width: 2px;\n"
            "font: bold 30px;\n"
            "\n"
            ""
        )
        self.pushButton_6.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 620, 130, 130))
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setStyleSheet("background-image: url(:/新前置字串/image/link_img.jpg);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(parent=self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.actionChange_Background_Color = QtGui.QAction(parent=MainWindow)
        self.actionChange_Background_Color.setObjectName("actionChange_Background_Color")
        self.actionChange_Text_Type = QtGui.QAction(parent=MainWindow)
        self.actionChange_Text_Type.setObjectName("actionChange_Text_Type")
        self.actionChange_Background_Image = QtGui.QAction(parent=MainWindow)
        self.actionChange_Background_Image.setObjectName("actionChange_Background_Image")
        self.actionBackground_color = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setBold(False)
        self.actionBackground_color.setFont(font)
        self.actionBackground_color.setObjectName("actionBackground_color")
        self.actionbackground_image = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        self.actionbackground_image.setFont(font)
        self.actionbackground_image.setObjectName("actionbackground_image")
        self.actionFont_type = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        self.actionFont_type.setFont(font)
        self.actionFont_type.setObjectName("actionFont_type")
        self.actionAbout_Excel_Filter_Tool = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setBold(False)
        self.actionAbout_Excel_Filter_Tool.setFont(font)
        self.actionAbout_Excel_Filter_Tool.setObjectName("actionAbout_Excel_Filter_Tool")
        self.actionContact = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        self.actionContact.setFont(font)
        self.actionContact.setObjectName("actionContact")
        self.actionBackground_Color = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setBold(True)
        self.actionBackground_Color.setFont(font)
        self.actionBackground_Color.setObjectName("actionBackground_Color")
        self.actionFont_Color = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setBold(True)
        self.actionFont_Color.setFont(font)
        self.actionFont_Color.setObjectName("actionFont_Color")
        self.actionFont_Types = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setBold(True)
        self.actionFont_Types.setFont(font)
        self.actionFont_Types.setObjectName("actionFont_Types")
        self.actionbackground_Image = QtGui.QAction(parent=MainWindow)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setBold(True)
        self.actionbackground_Image.setFont(font)
        self.actionbackground_Image.setObjectName("actionbackground_Image")
        self.menuSetting.addAction(self.actionbackground_Image)
        self.menuSetting.addAction(self.actionBackground_Color)
        self.menuSetting.addAction(self.actionFont_Color)
        self.menuSetting.addAction(self.actionFont_Types)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)


        self.stackedWidget.setCurrentIndex(1)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excel Filter Toolkit"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.radioButton.setText(_translate("MainWindow", "Electronic File"))
        self.radioButton_2.setText(_translate("MainWindow", "Manually Entered File"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse File"))
        self.label_11.setText(_translate("MainWindow", "Sheet Name"))
        self.label_12.setText(_translate("MainWindow", "Show File Path"))
        self.label_13.setText(_translate("MainWindow", "Select Sheet"))
        self.label_14.setText(_translate("MainWindow", "Select Year code"))
        self.label_15.setText(_translate("MainWindow", "      Select File Type"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "代謝症候群"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "過勞量表"))
        self.pushButton_5.setText(_translate("MainWindow", "Confirm"))
        self.label_3.setText(_translate("MainWindow", "Select Sheet"))
        self.label_4.setText(_translate("MainWindow", "Year code"))
        self.label_5.setText(_translate("MainWindow", "Sheet Name"))
        self.comboBox.setItemText(1, _translate("MainWindow", "代謝症候群"))
        self.comboBox.setItemText(2, _translate("MainWindow", "過勞量表"))
        self.label.setText(_translate("MainWindow", "      Select File Type"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse File"))
        self.label_2.setText(_translate("MainWindow", "Show File Path"))
        self.label_16.setText(_translate("MainWindow", "Copyright © 2023 YF Liu. All rights reserved."))
        self.pushButton_6.setText(_translate("MainWindow", "Preview"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionChange_Background_Color.setText(_translate("MainWindow", "Background Color"))
        self.actionChange_Text_Type.setText(_translate("MainWindow", "Text Type"))
        self.actionChange_Background_Image.setText(_translate("MainWindow", "Background Image"))
        self.actionBackground_color.setText(_translate("MainWindow", "Background color"))
        self.actionbackground_image.setText(_translate("MainWindow", "Background image"))
        self.actionFont_type.setText(_translate("MainWindow", "Font type"))
        self.actionAbout_Excel_Filter_Tool.setText(_translate("MainWindow", "About Excel Filter Tool"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
        self.actionBackground_Color.setText(_translate("MainWindow", "Background Color"))
        self.actionFont_Color.setText(_translate("MainWindow", "Font Color"))
        self.actionFont_Types.setText(_translate("MainWindow", "Font Types"))
        self.actionbackground_Image.setText(_translate("MainWindow", "background Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
