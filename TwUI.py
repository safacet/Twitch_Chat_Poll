# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import IRCtw
import threading


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(480, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMinimumSize(QtCore.QSize(460, 540))
        TabWidget.setMaximumSize(QtCore.QSize(512, 612))
        TabWidget.setAutoFillBackground(True)
        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setUsesScrollButtons(False)
        TabWidget.setTabsClosable(False)
        TabWidget.setMovable(False)
        TabWidget.setTabBarAutoHide(False)
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(30, 30, 30, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 70, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.channel_Edit = QtWidgets.QLineEdit(self.tab1)
        self.channel_Edit.setObjectName("channel_Edit")
        self.verticalLayout_2.addWidget(self.channel_Edit)
        self.keyWord_edit = QtWidgets.QLineEdit(self.tab1)
        self.keyWord_edit.setObjectName("keyWord_edit")
        self.verticalLayout_2.addWidget(self.keyWord_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(90, -1, 90, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(self.tab1)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.tab1)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_2.addWidget(self.stop_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.results_browser = QtWidgets.QTextEdit(self.tab1)
        self.results_browser.setReadOnly(True)
        self.results_browser.setObjectName("results_browser")
        self.verticalLayout_3.addWidget(self.results_browser)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        TabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(30, 30, 30, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.idea_select = QtWidgets.QComboBox(self.tab2)
        self.idea_select.setIconSize(QtCore.QSize(16, 16))
        self.idea_select.setObjectName("idea_select")
        self.verticalLayout_4.addWidget(self.idea_select)
        self.detail_browser = QtWidgets.QTextEdit(self.tab2)
        self.detail_browser.setObjectName("detail_browser")
        self.verticalLayout_4.addWidget(self.detail_browser)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        TabWidget.addTab(self.tab2, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

        self.rslt = str()
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Chat Poll"))
        self.label.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:18pt;\">Channel:</span></p></body></html>"))
        self.label_2.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:18pt;\">KeyWord:</span></p></body></html>"))
        self.start_button.setText(_translate("TabWidget", "Start"))
        self.stop_button.setText(_translate("TabWidget", "Stop"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Poll and Results"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab2), _translate("TabWidget", "Detail"))
    
    def start(self):
        self.rslt = self.rslt + "Connecting...\n"
        self.results_browser.setText(self.rslt)
        channel = self.channel_Edit.text()
        channel = str(channel)
        self.results_browser.setText(self.rslt)
        if channel =='':
            self.channel_Edit.setText("This area must be filled")
            self.rslt = self.rslt + "Failure!\n"
            self.results_browser.setText(self.rslt)
            return
        else:
            channel = channel.lower()
        self.keyword = self.keyWord_edit.text()
        if self.keyword == '':
            self.keyWord_edit.setText("This area must be filled")
            self.rslt = self.rslt + "Failure!\n"
            self.results_browser.setText(self.rslt)
            return
        global connection
        connection = IRCtw.IRCclient(self, channel)
        if connection.joinControl == True:
            self.rslt = self.rslt + "Connection Succsesful!\nChat scanning...\n"
            connection.start()
        else:
            self.rslt = self.rslt + "Connection Timeout!\nSomething went wrong... Please try again!"
            connection.quit()
        self.results_browser.setText(self.rslt)
    
    def show(self):
        self.results_browser.setText(self.rslt)
        return    

                
    def stop(self):
        global connection
        connection.quit()
        idea_list = []
        text = str()
        for i in self.rslt:
            text = text + i[0] + " --> " + str(i[2]) + "\n" 
            idea_list.append(i[0])
        text = text + "Connection Ended...\n"
        self.results_browser.setText(text)
        self.idea_select.addItems(idea_list)
        self.idea_select.currentIndexChanged.connect(self.voters_list)
        
        
    def voters_list(self):
        idea = self.idea_select.currentText()
        for i in self.rslt:
            if i[0] == idea:
                voter_stings = i[1]
                voters = voter_stings.replace(" ", "\n")
                self.detail_browser.setText(voters)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
