# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QSizePolicy, QTextEdit, QWidget)

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.resize(938, 536)
        self.centralwidget = QWidget(login_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#main_body{\n"
"	background-color: #0b0b0b;\n"
"}\n"
"#left_menu{\n"
"	background-color: #3c6142\n"
"}\n"
"#login_container{\n"
"	background-color:#272626\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QWidget(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.textEdit_6 = QTextEdit(self.left_menu)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(20, 20, 51, 51))
        self.textEdit_7 = QTextEdit(self.left_menu)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(70, 100, 251, 71))
        self.textEdit_8 = QTextEdit(self.left_menu)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(120, 300, 351, 231))

        self.horizontalLayout.addWidget(self.left_menu)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.gridLayout = QGridLayout(self.main_body)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(70, 60, 70, 60)
        self.login_container = QWidget(self.main_body)
        self.login_container.setObjectName(u"login_container")
        self.textEdit = QTextEdit(self.login_container)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 210, 271, 41))
        self.textEdit_2 = QTextEdit(self.login_container)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 270, 271, 41))
        self.textEdit_3 = QTextEdit(self.login_container)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(30, 120, 121, 41))
        self.textEdit_4 = QTextEdit(self.login_container)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(30, 320, 271, 16))
        self.textEdit_5 = QTextEdit(self.login_container)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(30, 180, 271, 16))

        self.gridLayout.addWidget(self.login_container, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.main_body)

        login_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"MainWindow", None))
    # retranslateUi

