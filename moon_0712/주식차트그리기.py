import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtGui import *

form_class = uic.loadUiType("team.ui")[0]

bitcoin = pd.read_csv("BTC-USD.csv",index_col="Date")

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BITCOIN")
        self.setWindowIcon(QIcon("bitbit.png"))

        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn_clicked_2)
        self.pushButton_3.clicked.connect(self.btn_clicked_3)
        self.pushButton_4.clicked.connect(self.btn_clicked_4)
        self.pushButton_5.clicked.connect(self.btn_clicked_5)

        ###
        self.pushButtonCancel.clicked.connect(self.close)
        ###

        self.lineEdit.returnPressed.connect(self.inquiry)




    def btn_clicked(self):
        plt.plot(bitcoin["Open"])
        plt.legend(loc="best")
        plt.grid()
        plt.show()

    def btn_clicked_2(self):
        plt.plot(bitcoin["High"])
        plt.legend(loc="best")
        plt.grid()
        plt.show()

    def btn_clicked_3(self):
        plt.plot(bitcoin["Low"])
        plt.legend(loc="best")
        plt.grid()
        plt.show()

    def btn_clicked_4(self):
        plt.plot(bitcoin["Close"])
        plt.legend(loc="best")
        plt.grid()
        plt.show()

    def btn_clicked_5(self):
        ma5 = bitcoin['Adj Close'].rolling(window=5).mean()
        ma20 = bitcoin['Adj Close'].rolling(window=20).mean()
        ma60 = bitcoin['Adj Close'].rolling(window=60).mean()
        ma120 = bitcoin['Adj Close'].rolling(window=120).mean()
        bitcoin.insert(len(bitcoin.columns), "MA5", ma5)
        bitcoin.insert(len(bitcoin.columns), "MA20", ma20)
        bitcoin.insert(len(bitcoin.columns), "MA60", ma60)
        bitcoin.insert(len(bitcoin.columns), "MA120", ma120)
        plt.plot(bitcoin.index, bitcoin['Adj Close'], label='Adj Close')
        plt.plot(bitcoin.index, bitcoin['MA5'], label='MA5')
        plt.plot(bitcoin.index, bitcoin['MA20'], label='MA20')
        plt.plot(bitcoin.index, bitcoin['MA60'], label='MA60')
        plt.plot(bitcoin.index, bitcoin['MA120'], label='MA120')
        plt.legend(loc="best")
        plt.grid()
        plt.show()



    def inquiry(self):
        date = self.lineEdit.text()
        day_data = bitcoin.loc[date, "Open"]
        self.lineEdit_2.setText(str(day_data))
        day_data2 = bitcoin.loc[date, "High"]
        self.lineEdit_3.setText(str(day_data2))
        day_data3 = bitcoin.loc[date, "Low"]
        self.lineEdit_4.setText(str(day_data3))
        day_data4 = bitcoin.loc[date, "Close"]
        self.lineEdit_5.setText(str(day_data4))




app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()