# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brain3d.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox, QSlider,
    QWidget)


class DropLineEdit(QLineEdit):
    textDropped = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith(('.nii', '.nii.gz')):
                self.setText(file_path)
                self.textDropped.emit(file_path)
                break

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setFixedSize(900, 500)  # 禁止視窗縮放
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.BF_lineEdit = DropLineEdit(self.centralwidget)
        self.BF_lineEdit.setObjectName(u"BF_lineEdit")
        self.BF_lineEdit.setGeometry(QRect(90, 40, 161, 21))
        self.BF_lineEdit.setClearButtonEnabled(False)
        self.BF_label = QLabel(self.centralwidget)
        self.BF_label.setObjectName(u"BF_label")
        self.BF_label.setGeometry(QRect(20, 40, 60, 21))
        self.BF_lineEdit.setAcceptDrops(True)

        self.LF_label = QLabel(self.centralwidget)
        self.LF_label.setObjectName(u"LF_label")
        self.LF_label.setGeometry(QRect(20, 70, 60, 21))
        self.LF_lineEdit = DropLineEdit(self.centralwidget)
        self.LF_lineEdit.setObjectName(u"LF_lineEdit")
        self.LF_lineEdit.setGeometry(QRect(90, 70, 161, 21))
        self.LF_lineEdit.setEnabled(False)
        self.LF_lineEdit.setClearButtonEnabled(False)
        self.LF_lineEdit.setAcceptDrops(True)

        self.PF_label = QLabel(self.centralwidget)
        self.PF_label.setObjectName(u"PF_label")
        self.PF_label.setGeometry(QRect(20, 100, 60, 21))
        self.PF_lineEdit = DropLineEdit(self.centralwidget)
        self.PF_lineEdit.setObjectName(u"PF_lineEdit")
        self.PF_lineEdit.setGeometry(QRect(90, 100, 161, 21))
        self.PF_lineEdit.setClearButtonEnabled(False)
        self.PF_lineEdit.setAcceptDrops(True)
        self.PF_lineEdit.setEnabled(False)

        self.BF_btn = QPushButton(self.centralwidget)
        self.BF_btn.setObjectName(u"BF_btn")
        self.BF_btn.setGeometry(QRect(253, 35, 51, 32))
        self.LF_btn = QPushButton(self.centralwidget)
        self.LF_btn.setObjectName(u"LF_btn")
        self.LF_btn.setGeometry(QRect(253, 65, 51, 32))
        self.LF_btn.setEnabled(False)
        self.PF_btn = QPushButton(self.centralwidget)
        self.PF_btn.setObjectName(u"PF_btn")
        self.PF_btn.setGeometry(QRect(253, 95, 51, 32))
        self.PF_btn.setEnabled(False)

        self.BO_label = QLabel(self.centralwidget)
        self.BO_label.setObjectName(u"BO_label")
        self.BO_label.setGeometry(QRect(20, 150, 81, 21))
        self.BO_spinBox = QSpinBox(self.centralwidget)
        self.BO_spinBox.setObjectName(u"BO_spinBox")
        self.BO_spinBox.setGeometry(QRect(110, 150, 61, 24))
        self.BO_spinBox.setMinimum(1)
        self.BO_spinBox.setMaximum(40)
        self.BO_spinBox.setValue(20)
        self.BO_spinBox.setSingleStep(1)
        self.BO_spinBox.setEnabled(False)

        self.label_label = QLabel(self.centralwidget)
        self.label_label.setObjectName(u"label_label")
        self.label_label.setGeometry(QRect(20, 200, 60, 21))

        self.label_op_label = QLabel(self.centralwidget)
        self.label_op_label.setObjectName(u"label_op_label")
        self.label_op_label.setGeometry(QRect(20, 230, 91, 21))

        self.LO_spinBox = QSpinBox(self.centralwidget)
        self.LO_spinBox.setObjectName(u"LO_spinBox")
        self.LO_spinBox.setGeometry(QRect(110, 230, 61, 24))
        self.LO_spinBox.setMinimum(1)
        self.LO_spinBox.setMaximum(40)
        self.LO_spinBox.setValue(20)
        self.LO_spinBox.setSingleStep(1)
        self.LO_spinBox.setEnabled(False)

        self.radioButton_1 = QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setGeometry(QRect(70, 200, 41, 20))
        self.radioButton_1.setEnabled(False)
        self.radioButton_1.setChecked(False)
        self.radioButton_1.setAutoExclusive(False)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(110, 200, 41, 20))
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(150, 200, 41, 20))
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(190, 200, 41, 20))
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(230, 200, 41, 20))
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setAutoExclusive(False)

        self.pred_label = QLabel(self.centralwidget)
        self.pred_label.setObjectName(u"pred_label")
        self.pred_label.setGeometry(QRect(20, 280, 60, 21))

        self.radioButton_tp = QRadioButton(self.centralwidget)
        self.radioButton_tp.setObjectName(u"radioButton_tp")
        self.radioButton_tp.setGeometry(QRect(70, 280, 41, 20))
        self.radioButton_tp.setEnabled(False)
        self.radioButton_tp.setAutoExclusive(False)
        self.radioButton_fp = QRadioButton(self.centralwidget)
        self.radioButton_fp.setObjectName(u"radioButton_fp")
        self.radioButton_fp.setGeometry(QRect(120, 280, 41, 20))
        self.radioButton_fp.setEnabled(False)
        self.radioButton_fp.setAutoExclusive(False)
        self.radioButton_fn = QRadioButton(self.centralwidget)
        self.radioButton_fn.setObjectName(u"radioButton_fn")
        self.radioButton_fn.setGeometry(QRect(170, 280, 41, 20))
        self.radioButton_fn.setEnabled(False)
        self.radioButton_fn.setAutoExclusive(False)

        self.pred_op_label = QLabel(self.centralwidget)
        self.pred_op_label.setObjectName(u"pred_op_label")
        self.pred_op_label.setGeometry(QRect(20, 310, 91, 21))

        self.PO_spinBox = QSpinBox(self.centralwidget)
        self.PO_spinBox.setObjectName(u"PO_spinBox")
        self.PO_spinBox.setGeometry(QRect(110, 310, 61, 24))
        self.PO_spinBox.setMinimum(1)
        self.PO_spinBox.setMaximum(40)
        self.PO_spinBox.setValue(20)
        self.PO_spinBox.setSingleStep(1)
        self.PO_spinBox.setEnabled(False)

        self.render = QWidget(self.centralwidget)
        self.render.setObjectName(u"render")
        self.render.setGeometry(QRect(320, 20, 561, 461))

        self.render_pushButton = QPushButton(self.centralwidget)
        self.render_pushButton.setObjectName(u"render_pushButton")
        self.render_pushButton.setGeometry(QRect(30, 360, 113, 32))
        self.render_pushButton.setEnabled(False)

        self.save_pushButton = QPushButton(self.centralwidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(160, 360, 113, 32))
        self.save_pushButton.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BF_label.setText(QCoreApplication.translate("MainWindow", u"Brain File:", None))
        self.LF_label.setText(QCoreApplication.translate("MainWindow", u"Label File:", None))
        self.PF_label.setText(QCoreApplication.translate("MainWindow", u"Pred File:", None))
        self.BO_label.setText(QCoreApplication.translate("MainWindow", u"Brain Opacity", None))
        self.label_label.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_op_label.setText(QCoreApplication.translate("MainWindow", u"Label Opacity", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.render_pushButton.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pred_label.setText(QCoreApplication.translate("MainWindow", u"Pred", None))
        self.pred_op_label.setText(QCoreApplication.translate("MainWindow", u"Pred Opacity", None))
        self.radioButton_tp.setText(QCoreApplication.translate("MainWindow", u"TP", None))
        self.radioButton_fp.setText(QCoreApplication.translate("MainWindow", u"FP", None))
        self.radioButton_fn.setText(QCoreApplication.translate("MainWindow", u"FN", None))
        self.BF_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.LF_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.PF_btn.setText(QCoreApplication.translate("MainWindow", u"^", None))
    # retranslateUi

