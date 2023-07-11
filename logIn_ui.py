# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logIn.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LogInForm(object):
    def setupUi(self, LogInForm):
        if not LogInForm.objectName():
            LogInForm.setObjectName(u"LogInForm")
        LogInForm.resize(885, 498)
        LogInForm.setStyleSheet(u"* {\n"
"    font-family: century gothic;\n"
"    font-size: 24px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #202a34;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 25px;\n"
"    padding: 10px;\n"
"    background-color: #d9d9d9;\n"
"    transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #49ebff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #00aaff;\n"
"    border: 2px solid #4d6fe9;\n"
"}\n"
"\n"
"QPushButton,\n"
"QToolButton,\n"
"QMessageBox QPushButton {\n"
"    color: white;\n"
"    background: #4d6fe9;\n"
"    border-radius: 25px;\n"
"    transition: background-color 0.5s ease, transform 0.3s ease, box-shadow 0.3s ease;\n"
"    box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover,\n"
"QMessageBox QPushButton:hover {\n"
"    color: #4d6fe9;\n"
"    background: #4460c7;\n"
"    border-radius: 30px;\n"
"    transform: scale(1.05) rotate(5deg);\n"
"    box-shadow: 0 0 12px rgba(0, 0, 0, 0.3);\n"
""
                        "}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QMessageBox QPushButton:pressed,\n"
"QMessageBox QToolButton:pressed {\n"
"    background: #3a54b0;\n"
"    border-radius: 25px;\n"
"    transform: scale(0.98) rotate(-5deg);\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: #202a34;\n"
"    color: white;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QMessageBox QPushButton,\n"
"QMessageBox QToolButton {\n"
"    background: #4d6fe9;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 12px;\n"
"    border-radius: 10px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"	color: white;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed,\n"
"QMessageBox QToolButton:pressed {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(LogInForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.li_login = QLineEdit(LogInForm)
        self.li_login.setObjectName(u"li_login")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.li_login.sizePolicy().hasHeightForWidth())
        self.li_login.setSizePolicy(sizePolicy)
        self.li_login.setMinimumSize(QSize(260, 60))
        self.li_login.setMaximumSize(QSize(1300, 130))
        self.li_login.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.li_login)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.li_password = QLineEdit(LogInForm)
        self.li_password.setObjectName(u"li_password")
        sizePolicy.setHeightForWidth(self.li_password.sizePolicy().hasHeightForWidth())
        self.li_password.setSizePolicy(sizePolicy)
        self.li_password.setMinimumSize(QSize(260, 60))
        self.li_password.setMaximumSize(QSize(1300, 130))
        self.li_password.setEchoMode(QLineEdit.Password)
        self.li_password.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.li_password)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 4)
        self.verticalLayout_2.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.li_b_log_in = QPushButton(LogInForm)
        self.li_b_log_in.setObjectName(u"li_b_log_in")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.li_b_log_in.sizePolicy().hasHeightForWidth())
        self.li_b_log_in.setSizePolicy(sizePolicy1)
        self.li_b_log_in.setMinimumSize(QSize(260, 70))
        self.li_b_log_in.setMaximumSize(QSize(800, 130))
        self.li_b_log_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.li_b_log_in.setFocusPolicy(Qt.ClickFocus)
        self.li_b_log_in.setInputMethodHints(Qt.ImhNone)
        self.li_b_log_in.setCheckable(False)

        self.verticalLayout_3.addWidget(self.li_b_log_in)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.li_b_sign_up = QPushButton(LogInForm)
        self.li_b_sign_up.setObjectName(u"li_b_sign_up")
        sizePolicy1.setHeightForWidth(self.li_b_sign_up.sizePolicy().hasHeightForWidth())
        self.li_b_sign_up.setSizePolicy(sizePolicy1)
        self.li_b_sign_up.setMinimumSize(QSize(260, 70))
        self.li_b_sign_up.setMaximumSize(QSize(800, 130))
        self.li_b_sign_up.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.li_b_sign_up)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(LogInForm)

        QMetaObject.connectSlotsByName(LogInForm)
    # setupUi

    def retranslateUi(self, LogInForm):
        LogInForm.setWindowTitle(QCoreApplication.translate("LogInForm", u"Form", None))
        self.li_login.setText("")
        self.li_login.setPlaceholderText(QCoreApplication.translate("LogInForm", u"Login", None))
        self.li_password.setPlaceholderText(QCoreApplication.translate("LogInForm", u"Password", None))
        self.li_b_log_in.setText(QCoreApplication.translate("LogInForm", u"Log in", None))
        self.li_b_sign_up.setText(QCoreApplication.translate("LogInForm", u"Sign up", None))
    # retranslateUi

