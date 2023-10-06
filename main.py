# Form implementation generated from reading ui file 'kold_launcher_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi()
        self.storeWidget.hide()
        self.ownedWidget.hide()
        self.Menu_Indicator.hide()
    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(900, 600)
        self.MainWindow.setMinimumSize(QtCore.QSize(880, 600))
        self.MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(parent=self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title_bar.setStyleSheet("background-color: none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(parent=self.title_bar)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(parent=self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimize = QtWidgets.QPushButton(parent=self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 2px;        \n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(166, 166, 166);\n"
"}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.clicked.connect(self.MainWindow.showMinimized)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_maximize = QtWidgets.QPushButton(parent=self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 2px;    \n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(166, 166, 166);\n"
"}")
        self.btn_maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/square.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.clicked.connect(self.fullscreen)
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_close = QtWidgets.QPushButton(parent=self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 2px;        \n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgb(184, 76, 78);\n"
"}")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.btn_close.clicked.connect(self.MainWindow.close)
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.content_bar = QtWidgets.QFrame(parent=self.drop_shadow_frame)
        self.content_bar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bar.setObjectName("content_bar")
        self.frame = QtWidgets.QFrame(parent=self.content_bar)
        self.frame.setGeometry(QtCore.QRect(10, 0, 731, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Tabs = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Tabs.setContentsMargins(0, 0, 0, 0)
        self.Tabs.setObjectName("Tabs")
        self.storeBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storeBtn.sizePolicy().hasHeightForWidth())
        self.storeBtn.setSizePolicy(sizePolicy)
        self.storeBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.storeBtn.setFont(font)
        self.storeBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: rgb(168, 168, 168);\n"
"    border-radius: 1px;        \n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(116, 116, 116);\n"
"}")
        self.storeBtn.setObjectName("storeBtn")
        self.storeBtn.clicked.connect(self.store)
        self.Tabs.addWidget(self.storeBtn)
        self.line = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.line.setMaximumSize(QtCore.QSize(16777215, 35))
        self.line.setStyleSheet("background-color: rgb(161, 161, 161)")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.Tabs.addWidget(self.line)
        self.ownedBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ownedBtn.sizePolicy().hasHeightForWidth())
        self.ownedBtn.setSizePolicy(sizePolicy)
        self.ownedBtn.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.ownedBtn.setFont(font)
        self.ownedBtn.setStyleSheet("QPushButton {\n""    border: none;\n""    color: rgb(168, 168, 168);\n""    border-radius: 1px;        \n""    background-color: transparent;\n""}\n""QPushButton:hover {    \n""    background-color: rgb(116, 116, 116);\n""}")
        self.ownedBtn.setObjectName("ownedBtn")
        self.ownedBtn.clicked.connect(self.owned)
        self.Tabs.addWidget(self.ownedBtn)
        self.verticalLayout.addWidget(self.content_bar)
        self.ownedWidget = QtWidgets.QTabWidget(parent=self.content_bar)
        self.ownedWidget.setGeometry(QtCore.QRect(16, 59, 731, 481))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        self.ownedWidget.setFont(font)
        self.ownedWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ownedWidget.setAutoFillBackground(False)
        self.ownedWidget.setStyleSheet("QTabBar::tab {\n"
"  background: rgb(45, 45, 45);\n"
"  color: rgb(168, 168, 168);\n"
"  padding:10px;\n"
"  border: 0px solid rgb(168, 168, 168);\n"
" }\n"
"\n"
"QTabWidget::pane { border: none; }\n"
"\n"
" QTabBar::tab:selected {\n"
"  border-bottom-width: 1px;\n"
" }")
        self.ownedWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.ownedWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.ownedWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.ownedWidget.setUsesScrollButtons(True)
        self.ownedWidget.setDocumentMode(False)
        self.ownedWidget.setTabsClosable(False)
        self.ownedWidget.setTabBarAutoHide(False)
        self.ownedWidget.setObjectName("ownedWidget")
        self.owned_games = QtWidgets.QWidget()
        self.owned_games.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.owned_games.setObjectName("games")
        self.verticalWidget = QtWidgets.QWidget(parent=self.owned_games)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 731, 441))
        self.verticalWidget.setStyleSheet("")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.verticalWidget)
        self.scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 45);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(65, 65, 65);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 2000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(698, 2000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.ownedWidget.addTab(self.owned_games, "")
        self.owned_dlcs = QtWidgets.QWidget()
        self.owned_dlcs.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.owned_dlcs.setObjectName("owned_dlcs")
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.owned_dlcs)
        self.verticalWidget_2.setGeometry(QtCore.QRect(0, 0, 731, 441))
        self.verticalWidget_2.setStyleSheet("")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.verticalWidget_2)
        self.scrollArea_2.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 45);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(65, 65, 65);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 699, 2000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_2)
        self.frame_3.setMinimumSize(QtCore.QSize(698, 2000))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6.addWidget(self.frame_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.ownedWidget.addTab(self.owned_dlcs, "")
        self.Menu_Indicator = QtWidgets.QFrame(parent=self.content_bar)
        self.Menu_Indicator.setGeometry(QtCore.QRect(500, 50, 118, 1))
        self.Menu_Indicator.setStyleSheet("background:rgb(170, 170, 170)")
        self.Menu_Indicator.setLineWidth(1)
        self.Menu_Indicator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.Menu_Indicator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.Menu_Indicator.setObjectName("Menu_Indicator")
        self.storeWidget = QtWidgets.QTabWidget(parent=self.content_bar)
        self.storeWidget.setGeometry(QtCore.QRect(16, 59, 731, 481))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        self.storeWidget.setFont(font)
        self.storeWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.storeWidget.setAutoFillBackground(False)
        self.storeWidget.setStyleSheet("QTabBar::tab {\n"
"  background: rgb(45, 45, 45);\n"
"  color: rgb(168, 168, 168);\n"
"  padding:10px;\n"
"  border: 0px solid rgb(168, 168, 168);\n"
" }\n"
"\n"
"QTabWidget::pane { border: none; }\n"
"\n"
" QTabBar::tab:selected {\n"
"  border-bottom-width: 1px;\n"
" }")
        self.storeWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.storeWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.storeWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.storeWidget.setUsesScrollButtons(True)
        self.storeWidget.setDocumentMode(False)
        self.storeWidget.setTabsClosable(False)
        self.storeWidget.setTabBarAutoHide(False)
        self.storeWidget.setObjectName("storeWidget")
        self.store_games = QtWidgets.QWidget()
        self.store_games.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_games.setObjectName("store_games")
        self.verticalWidget_3 = QtWidgets.QWidget(parent=self.store_games)
        self.verticalWidget_3.setGeometry(QtCore.QRect(0, 0, 731, 441))
        self.verticalWidget_3.setStyleSheet("")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.verticalWidget_3)
        self.scrollArea_3.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 45);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(65, 65, 65);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 699, 2000))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_4.setMinimumSize(QtCore.QSize(698, 2000))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8.addWidget(self.frame_4)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollArea_3)
        self.storeWidget.addTab(self.store_games, "")
        self.store_shop = QtWidgets.QWidget()
        self.store_shop.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_shop.setObjectName("store_shop")
        self.verticalWidget_5 = QtWidgets.QWidget(parent=self.store_shop)
        self.verticalWidget_5.setGeometry(QtCore.QRect(0, 0, 731, 441))
        self.verticalWidget_5.setStyleSheet("")
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_5 = QtWidgets.QScrollArea(parent=self.verticalWidget_5)
        self.scrollArea_5.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 45);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(65, 65, 65);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 699, 2000))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_5)
        self.frame_6.setMinimumSize(QtCore.QSize(698, 2000))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_12.addWidget(self.frame_6)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_11.addWidget(self.scrollArea_5)
        self.storeWidget.addTab(self.store_shop, "")
        self.store_dlcs = QtWidgets.QWidget()
        self.store_dlcs.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_dlcs.setObjectName("store_dlcs")
        self.verticalWidget_4 = QtWidgets.QWidget(parent=self.store_dlcs)
        self.verticalWidget_4.setGeometry(QtCore.QRect(0, 0, 731, 441))
        self.verticalWidget_4.setStyleSheet("")
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_4 = QtWidgets.QScrollArea(parent=self.verticalWidget_4)
        self.scrollArea_4.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 45);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(65, 65, 65);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(65, 65, 65);\n"
"    height: 15px;\n"
"    border-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 699, 2000))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_5 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_5.setMinimumSize(QtCore.QSize(698, 2000))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        image_path = 'path_to_your_image.jpg'  # Replace with the path to your image file
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # Create a QLabel to display the image
            image_label = QtWidgets.QLabel(self)
            image_label.setPixmap(pixmap)

            # Add the QLabel to the layout
            self.centralwidget.addWidget(image_label)
        else:
            # Display an error message if the image cannot be loaded
            error_label = QtWidgets.QLabel("Error: Image not found")
            self.centralwidget.addWidget(error_label)

        self.verticalLayout_10.addWidget(self.frame_5)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.addWidget(self.scrollArea_4)
        self.storeWidget.addTab(self.store_dlcs, "")
        self.verticalLayout.addWidget(self.content_bar)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        self.ownedWidget.setCurrentIndex(0)
        self.storeWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.storeBtn.setText(_translate("MainWindow", "STORE"))
        self.ownedBtn.setText(_translate("MainWindow", "OWNED"))
        self.ownedWidget.setTabText(self.ownedWidget.indexOf(self.owned_games), _translate("MainWindow", "Games"))
        self.ownedWidget.setTabText(self.ownedWidget.indexOf(self.owned_dlcs), _translate("MainWindow", "DLCs"))
        self.storeWidget.setTabText(self.storeWidget.indexOf(self.store_games), _translate("MainWindow", "Games"))
        self.storeWidget.setTabText(self.storeWidget.indexOf(self.store_shop), _translate("MainWindow", "Shop"))
        self.storeWidget.setTabText(self.storeWidget.indexOf(self.store_dlcs), _translate("MainWindow", "DLCs"))


    def fullscreen(self):
        if self.MainWindow.isFullScreen():
            self.MainWindow.showNormal()
        else:
            self.MainWindow.showFullScreen()
    def store(self):
        self.storeWidget.show()
        self.ownedWidget.hide()
        self.Menu_Indicator.show()
        self.Menu_Indicator.setGeometry(QtCore.QRect(128, 50, 118, 1))
    def owned(self):
        self.ownedWidget.show()
        self.storeWidget.hide()
        self.Menu_Indicator.show()
        self.Menu_Indicator.setGeometry(QtCore.QRect(500, 50, 118, 1))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main_window = Ui_MainWindow(self)
        self.ui_main_window.setupUi()
        self.offset = None
        # install the event filter on the infoBar widget
        self.ui_main_window.title_bar.installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.ui_main_window.title_bar:
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.Type.MouseMove and self.offset is not None:
                # no need for complex computations: just use the offset to compute
                # "delta" position, and add that to the current one
                self.move(self.pos() - self.offset + event.pos())
                # return True to tell Qt that the event has been accepted and
                # should not be processed any further
                return True
            elif event.type() == QtCore.QEvent.Type.MouseButtonRelease:
                self.offset = None
        # let Qt process any other event
        return super().eventFilter(source, event)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_ = MainWindow()
    MainWindow_.show()
    sys.exit(app.exec())
