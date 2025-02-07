from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Signal
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QSpinBox, QLabel, QPushButton, QRadioButton, QSizePolicy, QLineEdit
)

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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)

        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName("leftPanel")
        self.leftPanel.setFixedWidth(300)
        self.leftPanel.setFixedHeight(500) 


        self.BF_label = QLabel("Image File:", self.leftPanel)
        self.BF_label.setObjectName("BF_label")
        self.BF_label.setGeometry(QRect(20, 40, 60, 21))
        self.BF_lineEdit = DropLineEdit(self.leftPanel)
        self.BF_lineEdit.setObjectName("BF_lineEdit")
        self.BF_lineEdit.setGeometry(QRect(90, 40, 161, 21))
        self.BF_lineEdit.setClearButtonEnabled(False)
        self.BF_btn = QPushButton("^", self.leftPanel)
        self.BF_btn.setObjectName("BF_btn")
        self.BF_btn.setGeometry(QRect(253, 35, 48, 32))


        self.LF_label = QLabel("Label File:", self.leftPanel)
        self.LF_label.setObjectName("LF_label")
        self.LF_label.setGeometry(QRect(20, 70, 60, 21))
        self.LF_lineEdit = DropLineEdit(self.leftPanel)
        self.LF_lineEdit.setObjectName("LF_lineEdit")
        self.LF_lineEdit.setGeometry(QRect(90, 70, 161, 21))
        self.LF_lineEdit.setEnabled(False)
        self.LF_lineEdit.setClearButtonEnabled(False)
        self.LF_btn = QPushButton("^", self.leftPanel)
        self.LF_btn.setObjectName("LF_btn")
        self.LF_btn.setGeometry(QRect(253, 65, 48, 32))
        self.LF_btn.setEnabled(False)


        self.PF_label = QLabel("Pred File:", self.leftPanel)
        self.PF_label.setObjectName("PF_label")
        self.PF_label.setGeometry(QRect(20, 100, 60, 21))
        self.PF_lineEdit = DropLineEdit(self.leftPanel)
        self.PF_lineEdit.setObjectName("PF_lineEdit")
        self.PF_lineEdit.setGeometry(QRect(90, 100, 161, 21))
        self.PF_lineEdit.setEnabled(False)
        self.PF_lineEdit.setClearButtonEnabled(False)
        self.PF_btn = QPushButton("^", self.leftPanel)
        self.PF_btn.setObjectName("PF_btn")
        self.PF_btn.setGeometry(QRect(253, 95, 48, 32))
        self.PF_btn.setEnabled(False)


        self.BO_label = QLabel("Brain Opacity", self.leftPanel)
        self.BO_label.setObjectName("BO_label")
        self.BO_label.setGeometry(QRect(20, 150, 81, 21))
        self.BO_spinBox = QSpinBox(self.leftPanel)
        self.BO_spinBox.setObjectName("BO_spinBox")
        self.BO_spinBox.setGeometry(QRect(110, 150, 61, 24))
        self.BO_spinBox.setMinimum(1)
        self.BO_spinBox.setMaximum(40)
        self.BO_spinBox.setValue(20)
        self.BO_spinBox.setSingleStep(1)
        self.BO_spinBox.setEnabled(False)


        self.label_label = QLabel("Label", self.leftPanel)
        self.label_label.setObjectName("label_label")
        self.label_label.setGeometry(QRect(20, 200, 60, 21))


        self.radioButton_1 = QRadioButton("1", self.leftPanel)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.setGeometry(QRect(70, 200, 41, 20))
        self.radioButton_1.setEnabled(False)
        self.radioButton_2 = QRadioButton("2", self.leftPanel)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setGeometry(QRect(110, 200, 41, 20))
        self.radioButton_2.setEnabled(False)
        self.radioButton_3 = QRadioButton("3", self.leftPanel)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setGeometry(QRect(150, 200, 41, 20))
        self.radioButton_3.setEnabled(False)
        self.radioButton_4 = QRadioButton("4", self.leftPanel)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setGeometry(QRect(190, 200, 41, 20))
        self.radioButton_4.setEnabled(False)
        self.radioButton_5 = QRadioButton("5", self.leftPanel)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setGeometry(QRect(230, 200, 41, 20))
        self.radioButton_5.setEnabled(False)


        self.label_op_label = QLabel("Label Opacity", self.leftPanel)
        self.label_op_label.setObjectName("label_op_label")
        self.label_op_label.setGeometry(QRect(20, 230, 91, 21))
        self.LO_spinBox = QSpinBox(self.leftPanel)
        self.LO_spinBox.setObjectName("LO_spinBox")
        self.LO_spinBox.setGeometry(QRect(110, 230, 61, 24))
        self.LO_spinBox.setMinimum(1)
        self.LO_spinBox.setMaximum(40)
        self.LO_spinBox.setValue(20)
        self.LO_spinBox.setSingleStep(1)
        self.LO_spinBox.setEnabled(False)


        self.pred_label = QLabel("Pred", self.leftPanel)
        self.pred_label.setObjectName("pred_label")
        self.pred_label.setGeometry(QRect(20, 280, 60, 21))


        self.radioButton_tp = QRadioButton("TP", self.leftPanel)
        self.radioButton_tp.setObjectName("radioButton_tp")
        self.radioButton_tp.setGeometry(QRect(70, 280, 41, 20))
        self.radioButton_tp.setEnabled(False)
        self.radioButton_fp = QRadioButton("FP", self.leftPanel)
        self.radioButton_fp.setObjectName("radioButton_fp")
        self.radioButton_fp.setGeometry(QRect(120, 280, 41, 20))
        self.radioButton_fp.setEnabled(False)
        self.radioButton_fn = QRadioButton("FN", self.leftPanel)
        self.radioButton_fn.setObjectName("radioButton_fn")
        self.radioButton_fn.setGeometry(QRect(170, 280, 41, 20))
        self.radioButton_fn.setEnabled(False)


        self.pred_op_label = QLabel("Pred Opacity", self.leftPanel)
        self.pred_op_label.setObjectName("pred_op_label")
        self.pred_op_label.setGeometry(QRect(20, 310, 91, 21))
        self.PO_spinBox = QSpinBox(self.leftPanel)
        self.PO_spinBox.setObjectName("PO_spinBox")
        self.PO_spinBox.setGeometry(QRect(110, 310, 61, 24))
        self.PO_spinBox.setMinimum(1)
        self.PO_spinBox.setMaximum(40)
        self.PO_spinBox.setValue(20)
        self.PO_spinBox.setSingleStep(1)
        self.PO_spinBox.setEnabled(False)


        self.render_pushButton = QPushButton("Render", self.leftPanel)
        self.render_pushButton.setObjectName("render_pushButton")
        self.render_pushButton.setGeometry(QRect(30, 360, 113, 32))
        self.render_pushButton.setEnabled(False)
        self.save_pushButton = QPushButton("Save", self.leftPanel)
        self.save_pushButton.setObjectName("save_pushButton")
        self.save_pushButton.setGeometry(QRect(160, 360, 113, 32))
        self.save_pushButton.setEnabled(False)


        self.mainLayout.addWidget(self.leftPanel)

        self.render = QWidget(self.centralwidget)
        self.render.setObjectName("render")
        self.render.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainLayout.addWidget(self.render)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
