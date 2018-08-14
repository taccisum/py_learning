#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox
from PyQt5.QtGui import QFont


class FooWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('微软雅黑', 10))

        self.resize(500, 500)
        self.move(100, 100)
        self.setWindowTitle('foo')
        self.setFont(QFont('微软雅黑', 10))

        btn = QPushButton('click me', self)
        btn.move(100, 100)
        btn.setToolTip('hello <b style="color:red">PyQT</b>')
        btn.clicked.connect(lambda: QMessageBox.information(self, 'msg box', 'hello pyqt5'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainform = FooWidget()
    sys.exit(app.exec_())
