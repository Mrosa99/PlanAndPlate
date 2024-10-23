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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_PlanAndPlate(object):
    def setupUi(self, PlanAndPlate):
        if not PlanAndPlate.objectName():
            PlanAndPlate.setObjectName(u"PlanAndPlate")
        PlanAndPlate.resize(900, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlanAndPlate.sizePolicy().hasHeightForWidth())
        PlanAndPlate.setSizePolicy(sizePolicy)
        PlanAndPlate.setMinimumSize(QSize(900, 550))
        PlanAndPlate.setMaximumSize(QSize(900, 550))
        self.main_container = QWidget(PlanAndPlate)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"#right_frame{\n"
"	background-color: #0b0b0b;\n"
"}\n"
"#left_frame{\n"
"	background-color: #3c6142;\n"
"}\n"
"#login_container{\n"
"	background-color: #272626;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.main_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.main_container)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.login_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.login_frame)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy1)
        self.left_frame.setMinimumSize(QSize(400, 0))
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.left_frame)

        self.right_frame = QFrame(self.login_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.right_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(75, 50, 75, 50)
        self.login_container = QFrame(self.right_frame)
        self.login_container.setObjectName(u"login_container")
        self.login_container.setStyleSheet(u"")
        self.login_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.login_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 50)
        self.logo_label = QLabel(self.login_container)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QSize(326, 100))
        self.logo_label.setMaximumSize(QSize(326, 180))
        self.logo_label.setPixmap(QPixmap(u"../assets/images/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setWordWrap(False)
        self.logo_label.setMargin(0)

        self.verticalLayout_2.addWidget(self.logo_label)

        self.login_text = QLabel(self.login_container)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setStyleSheet(u"font-size: 18pt; color: white;")
        self.login_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.login_text)

        self.body = QFrame(self.login_container)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"border-color: white;")
        self.body.setFrameShape(QFrame.Shape.NoFrame)
        self.body.setFrameShadow(QFrame.Shadow.Plain)
        self.body.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.username_textfield = QTextEdit(self.body)
        self.username_textfield.setObjectName(u"username_textfield")
        sizePolicy.setHeightForWidth(self.username_textfield.sizePolicy().hasHeightForWidth())
        self.username_textfield.setSizePolicy(sizePolicy)
        self.username_textfield.setMinimumSize(QSize(300, 40))
        self.username_textfield.setMaximumSize(QSize(300, 40))
        self.username_textfield.setStyleSheet(u"border: 3px solid #3c6142;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"background-color: #272626;\n"
"color: rgb(172, 172, 172);")

        self.verticalLayout_3.addWidget(self.username_textfield)

        self.password_textfield = QTextEdit(self.body)
        self.password_textfield.setObjectName(u"password_textfield")
        sizePolicy.setHeightForWidth(self.password_textfield.sizePolicy().hasHeightForWidth())
        self.password_textfield.setSizePolicy(sizePolicy)
        self.password_textfield.setMinimumSize(QSize(300, 40))
        self.password_textfield.setMaximumSize(QSize(300, 40))
        self.password_textfield.setStyleSheet(u"border: 3px solid #3c6142;\n"
"font: 12pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"background-color: #272626;\n"
"color: rgb(172, 172, 172);")

        self.verticalLayout_3.addWidget(self.password_textfield)


        self.verticalLayout_2.addWidget(self.body)

        self.help_button = QPushButton(self.login_container)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.help_button)

        self.login_button = QPushButton(self.login_container)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_2.addWidget(self.login_button)


        self.verticalLayout.addWidget(self.login_container)


        self.horizontalLayout_2.addWidget(self.right_frame)


        self.horizontalLayout.addWidget(self.login_frame)

        PlanAndPlate.setCentralWidget(self.main_container)

        self.retranslateUi(PlanAndPlate)

        QMetaObject.connectSlotsByName(PlanAndPlate)
    # setupUi

    def retranslateUi(self, PlanAndPlate):
        PlanAndPlate.setWindowTitle(QCoreApplication.translate("PlanAndPlate", u"MainWindow", None))
        self.login_text.setText(QCoreApplication.translate("PlanAndPlate", u"Login", None))
        self.username_textfield.setPlaceholderText(QCoreApplication.translate("PlanAndPlate", u"Username", None))
        self.password_textfield.setPlaceholderText(QCoreApplication.translate("PlanAndPlate", u"Password", None))
        self.help_button.setText(QCoreApplication.translate("PlanAndPlate", u"Help logging in?", None))
        self.login_button.setText(QCoreApplication.translate("PlanAndPlate", u"Login", None))
    # retranslateUi

