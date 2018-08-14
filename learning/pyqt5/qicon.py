#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class FooWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('icon')
        self.setWindowIcon(QIcon('./learning/desktop/assets/sun.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    foo = FooWindow()
    sys.exit(app.exec_())
