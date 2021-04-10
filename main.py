#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os
from PyQt5.QtWidgets import *
from untitled import Ui_MainWindow
import requests
from bs4 import BeautifulSoup


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.init()
        self.pushButton.clicked.connect(self.loda)
    def init(self):

        url = 'https://predictioncenter.org/'

        r = requests.get(url=url)

        r.encoding = 'utf-8'

        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)

        ygtvitem = soup.find('strong').find_all("a")

        news_list = soup.find_all('table')
        title_list = []
        abstract_list = []

        for news in news_list:
            news_titles_list = news.find_all('b')
            for news_title in news_titles_list:
                # print(type(news))
                if not news.find('table') and not news_title.find('i'):

                    news_abstract = news.find('a')

                    title_list.append(news_title.text)
                    abstract_list.append(news_abstract.text)
        self.title_list = title_list
        self.abstract_list = abstract_list
        print("Data loading finished!")

    def loda(self):
        self.lineEdit.setText(self.title_list[0])
        self.lineEdit_2.setText(self.title_list[1])
        self.lineEdit_3.setText(self.title_list[2])

        self.textEdit.setText(self.abstract_list[0])
        self.textEdit_2.setText(self.abstract_list[1])
        self.textEdit_3.setText(self.abstract_list[2])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
