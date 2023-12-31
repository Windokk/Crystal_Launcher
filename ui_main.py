from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi()
    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(880, 600)
        self.MainWindow.setMinimumSize(QtCore.QSize(880, 600))
        self.MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.background = QtWidgets.QFrame(parent=self.centralwidget)
        self.background.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;")
        self.background.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(parent=self.background)
        self.title.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title.setStyleSheet("background-color: none;")
        self.title.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(parent=self.title)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 40))
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
        self.frame_btns = QtWidgets.QFrame(parent=self.title)
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
        self.verticalLayout.addWidget(self.title)
        self.content = QtWidgets.QFrame(parent=self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet("background-color: none;")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Menu = QtWidgets.QFrame(parent=self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Menu.sizePolicy().hasHeightForWidth())
        self.Menu.setSizePolicy(sizePolicy)
        self.Menu.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.Menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Menu.setObjectName("Menu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Menu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MenuItems = QtWidgets.QFrame(parent=self.Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuItems.sizePolicy().hasHeightForWidth())
        self.MenuItems.setSizePolicy(sizePolicy)
        self.MenuItems.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuItems.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuItems.setObjectName("MenuItems")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.MenuItems)
        self.horizontalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(parent=self.MenuItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(21, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.storeBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storeBtn.sizePolicy().hasHeightForWidth())
        self.storeBtn.setSizePolicy(sizePolicy)
        self.storeBtn.setMinimumSize(QtCore.QSize(250, 0))
        self.storeBtn.setMaximumSize(QtCore.QSize(16777215, 50))
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
        self.horizontalLayout_4.addWidget(self.storeBtn)
        self.separationLine = QtWidgets.QFrame(parent=self.MenuItems)
        self.separationLine.setMaximumSize(QtCore.QSize(16777215, 35))
        self.separationLine.setStyleSheet("background-color: rgb(161, 161, 161)")
        self.separationLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.separationLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separationLine.setObjectName("separationLine")
        self.horizontalLayout_4.addWidget(self.separationLine)
        self.ownedBtn = QtWidgets.QPushButton(parent=self.MenuItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ownedBtn.sizePolicy().hasHeightForWidth())
        self.ownedBtn.setSizePolicy(sizePolicy)
        self.ownedBtn.setMinimumSize(QtCore.QSize(250, 0))
        self.ownedBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
        self.ownedBtn.setFont(font)
        self.ownedBtn.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: rgb(168, 168, 168);\n"
"    border-radius: 1px;        \n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(116, 116, 116);\n"
"}")
        self.ownedBtn.setObjectName("ownedBtn")
        self.ownedBtn.clicked.connect(self.owned)
        self.horizontalLayout_4.addWidget(self.ownedBtn)
        self.middlespacer = QtWidgets.QFrame(parent=self.MenuItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middlespacer.sizePolicy().hasHeightForWidth())
        self.middlespacer.setSizePolicy(sizePolicy)
        self.middlespacer.setMinimumSize(QtCore.QSize(100, 0))
        self.middlespacer.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.middlespacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.middlespacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.middlespacer.setObjectName("middlespacer")
        self.horizontalLayout_4.addWidget(self.middlespacer)
        self.PlayerIcon = QtWidgets.QFrame(parent=self.MenuItems)
        self.PlayerIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.PlayerIcon.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.PlayerIcon.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.PlayerIcon.setObjectName("PlayerIcon")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.PlayerIcon)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PlayerBtn = QtWidgets.QPushButton(parent=self.PlayerIcon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayerBtn.sizePolicy().hasHeightForWidth())
        self.PlayerBtn.setSizePolicy(sizePolicy)
        self.PlayerBtn.setMaximumSize(QtCore.QSize(5000, 5000))
        self.PlayerBtn.setStyleSheet("QPushButton{\n"
"    border: 2px solid  white;\n"
"    background-color:rgb(45,45,45);\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius:16px;\n"
"\n"
"}")
        self.PlayerBtn.setText("")
        self.PlayerBtn.clicked.connect(self.player_btn)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/default-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PlayerBtn.setIcon(icon3)
        self.PlayerBtn.setIconSize(QtCore.QSize(20, 30))
        self.PlayerBtn.setObjectName("PlayerBtn")
        self.verticalLayout_3.addWidget(self.PlayerBtn)
        self.horizontalLayout_4.addWidget(self.PlayerIcon)
        self.rightspacer = QtWidgets.QFrame(parent=self.MenuItems)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightspacer.sizePolicy().hasHeightForWidth())
        self.rightspacer.setSizePolicy(sizePolicy)
        self.rightspacer.setMaximumSize(QtCore.QSize(24, 16777215))
        self.rightspacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.rightspacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.rightspacer.setObjectName("rightspacer")
        self.horizontalLayout_4.addWidget(self.rightspacer)
        self.horizontalLayout_2.addWidget(self.MenuItems)
        self.verticalLayout_13.addWidget(self.Menu)
        self.MenuIndicatorContainer = QtWidgets.QFrame(parent=self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuIndicatorContainer.sizePolicy().hasHeightForWidth())
        self.MenuIndicatorContainer.setSizePolicy(sizePolicy)
        self.MenuIndicatorContainer.setMaximumSize(QtCore.QSize(100000, 10))
        self.MenuIndicatorContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.MenuIndicatorContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.MenuIndicatorContainer.setObjectName("MenuIndicatorContainer")
        self.MenuIndicator = QtWidgets.QFrame(parent=self.MenuIndicatorContainer)
        self.MenuIndicator.setGeometry(QtCore.QRect(102, 0, 100, 1))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuIndicator.sizePolicy().hasHeightForWidth())
        self.MenuIndicator.setSizePolicy(sizePolicy)
        self.MenuIndicator.setMaximumSize(QtCore.QSize(167, 167))
        self.MenuIndicator.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.MenuIndicator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.MenuIndicator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.MenuIndicator.setObjectName("MenuIndicator")
        self.verticalLayout_13.addWidget(self.MenuIndicatorContainer)
        self.SubMenus = QtWidgets.QFrame(parent=self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubMenus.sizePolicy().hasHeightForWidth())
        self.SubMenus.setSizePolicy(sizePolicy)
        self.SubMenus.setMaximumSize(QtCore.QSize(1677721, 1677721))
        self.SubMenus.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.SubMenus.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.SubMenus.setObjectName("SubMenus")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.SubMenus)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.storeWidget = QtWidgets.QTabWidget(parent=self.SubMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storeWidget.sizePolicy().hasHeightForWidth())
        self.storeWidget.setSizePolicy(sizePolicy)
        self.storeWidget.setMaximumSize(QtCore.QSize(1677725, 1677725))
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
        self.store_games.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_games.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_games.setObjectName("store_games")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.store_games)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.store_games_widgets = QtWidgets.QWidget(parent=self.store_games)
        self.store_games_widgets.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_games_widgets.setStyleSheet("")
        self.store_games_widgets.setObjectName("store_games_widgets")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.store_games_widgets)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.store_games_scrollArea = QtWidgets.QScrollArea(parent=self.store_games_widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_games_scrollArea.sizePolicy().hasHeightForWidth())
        self.store_games_scrollArea.setSizePolicy(sizePolicy)
        self.store_games_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_games_scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
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
        self.store_games_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.store_games_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.store_games_scrollArea.setWidgetResizable(True)
        self.store_games_scrollArea.setObjectName("store_games_scrollArea")
        self.store_games_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.store_games_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 2000))
        self.store_games_scrollAreaWidgetContents.setObjectName("store_games_scrollAreaWidgetContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.store_games_scrollAreaWidgetContents)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.game1 = QtWidgets.QFrame(parent=self.store_games_scrollAreaWidgetContents)
        self.game1.setMinimumSize(QtCore.QSize(698, 2000))
        self.game1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.game1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.game1.setObjectName("game1")
        self.verticalLayout_10.addWidget(self.game1)
        self.store_games_scrollArea.setWidget(self.store_games_scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.store_games_scrollArea)
        self.horizontalLayout_6.addWidget(self.store_games_widgets)
        self.store_games_right_spacer = QtWidgets.QFrame(parent=self.store_games)
        self.store_games_right_spacer.setMaximumSize(QtCore.QSize(108, 16777215))
        self.store_games_right_spacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.store_games_right_spacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.store_games_right_spacer.setObjectName("store_games_right_spacer")
        self.horizontalLayout_6.addWidget(self.store_games_right_spacer)
        self.storeWidget.addTab(self.store_games, "")
        self.store_dlcs = QtWidgets.QWidget()
        self.store_dlcs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_dlcs.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_dlcs.setObjectName("store_dlcs")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.store_dlcs)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.store_dlcs_widgets = QtWidgets.QWidget(parent=self.store_dlcs)
        self.store_dlcs_widgets.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_dlcs_widgets.setStyleSheet("")
        self.store_dlcs_widgets.setObjectName("store_dlcs_widgets")
        self.verticalLayout_91 = QtWidgets.QVBoxLayout(self.store_dlcs_widgets)
        self.verticalLayout_91.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_91.setObjectName("verticalLayout_91")
        self.store_dlcs_scrollArea = QtWidgets.QScrollArea(parent=self.store_dlcs_widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_dlcs_scrollArea.sizePolicy().hasHeightForWidth())
        self.store_dlcs_scrollArea.setSizePolicy(sizePolicy)
        self.store_dlcs_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_dlcs_scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
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
        self.store_dlcs_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.store_dlcs_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.store_dlcs_scrollArea.setWidgetResizable(True)
        self.store_dlcs_scrollArea.setObjectName("store_dlcs_scrollArea")
        self.store_dlcs_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.store_dlcs_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 2000))
        self.store_dlcs_scrollAreaWidgetContents.setObjectName("store_dlcs_scrollAreaWidgetContents")
        self.verticalLayout_101 = QtWidgets.QVBoxLayout(self.store_dlcs_scrollAreaWidgetContents)
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_101.setObjectName("verticalLayout_101")
        self.dlc1 = QtWidgets.QFrame(parent=self.store_dlcs_scrollAreaWidgetContents)
        self.dlc1.setMinimumSize(QtCore.QSize(698, 2000))
        self.dlc1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dlc1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dlc1.setObjectName("dlc1")
        self.verticalLayout_101.addWidget(self.dlc1)
        self.store_dlcs_scrollArea.setWidget(self.store_dlcs_scrollAreaWidgetContents)
        self.verticalLayout_91.addWidget(self.store_dlcs_scrollArea)
        self.horizontalLayout_61.addWidget(self.store_dlcs_widgets)
        self.store_dlcs_right_spacer = QtWidgets.QFrame(parent=self.store_dlcs)
        self.store_dlcs_right_spacer.setMaximumSize(QtCore.QSize(108, 16777215))
        self.store_dlcs_right_spacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.store_dlcs_right_spacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.store_dlcs_right_spacer.setObjectName("store_dlcs_right_spacer")
        self.horizontalLayout_61.addWidget(self.store_dlcs_right_spacer)
        self.storeWidget.addTab(self.store_dlcs, "")
        self.store_shop = QtWidgets.QWidget()
        self.store_shop.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_shop.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.store_shop.setObjectName("store_shop")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.store_shop)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.store_shop_widgets = QtWidgets.QWidget(parent=self.store_shop)
        self.store_shop_widgets.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_shop_widgets.setStyleSheet("")
        self.store_shop_widgets.setObjectName("store_shop_widgets")
        self.verticalLayout_92 = QtWidgets.QVBoxLayout(self.store_shop_widgets)
        self.verticalLayout_92.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_92.setObjectName("verticalLayout_92")
        self.store_shop_scrollArea = QtWidgets.QScrollArea(parent=self.store_shop_widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_shop_scrollArea.sizePolicy().hasHeightForWidth())
        self.store_shop_scrollArea.setSizePolicy(sizePolicy)
        self.store_shop_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.store_shop_scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
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
        self.store_shop_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.store_shop_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.store_shop_scrollArea.setWidgetResizable(True)
        self.store_shop_scrollArea.setObjectName("store_shop_scrollArea")
        self.store_shop_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.store_shop_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 2000))
        self.store_shop_scrollAreaWidgetContents.setObjectName("store_shop_scrollAreaWidgetContents")
        self.verticalLayout_102 = QtWidgets.QVBoxLayout(self.store_shop_scrollAreaWidgetContents)
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_102.setObjectName("verticalLayout_102")
        self.shop_frame = QtWidgets.QFrame(parent=self.store_shop_scrollAreaWidgetContents)
        self.shop_frame.setMinimumSize(QtCore.QSize(698, 2000))
        self.shop_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.shop_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.shop_frame.setObjectName("shop_frame")
        self.verticalLayout_102.addWidget(self.shop_frame)
        self.store_shop_scrollArea.setWidget(self.store_shop_scrollAreaWidgetContents)
        self.verticalLayout_92.addWidget(self.store_shop_scrollArea)
        self.horizontalLayout_62.addWidget(self.store_shop_widgets)
        self.store_shop_right_spacer = QtWidgets.QFrame(parent=self.store_shop)
        self.store_shop_right_spacer.setMaximumSize(QtCore.QSize(108, 16777215))
        self.store_shop_right_spacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.store_shop_right_spacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.store_shop_right_spacer.setObjectName("store_shop_right_spacer")
        self.horizontalLayout_62.addWidget(self.store_shop_right_spacer)
        self.storeWidget.addTab(self.store_shop, "")
        self.horizontalLayout_5.addWidget(self.storeWidget)
        self.ownedWidget = QtWidgets.QTabWidget(parent=self.SubMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ownedWidget.sizePolicy().hasHeightForWidth())
        self.ownedWidget.setSizePolicy(sizePolicy)
        self.ownedWidget.setMaximumSize(QtCore.QSize(1677725, 1677725))
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
        self.owned_games.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_games.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.owned_games.setObjectName("owned_games")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.owned_games)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.owned_games_widgets = QtWidgets.QWidget(parent=self.owned_games)
        self.owned_games_widgets.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_games_widgets.setStyleSheet("")
        self.owned_games_widgets.setObjectName("owned_games_widgets")
        self.verticalLayout_93 = QtWidgets.QVBoxLayout(self.owned_games_widgets)
        self.verticalLayout_93.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_93.setObjectName("verticalLayout_93")
        self.owned_games_scrollArea = QtWidgets.QScrollArea(parent=self.owned_games_widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owned_games_scrollArea.sizePolicy().hasHeightForWidth())
        self.owned_games_scrollArea.setSizePolicy(sizePolicy)
        self.owned_games_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_games_scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
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
        self.owned_games_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.owned_games_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.owned_games_scrollArea.setWidgetResizable(True)
        self.owned_games_scrollArea.setObjectName("owned_games_scrollArea")
        self.owned_games_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.owned_games_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 2000))
        self.owned_games_scrollAreaWidgetContents.setObjectName("owned_games_scrollAreaWidgetContents")
        self.verticalLayout_103 = QtWidgets.QVBoxLayout(self.owned_games_scrollAreaWidgetContents)
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_103.setObjectName("verticalLayout_103")
        self.game11 = QtWidgets.QFrame(parent=self.owned_games_scrollAreaWidgetContents)
        self.game11.setMinimumSize(QtCore.QSize(698, 2000))
        self.game11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.game11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.game11.setObjectName("game11")
        self.verticalLayout_103.addWidget(self.game11)
        self.owned_games_scrollArea.setWidget(self.owned_games_scrollAreaWidgetContents)
        self.verticalLayout_93.addWidget(self.owned_games_scrollArea)
        self.horizontalLayout_63.addWidget(self.owned_games_widgets)
        self.owned_games_right_spacer = QtWidgets.QFrame(parent=self.owned_games)
        self.owned_games_right_spacer.setMaximumSize(QtCore.QSize(108, 16777215))
        self.owned_games_right_spacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.owned_games_right_spacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.owned_games_right_spacer.setObjectName("owned_games_right_spacer")
        self.horizontalLayout_63.addWidget(self.owned_games_right_spacer)
        self.ownedWidget.addTab(self.owned_games, "")
        self.owned_dlcs = QtWidgets.QWidget()
        self.owned_dlcs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_dlcs.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.owned_dlcs.setObjectName("owned_dlcs")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.owned_dlcs)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.owned_dlcs_widgets = QtWidgets.QWidget(parent=self.owned_dlcs)
        self.owned_dlcs_widgets.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_dlcs_widgets.setStyleSheet("")
        self.owned_dlcs_widgets.setObjectName("owned_dlcs_widgets")
        self.verticalLayout_94 = QtWidgets.QVBoxLayout(self.owned_dlcs_widgets)
        self.verticalLayout_94.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_94.setObjectName("verticalLayout_94")
        self.owned_dlcs_scrollArea = QtWidgets.QScrollArea(parent=self.owned_dlcs_widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owned_dlcs_scrollArea.sizePolicy().hasHeightForWidth())
        self.owned_dlcs_scrollArea.setSizePolicy(sizePolicy)
        self.owned_dlcs_scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.owned_dlcs_scrollArea.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
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
        self.owned_dlcs_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.owned_dlcs_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.owned_dlcs_scrollArea.setWidgetResizable(True)
        self.owned_dlcs_scrollArea.setObjectName("owned_dlcs_scrollArea")
        self.owned_dlcs_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.owned_dlcs_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 2000))
        self.owned_dlcs_scrollAreaWidgetContents.setObjectName("owned_dlcs_scrollAreaWidgetContents")
        self.verticalLayout_104 = QtWidgets.QVBoxLayout(self.owned_dlcs_scrollAreaWidgetContents)
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_104.setObjectName("verticalLayout_104")
        self.dlc1_1 = QtWidgets.QFrame(parent=self.owned_dlcs_scrollAreaWidgetContents)
        self.dlc1_1.setMinimumSize(QtCore.QSize(698, 2000))
        self.dlc1_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dlc1_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dlc1_1.setObjectName("dlc1_1")
        self.verticalLayout_104.addWidget(self.dlc1_1)
        self.owned_dlcs_scrollArea.setWidget(self.owned_dlcs_scrollAreaWidgetContents)
        self.verticalLayout_94.addWidget(self.owned_dlcs_scrollArea)
        self.horizontalLayout_64.addWidget(self.owned_dlcs_widgets)
        self.owned_dlcs_right_spacer = QtWidgets.QFrame(parent=self.owned_dlcs)
        self.owned_dlcs_right_spacer.setMaximumSize(QtCore.QSize(108, 16777215))
        self.owned_dlcs_right_spacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.owned_dlcs_right_spacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.owned_dlcs_right_spacer.setObjectName("owned_dlcs_right_spacer")
        self.horizontalLayout_64.addWidget(self.owned_dlcs_right_spacer)
        self.ownedWidget.addTab(self.owned_dlcs, "")
        self.horizontalLayout_5.addWidget(self.ownedWidget)
        self.verticalLayout_13.addWidget(self.SubMenus)
        self.verticalLayout.addWidget(self.content)
        self.bottomBar = QtWidgets.QFrame(parent=self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomBar.sizePolicy().hasHeightForWidth())
        self.bottomBar.setSizePolicy(sizePolicy)
        self.bottomBar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bottomBar.setStyleSheet("background-color: none;")
        self.bottomBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bottomBar)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bottomSpacer = QtWidgets.QFrame(parent=self.bottomBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomSpacer.sizePolicy().hasHeightForWidth())
        self.bottomSpacer.setSizePolicy(sizePolicy)
        self.bottomSpacer.setMaximumSize(QtCore.QSize(1677721, 1677721))
        self.bottomSpacer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomSpacer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottomSpacer.setObjectName("bottomSpacer")
        self.horizontalLayout_7.addWidget(self.bottomSpacer)
        self.resizer = QtWidgets.QFrame(parent=self.bottomBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resizer.sizePolicy().hasHeightForWidth())
        self.resizer.setSizePolicy(sizePolicy)
        self.resizer.setMaximumSize(QtCore.QSize(28, 28))
        self.resizer.setStyleSheet("")
        self.resizer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resizer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resizer.setObjectName("resizer")
        self.resizer_icon = QtWidgets.QLabel(parent=self.resizer)
        self.resizer_icon.setGeometry(QtCore.QRect(4, 0, 21, 21))
        self.resizer_icon.setText("")
        self.resizer_icon.setPixmap(QtGui.QPixmap("icons/resize-dots.png"))
        self.resizer_icon.setScaledContents(True)
        self.resizer_icon.setObjectName("resizer_icon")
        self.size_grip = QtWidgets.QSizeGrip(self.resizer)
        self.size_grip.setGeometry(QtCore.QRect(6, 4, 21, 21))
        self.size_grip.setObjectName("SizeGrip")
        self.horizontalLayout_7.addWidget(self.resizer)
        self.verticalLayout.addWidget(self.bottomBar)
        self.drop_shadow_layout.addWidget(self.background)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        self.ownedWidget.setCurrentIndex(0)
        self.storeWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.storeWidget.hide()
        self.ownedWidget.hide()
        self.MenuIndicator.hide()

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
        self.ownedWidget.hide()
        self.storeWidget.show()
        self.MenuIndicator.show()
        self.MenuIndicator.setGeometry(QtCore.QRect(104, 0, 100, 1))
    def owned(self):
        self.storeWidget.hide()
        self.ownedWidget.show()
        self.MenuIndicator.show()
        self.MenuIndicator.setGeometry(QtCore.QRect(378, 0, 100, 1))
    def player_btn(self):
        print("dd")
