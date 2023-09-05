# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 50, 100, 32))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 100, 100, 32))
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 150, 100, 32))
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 200, 100, 32))
        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(250, 50, 100, 32))
        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(90, 10, 100, 32))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 20, 58, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Aggiungi 1 EUR", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Aggiungi 2 EUR", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Aggiungi 5 EUR", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Azzera card", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Dump card", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"Ricerca card", None))
        self.label.setText("")
    # retranslateUi

