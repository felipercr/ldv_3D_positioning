# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\felipe.ribeiro\Desktop\felipe\ldv\ldv_3D_positioning\gui\gui_ldv.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_frame.setStyleSheet("background-color: rgb(15, 118, 151);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_frame = QtWidgets.QWidget(self.top_frame)
        self.menu_frame.setMaximumSize(QtCore.QSize(40, 16777215))
        self.menu_frame.setStyleSheet("background-color: rgb(186, 217, 74);")
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.top_menu_button = QtWidgets.QFrame(self.menu_frame)
        self.top_menu_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menu_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_menu_button.setObjectName("top_menu_button")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.top_menu_button)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.m_btn_0 = QtWidgets.QPushButton(self.top_menu_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_btn_0.sizePolicy().hasHeightForWidth())
        self.m_btn_0.setSizePolicy(sizePolicy)
        self.m_btn_0.setMinimumSize(QtCore.QSize(40, 40))
        self.m_btn_0.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    border: 0px solid\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        self.m_btn_0.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_0.setIcon(icon)
        self.m_btn_0.setIconSize(QtCore.QSize(20, 20))
        self.m_btn_0.setObjectName("m_btn_0")
        self.verticalLayout_5.addWidget(self.m_btn_0)
        self.verticalLayout_4.addWidget(self.top_menu_button)
        self.horizontalLayout_2.addWidget(self.menu_frame)
        self.top_frame_2 = QtWidgets.QFrame(self.top_frame)
        self.top_frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.top_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame_2.setObjectName("top_frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.top_frame_2)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.top_buttons = QtWidgets.QFrame(self.top_frame_2)
        self.top_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_buttons.setObjectName("top_buttons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_buttons)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minim = QtWidgets.QPushButton(self.top_buttons)
        self.minim.setMinimumSize(QtCore.QSize(40, 40))
        self.minim.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 118, 151);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 96, 117);\n"
"}")
        self.minim.setObjectName("minim")
        self.horizontalLayout_3.addWidget(self.minim)
        self.aum = QtWidgets.QPushButton(self.top_buttons)
        self.aum.setMinimumSize(QtCore.QSize(40, 40))
        self.aum.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 118, 151);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 96, 117);\n"
"}")
        self.aum.setObjectName("aum")
        self.horizontalLayout_3.addWidget(self.aum)
        self.close = QtWidgets.QPushButton(self.top_buttons)
        self.close.setMinimumSize(QtCore.QSize(40, 40))
        self.close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.close.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(15, 118, 151);\n"
"    border: 0px solid\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 96, 117);\n"
"}")
        self.close.setObjectName("close")
        self.horizontalLayout_3.addWidget(self.close)
        self.horizontalLayout_4.addWidget(self.top_buttons, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.top_frame_2)
        self.verticalLayout.addWidget(self.top_frame)
        self.central_frame = QtWidgets.QFrame(self.centralwidget)
        self.central_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.central_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_frame.setObjectName("central_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.central_frame)
        self.side_menu.setMinimumSize(QtCore.QSize(40, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(40, 16777215))
        self.side_menu.setStyleSheet("background-color: rgb(186, 217, 74);")
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_buttons = QtWidgets.QFrame(self.side_menu)
        self.menu_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menu_buttons.setObjectName("menu_buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_buttons)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.m_btn_1 = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_1.setMinimumSize(QtCore.QSize(0, 40))
        self.m_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_1.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 10px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_1.setIcon(icon1)
        self.m_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.m_btn_1.setObjectName("m_btn_1")
        self.verticalLayout_3.addWidget(self.m_btn_1)
        self.m_btn_2 = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.m_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 10px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_2.setIcon(icon2)
        self.m_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.m_btn_2.setObjectName("m_btn_2")
        self.verticalLayout_3.addWidget(self.m_btn_2)
        self.m_btn_3 = QtWidgets.QPushButton(self.menu_buttons)
        self.m_btn_3.setMinimumSize(QtCore.QSize(0, 40))
        self.m_btn_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m_btn_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(186, 217, 74);\n"
"    padding: 10px;\n"
"    border: 0px solid;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(127, 127, 127);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\felipe.ribeiro\\Desktop\\felipe\\ldv\\ldv_3D_positioning\\gui\\imgs/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.m_btn_3.setIcon(icon3)
        self.m_btn_3.setIconSize(QtCore.QSize(20, 20))
        self.m_btn_3.setObjectName("m_btn_3")
        self.verticalLayout_3.addWidget(self.m_btn_3)
        self.verticalLayout_2.addWidget(self.menu_buttons, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)
        self.widget_2 = QtWidgets.QWidget(self.central_frame)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.main_frame = QtWidgets.QFrame(self.widget_2)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stacked_pages = QtWidgets.QStackedWidget(self.main_frame)
        self.stacked_pages.setMinimumSize(QtCore.QSize(0, 40))
        self.stacked_pages.setObjectName("stacked_pages")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stacked_pages.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stacked_pages.addWidget(self.page_2)
        self.verticalLayout_7.addWidget(self.stacked_pages)
        self.verticalLayout_6.addWidget(self.main_frame)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.central_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minim.setText(_translate("MainWindow", "minim"))
        self.aum.setText(_translate("MainWindow", "aum"))
        self.close.setText(_translate("MainWindow", "close"))
        self.m_btn_1.setText(_translate("MainWindow", "m_btn_1"))
        self.m_btn_2.setText(_translate("MainWindow", "m_btn_2"))
        self.m_btn_3.setText(_translate("MainWindow", "m_btn_3"))
import rsc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())