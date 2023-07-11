# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 811)
        MainWindow.setStyleSheet(u"* {\n"
"    font-family: century gothic;\n"
"    font-size: 12px;\n"
"}\n"
"QStatusBar,\n"
"QAction,\n"
"QMenu,\n"
"QMenuBar {\n"
"    color: white;\n"
"    background-color: #202a34;\n"
"}\n"
"\n"
"QAction {\n"
"    transition: background-color 0.3s ease-in-out;\n"
"}\n"
"\n"
"QAction:hover {\n"
"    background-color: #555;\n"
"}\n"
"\n"
"QAction:checked {\n"
"    background-color: #888;\n"
"    animation: myAnimation 0.3s ease-in-out;\n"
"}\n"
"\n"
"@keyframes myAnimation {\n"
"    0% {\n"
"        transform: scale(1);\n"
"    }\n"
"    50% {\n"
"        transform: scale(1.1);\n"
"    }\n"
"    100% {\n"
"        transform: scale(1);\n"
"    }\n"
"}\n"
"\n"
"QAction:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #202a34;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"    background-color: #d9d9d9;\n"
"    transition: background-color 0.5s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #49ebff;\n"
"}\n"
"\n"
"Q"
                        "LineEdit:focus {\n"
"    background-color: #00aaff;\n"
"    border: 2px solid #4d6fe9;\n"
"}\n"
"\n"
"QPushButton,\n"
"QToolButton,\n"
"QLabel,\n"
"QMessageBox QPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton,\n"
"QToolButton,\n"
"QMessageBox QPushButton {\n"
"    background: #4d6fe9;\n"
"    border-radius: 10px;\n"
"    transition: background-color 0.5s ease, transform 0.3s ease, box-shadow 0.3s ease;\n"
"    box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover,\n"
"QMessageBox QPushButton:hover {\n"
"    color: #4d6fe9;\n"
"    background: #4460c7;\n"
"    border-radius: 15px;\n"
"    transform: scale(1.05) rotate(5deg);\n"
"    box-shadow: 0 0 12px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QMessageBox QPushButton:pressed,\n"
"QMessageBox QToolButton:pressed {\n"
"    background: #3a54b0;\n"
"    border-radius:10px;\n"
"    transform: scale(0.98) rotate(-5deg);\n"
"    box-shadow: none;\n"
"}\n"
"\n"
"QMessage"
                        "Box {\n"
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
"\n"
"\n"
"\n"
"    QDialog QLineEdit {\n"
"        background-color: #F0F0F0;\n"
"        padding: 4px;\n"
"        border: 1px solid #CCCCCC;\n"
"    }\n"
"    \n"
"    QDialog QPushButton {\n"
"        background-color: #4CAF50;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        font-weight: bold;\n"
"    }\n"
"    \n"
"    QDialog QPushButton:hover {\n"
"        background-color: #4"
                        "5a049;\n"
"    }\n"
"    \n"
"    QDialog QPushButton:pressed {\n"
"        background-color: #3e8e41;\n"
"    }")
        self.actionsearch = QAction(MainWindow)
        self.actionsearch.setObjectName(u"actionsearch")
        self.actionWorld = QAction(MainWindow)
        self.actionWorld.setObjectName(u"actionWorld")
        self.actionExcel = QAction(MainWindow)
        self.actionExcel.setObjectName(u"actionExcel")
        self.e_excel = QAction(MainWindow)
        self.e_excel.setObjectName(u"e_excel")
        self.e_word = QAction(MainWindow)
        self.e_word.setObjectName(u"e_word")
        self.e_csv = QAction(MainWindow)
        self.e_csv.setObjectName(u"e_csv")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.WinPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.header)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(0, 50))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: url(icons/w_menu.ico); /* \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0438\u043a\u043e\u043d\u043a\u0435 \u043d\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"")
        self.left_menu_toggle.setFrameShape(QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.b_menu = QToolButton(self.left_menu_toggle)
        self.b_menu.setObjectName(u"b_menu")
        self.b_menu.setMinimumSize(QSize(50, 25))
        self.b_menu.setMaximumSize(QSize(50, 50))
        self.b_menu.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    color: #fff; /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #333; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #555; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"QToolButton:menu-indicator:hover {\n"
"    background-color: transparent; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435"
                        "\u0434\u0435\u043d\u0438\u0438 \u043d\u0430 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"\n"
"QToolButton:menu-indicator:pressed {\n"
"    background-color: transparent; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/w_menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_menu.setIcon(icon)
        self.b_menu.setIconSize(QSize(48, 48))

        self.horizontalLayout_2.addWidget(self.b_menu)


        self.horizontalLayout_3.addWidget(self.left_menu_toggle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.center_search = QFrame(self.header)
        self.center_search.setObjectName(u"center_search")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_search.sizePolicy().hasHeightForWidth())
        self.center_search.setSizePolicy(sizePolicy)
        self.center_search.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    width: 24px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #333; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #555; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"QToolButton:menu-indicator:hover {\n"
"    background-color: transparent; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043d\u0430 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"\n"
"QToolButton:menu-indi"
                        "cator:pressed {\n"
"    background-color: transparent; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 \u043d\u0430 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"")
        self.center_search.setFrameShape(QFrame.StyledPanel)
        self.center_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.center_search)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.le_h_search = QLineEdit(self.center_search)
        self.le_h_search.setObjectName(u"le_h_search")
        self.le_h_search.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.le_h_search)


        self.horizontalLayout_3.addWidget(self.center_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setStyleSheet(u"QPushButton {\n"
"    background-color: #202a34;\n"
"    color: gray; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: none;\n"
"    padding: 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3a4754;\n"
"    color: gray; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #15202b;\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu_top_buttons.sizePolicy().hasHeightForWidth())
        self.left_menu_top_buttons.setSizePolicy(sizePolicy1)
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu_top_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.b_orders = QPushButton(self.left_menu_top_buttons)
        self.b_orders.setObjectName(u"b_orders")
        icon1 = QIcon()
        icon1.addFile(u"icons/order.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_orders.setIcon(icon1)
        self.b_orders.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_orders)

        self.b_guest_d = QPushButton(self.left_menu_top_buttons)
        self.b_guest_d.setObjectName(u"b_guest_d")
        self.b_guest_d.setMinimumSize(QSize(0, 40))
        icon2 = QIcon()
        icon2.addFile(u"icons/guest.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_guest_d.setIcon(icon2)
        self.b_guest_d.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_guest_d)

        self.b_staff_d = QPushButton(self.left_menu_top_buttons)
        self.b_staff_d.setObjectName(u"b_staff_d")
        self.b_staff_d.setMinimumSize(QSize(0, 40))
        icon3 = QIcon()
        icon3.addFile(u"icons/personal.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_staff_d.setIcon(icon3)
        self.b_staff_d.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_staff_d)

        self.b_apartment_d = QPushButton(self.left_menu_top_buttons)
        self.b_apartment_d.setObjectName(u"b_apartment_d")
        self.b_apartment_d.setMinimumSize(QSize(0, 40))
        icon4 = QIcon()
        icon4.addFile(u"icons/apartament.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_apartment_d.setIcon(icon4)
        self.b_apartment_d.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_apartment_d)

        self.b_role = QPushButton(self.left_menu_top_buttons)
        self.b_role.setObjectName(u"b_role")
        self.b_role.setMinimumSize(QSize(0, 40))
        icon5 = QIcon()
        icon5.addFile(u"icons/roles.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_role.setIcon(icon5)
        self.b_role.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_role)

        self.b_discount = QPushButton(self.left_menu_top_buttons)
        self.b_discount.setObjectName(u"b_discount")
        self.b_discount.setMinimumSize(QSize(0, 40))
        icon6 = QIcon()
        icon6.addFile(u"icons/discount.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_discount.setIcon(icon6)
        self.b_discount.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_discount)

        self.b_useraccount = QPushButton(self.left_menu_top_buttons)
        self.b_useraccount.setObjectName(u"b_useraccount")
        self.b_useraccount.setMinimumSize(QSize(0, 40))
        icon7 = QIcon()
        icon7.addFile(u"icons/ac.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_useraccount.setIcon(icon7)
        self.b_useraccount.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_useraccount)

        self.b_logs = QPushButton(self.left_menu_top_buttons)
        self.b_logs.setObjectName(u"b_logs")
        self.b_logs.setMinimumSize(QSize(0, 40))
        icon8 = QIcon()
        icon8.addFile(u"icons/log.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_logs.setIcon(icon8)
        self.b_logs.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.b_logs)


        self.verticalLayout_2.addWidget(self.left_menu_top_buttons)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.left_menu_bottom_buttons = QFrame(self.left_side_menu)
        self.left_menu_bottom_buttons.setObjectName(u"left_menu_bottom_buttons")
        sizePolicy1.setHeightForWidth(self.left_menu_bottom_buttons.sizePolicy().hasHeightForWidth())
        self.left_menu_bottom_buttons.setSizePolicy(sizePolicy1)
        self.left_menu_bottom_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_bottom_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_menu_bottom_buttons)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.b_logout = QPushButton(self.left_menu_bottom_buttons)
        self.b_logout.setObjectName(u"b_logout")
        icon9 = QIcon()
        icon9.addFile(u"icons/log_out.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_logout.setIcon(icon9)
        self.b_logout.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.b_logout)


        self.verticalLayout_2.addWidget(self.left_menu_bottom_buttons, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"}\n"
"QScrollBar {\n"
"    background-color: #202a34;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    background-color: #3c4858;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: #777;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background-color: #999;\n"
"}\n"
"\n"
"QScrollBar::handle:pressed {\n"
"    background-color: #555;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Vertical Scrollbar */\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"/* Horizontal Scrollbar */\n"
"QScrollBar:horizontal {\n"
"    height: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.table = QTableWidget(self.center_main_items)
        self.table.setObjectName(u"table")
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setLineWidth(0)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table.setGridStyle(Qt.DashLine)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setMinimumSectionSize(30)
        self.table.verticalHeader().setMinimumSectionSize(39)
        self.table.verticalHeader().setDefaultSectionSize(39)

        self.verticalLayout_5.addWidget(self.table)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_side_menu = QFrame(self.body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMaximumSize(QSize(100, 16777215))
        self.right_side_menu.setStyleSheet(u"QPushButton {\n"
"    background-color: #202a34;\n"
"    color: gray; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3a4754;\n"
"    color: gray; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #15202b;\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.right_side_menu)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.b_rs_add = QPushButton(self.right_side_menu)
        self.b_rs_add.setObjectName(u"b_rs_add")
        self.b_rs_add.setMinimumSize(QSize(0, 30))
        icon10 = QIcon()
        icon10.addFile(u"icons/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_rs_add.setIcon(icon10)
        self.b_rs_add.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.b_rs_add)

        self.b_rs_refresh = QPushButton(self.right_side_menu)
        self.b_rs_refresh.setObjectName(u"b_rs_refresh")
        self.b_rs_refresh.setMinimumSize(QSize(0, 30))
        icon11 = QIcon()
        icon11.addFile(u"icons/upd.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_rs_refresh.setIcon(icon11)
        self.b_rs_refresh.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.b_rs_refresh)

        self.b_rs_delete = QPushButton(self.right_side_menu)
        self.b_rs_delete.setObjectName(u"b_rs_delete")
        self.b_rs_delete.setMinimumSize(QSize(0, 30))
        icon12 = QIcon()
        icon12.addFile(u"icons/delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_rs_delete.setIcon(icon12)
        self.b_rs_delete.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.b_rs_delete)

        self.b_rs_update = QPushButton(self.right_side_menu)
        self.b_rs_update.setObjectName(u"b_rs_update")
        icon13 = QIcon()
        icon13.addFile(u"icons/change.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.b_rs_update.setIcon(icon13)
        self.b_rs_update.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.b_rs_update)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.right_side_menu)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 23))
        self.menubar.setStyleSheet(u"font-family: century gothic;\n"
"font-size: 12px;\n"
"\n"
"")
        self.m_export = QMenu(self.menubar)
        self.m_export.setObjectName(u"m_export")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.m_export.menuAction())
        self.m_export.addAction(self.e_excel)
        self.m_export.addAction(self.e_csv)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsearch.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.actionWorld.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.actionExcel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.e_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.e_word.setText(QCoreApplication.translate("MainWindow", u"Word", None))
        self.e_csv.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.b_menu.setText("")
        self.le_h_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.b_orders.setText(QCoreApplication.translate("MainWindow", u"ORDER", None))
        self.b_guest_d.setText(QCoreApplication.translate("MainWindow", u"GUEST", None))
        self.b_staff_d.setText(QCoreApplication.translate("MainWindow", u"STAFF", None))
        self.b_apartment_d.setText(QCoreApplication.translate("MainWindow", u"APT", None))
        self.b_role.setText(QCoreApplication.translate("MainWindow", u"ROLE", None))
        self.b_discount.setText(QCoreApplication.translate("MainWindow", u"DISC", None))
        self.b_useraccount.setText(QCoreApplication.translate("MainWindow", u"A/C", None))
        self.b_logs.setText(QCoreApplication.translate("MainWindow", u"LOGS", None))
        self.b_logout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.b_rs_add.setText("")
        self.b_rs_refresh.setText("")
        self.b_rs_delete.setText("")
        self.b_rs_update.setText("")
        self.m_export.setTitle(QCoreApplication.translate("MainWindow", u"export", None))
    # retranslateUi

