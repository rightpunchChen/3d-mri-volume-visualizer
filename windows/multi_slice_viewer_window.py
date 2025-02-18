from PySide6.QtCore import QRect
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QLabel
)
from windows.drop_line import DropLineEdit

class MultiSliceViewer_Window(object):
    def __init__(self, centralwidget):
        self.msv_panel = QWidget(centralwidget)
        self.msv_panel.setObjectName("msv_panel")
        self.msv_panel.setFixedWidth(360)

        self.msv_layout = QGridLayout(centralwidget)

        self.viewer_data1_label = QLabel("Image File 1:", self.msv_panel)
        self.viewer_data1_label.setObjectName("viewer_data1_label")
        self.viewer_data1_label.setGeometry(QRect(20, 40, 75, 21))
        self.viewer_data1_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_data1_lineEdit.setObjectName("viewer_data1_lineEdit")
        self.viewer_data1_lineEdit.setGeometry(QRect(100, 40, 200, 21))
        self.viewer_data1_lineEdit.setClearButtonEnabled(False)
        self.viewer_data1_btn = QPushButton("^", self.msv_panel)
        self.viewer_data1_btn.setObjectName("viewer_data1_btn")
        self.viewer_data1_btn.setGeometry(QRect(300, 35, 48, 32))

        self.viewer_data2_label = QLabel("Image File 2:", self.msv_panel)
        self.viewer_data2_label.setObjectName("viewer_data2_label")
        self.viewer_data2_label.setGeometry(QRect(20, 70, 75, 21))
        self.viewer_data2_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_data2_lineEdit.setObjectName("viewer_data2_lineEdit")
        self.viewer_data2_lineEdit.setGeometry(QRect(100, 70, 200, 21))
        self.viewer_data2_lineEdit.setClearButtonEnabled(False)
        self.viewer_data2_btn = QPushButton("^", self.msv_panel)
        self.viewer_data2_btn.setObjectName("viewer_data2_btn")
        self.viewer_data2_btn.setGeometry(QRect(300, 65, 48, 32))

        self.viewer_data3_label = QLabel("Image File 3:", self.msv_panel)
        self.viewer_data3_label.setObjectName("viewer_data3_label")
        self.viewer_data3_label.setGeometry(QRect(20, 100, 75, 21))
        self.viewer_data3_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_data3_lineEdit.setObjectName("viewer_data3_lineEdit")
        self.viewer_data3_lineEdit.setGeometry(QRect(100, 100, 200, 21))
        self.viewer_data3_lineEdit.setClearButtonEnabled(False)
        self.viewer_data3_btn = QPushButton("^", self.msv_panel)
        self.viewer_data3_btn.setObjectName("viewer_data3_btn")
        self.viewer_data3_btn.setGeometry(QRect(300, 95, 48, 32))

        self.viewer_data4_label = QLabel("Image File 4:", self.msv_panel)
        self.viewer_data4_label.setObjectName("viewer_data4_label")
        self.viewer_data4_label.setGeometry(QRect(20, 130, 75, 21))
        self.viewer_data4_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_data4_lineEdit.setObjectName("viewer_data4_lineEdit")
        self.viewer_data4_lineEdit.setGeometry(QRect(100, 130, 200, 21))
        self.viewer_data4_lineEdit.setClearButtonEnabled(False)
        self.viewer_data4_btn = QPushButton("^", self.msv_panel)
        self.viewer_data4_btn.setObjectName("viewer_data4_btn")
        self.viewer_data4_btn.setGeometry(QRect(300, 125, 48, 32))

        self.viewer_pred1_label = QLabel("Pred Image 1:", self.msv_panel)
        self.viewer_pred1_label.setObjectName("viewer_pred1_label")
        self.viewer_pred1_label.setGeometry(QRect(13, 180, 80, 21))
        self.viewer_pred1_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_pred1_lineEdit.setObjectName("viewer_pred1_lineEdit")
        self.viewer_pred1_lineEdit.setGeometry(QRect(100, 180, 200, 21))
        self.viewer_pred1_lineEdit.setClearButtonEnabled(False)
        self.viewer_pred1_lineEdit.setEnabled(False)
        self.viewer_pred1_btn = QPushButton("^", self.msv_panel)
        self.viewer_pred1_btn.setObjectName("viewer_pred1_btn")
        self.viewer_pred1_btn.setGeometry(QRect(300, 175, 48, 32))
        self.viewer_pred1_btn.setEnabled(False)

        self.viewer_pred2_label = QLabel("Pred Image 2:", self.msv_panel)
        self.viewer_pred2_label.setObjectName("viewer_pred2_label")
        self.viewer_pred2_label.setGeometry(QRect(13, 210, 80, 21))
        self.viewer_pred2_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_pred2_lineEdit.setObjectName("viewer_pred2_lineEdit")
        self.viewer_pred2_lineEdit.setGeometry(QRect(100, 210, 200, 21))
        self.viewer_pred2_lineEdit.setClearButtonEnabled(False)
        self.viewer_pred2_lineEdit.setEnabled(False)
        self.viewer_pred2_btn = QPushButton("^", self.msv_panel)
        self.viewer_pred2_btn.setObjectName("viewer_pred2_btn")
        self.viewer_pred2_btn.setGeometry(QRect(300, 205, 48, 32))
        self.viewer_pred2_btn.setEnabled(False)

        self.viewer_pred3_label = QLabel("Pred Image 3:", self.msv_panel)
        self.viewer_pred3_label.setObjectName("viewer_pred3_label")
        self.viewer_pred3_label.setGeometry(QRect(13, 240, 80, 21))
        self.viewer_pred3_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_pred3_lineEdit.setObjectName("viewer_pred3_lineEdit")
        self.viewer_pred3_lineEdit.setGeometry(QRect(100, 240, 200, 21))
        self.viewer_pred3_lineEdit.setClearButtonEnabled(False)
        self.viewer_pred3_lineEdit.setEnabled(False)
        self.viewer_pred3_btn = QPushButton("^", self.msv_panel)
        self.viewer_pred3_btn.setObjectName("viewer_pred3_btn")
        self.viewer_pred3_btn.setGeometry(QRect(300, 235, 48, 32))
        self.viewer_pred3_btn.setEnabled(False)

        self.viewer_pred4_label = QLabel("Pred Image 4:", self.msv_panel)
        self.viewer_pred4_label.setObjectName("viewer_pred4_label")
        self.viewer_pred4_label.setGeometry(QRect(13, 270, 80, 21))
        self.viewer_pred4_lineEdit = DropLineEdit(self.msv_panel)
        self.viewer_pred4_lineEdit.setObjectName("viewer_pred4_lineEdit")
        self.viewer_pred4_lineEdit.setGeometry(QRect(100, 270, 200, 21))
        self.viewer_pred4_lineEdit.setClearButtonEnabled(False)
        self.viewer_pred4_lineEdit.setEnabled(False)
        self.viewer_pred4_btn = QPushButton("^", self.msv_panel)
        self.viewer_pred4_btn.setObjectName("viewer_pred4_btn")
        self.viewer_pred4_btn.setGeometry(QRect(300, 265, 48, 32))
        self.viewer_pred4_btn.setEnabled(False)

        self.render_btn = QPushButton("Render", self.msv_panel)
        self.render_btn.setObjectName("render_btn")
        self.render_btn.setGeometry(QRect(130, 360, 113, 32))
        self.render_btn.setEnabled(False)

        self.msv_layout.addWidget(self.msv_panel, 0, 0, 1, 1)