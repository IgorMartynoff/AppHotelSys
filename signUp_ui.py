# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUp.ui'
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

class Ui_SignUpForm(object):
    def setupUi(self, SignUpForm):
        if not SignUpForm.objectName():
            SignUpForm.setObjectName(u"SignUpForm")
        SignUpForm.resize(900, 582)
        SignUpForm.setStyleSheet(u"* {\n"
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
        self.verticalLayout = QVBoxLayout(SignUpForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.su_login = QLineEdit(SignUpForm)
        self.su_login.setObjectName(u"su_login")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.su_login.sizePolicy().hasHeightForWidth())
        self.su_login.setSizePolicy(sizePolicy)
        self.su_login.setMinimumSize(QSize(260, 60))
        self.su_login.setMaximumSize(QSize(1300, 130))
        self.su_login.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.su_login)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.su_password = QLineEdit(SignUpForm)
        self.su_password.setObjectName(u"su_password")
        sizePolicy.setHeightForWidth(self.su_password.sizePolicy().hasHeightForWidth())
        self.su_password.setSizePolicy(sizePolicy)
        self.su_password.setMinimumSize(QSize(260, 60))
        self.su_password.setMaximumSize(QSize(1300, 130))
        self.su_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.su_password)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.su_password_2 = QLineEdit(SignUpForm)
        self.su_password_2.setObjectName(u"su_password_2")
        sizePolicy.setHeightForWidth(self.su_password_2.sizePolicy().hasHeightForWidth())
        self.su_password_2.setSizePolicy(sizePolicy)
        self.su_password_2.setMinimumSize(QSize(260, 60))
        self.su_password_2.setMaximumSize(QSize(1300, 130))
        self.su_password_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.su_password_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.su_b_sign_up = QPushButton(SignUpForm)
        self.su_b_sign_up.setObjectName(u"su_b_sign_up")
        sizePolicy.setHeightForWidth(self.su_b_sign_up.sizePolicy().hasHeightForWidth())
        self.su_b_sign_up.setSizePolicy(sizePolicy)
        self.su_b_sign_up.setMinimumSize(QSize(260, 70))
        self.su_b_sign_up.setMaximumSize(QSize(800, 130))
        self.su_b_sign_up.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.su_b_sign_up)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.su_b_login_in = QPushButton(SignUpForm)
        self.su_b_login_in.setObjectName(u"su_b_login_in")
        sizePolicy.setHeightForWidth(self.su_b_login_in.sizePolicy().hasHeightForWidth())
        self.su_b_login_in.setSizePolicy(sizePolicy)
        self.su_b_login_in.setMinimumSize(QSize(260, 70))
        self.su_b_login_in.setMaximumSize(QSize(800, 130))
        self.su_b_login_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.su_b_login_in.setFocusPolicy(Qt.ClickFocus)
        self.su_b_login_in.setInputMethodHints(Qt.ImhNone)
        self.su_b_login_in.setCheckable(False)

        self.verticalLayout_3.addWidget(self.su_b_login_in)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SignUpForm)

        QMetaObject.connectSlotsByName(SignUpForm)
    # setupUi

    def retranslateUi(self, SignUpForm):
        SignUpForm.setWindowTitle(QCoreApplication.translate("SignUpForm", u"Form", None))
        self.su_login.setText("")
        self.su_login.setPlaceholderText(QCoreApplication.translate("SignUpForm", u"Login", None))
        self.su_password.setPlaceholderText(QCoreApplication.translate("SignUpForm", u"Password", None))
        self.su_password_2.setPlaceholderText(QCoreApplication.translate("SignUpForm", u"RePassword", None))
        self.su_b_sign_up.setText(QCoreApplication.translate("SignUpForm", u"Sign up", None))
        self.su_b_login_in.setText(QCoreApplication.translate("SignUpForm", u"Log in", None))
    # retranslateUi

