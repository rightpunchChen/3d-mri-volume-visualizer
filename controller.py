import vtk
import imageio
from vtkmodules.util import numpy_support as vtkutil
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox

from ui_window import Ui_MainWindow, DropLineEdit
from utils.vtk_tools import *
from utils.configs import *

class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()
        self.init_actor()
        
        self.brain_image_vtk = None
        self.label_image = None
        self.label_image_vtk = None
        self.pred_image_vtk = None

    def init_actor(self):
        self.brain_actor = None
        self.label_actor = None
        self.tp_actor = None
        self.fp_actor = None
        self.fn_actor = None

    def init(self):
        self.ui.BF_btn.clicked.connect(self.open_brain_file) 
        self.ui.LF_btn.clicked.connect(self.open_label_file)
        self.ui.PF_btn.clicked.connect(self.open_prediction_file)

        self.ui.BO_spinBox.valueChanged.connect(self.set_brain_opacity)
        self.ui.LO_spinBox.valueChanged.connect(self.set_label_opacity)
        self.ui.PO_spinBox.valueChanged.connect(self.set_pred_opacity)
        self.ui.render_pushButton.clicked.connect(self.render_brain)
        self.ui.save_pushButton.clicked.connect(self.save_mp4)

        self.ui.BF_lineEdit.textDropped.connect(self.update_render_button)
        self.ui.LF_lineEdit.textDropped.connect(self.update_label_button)
        self.ui.PF_lineEdit.textDropped.connect(self.update_pred_button)
        self.ui.BF_lineEdit.returnPressed.connect(self.update_render_button)
        self.ui.LF_lineEdit.returnPressed.connect(self.update_label_button)
        self.ui.PF_lineEdit.returnPressed.connect(self.update_pred_button)

        self.layout = QVBoxLayout(self.ui.render)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.vtk_widget = QVTKRenderWindowInteractor(self.ui.render)
        self.layout.addWidget(self.vtk_widget)  # Add the VTK widget to the layout

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(BACKGROUND_COLORS)
        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        self.interactor = self.render_window.GetInteractor()
        self.interactor.Initialize()

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec()

    def open_brain_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"Select NII files", "", "NII Files (*.nii *.nii.gz)")
        self.ui.BF_lineEdit.setText(file_path)
        self.update_render_button()
    
    def open_label_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"Select NII files", "", "NII Files (*.nii *.nii.gz)")
        self.ui.LF_lineEdit.setText(file_path)
        self.update_label_button()
        
    def open_prediction_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"Select NII files", "", "NII Files (*.nii *.nii.gz)")
        self.ui.PF_lineEdit.setText(file_path)
        self.update_pred_button()

    def update_render_button(self):
        file_path = self.ui.BF_lineEdit.text()
        file_exists = check_files(file_path)
        if file_exists:
            self.ui.LF_btn.setEnabled(True)
            self.ui.LF_lineEdit.setEnabled(True)
            self.ui.render_pushButton.setEnabled(True)
            return
        elif not file_exists:
            self.show_error_message(f"File does not exist: {file_path}")

        self.ui.LF_btn.setEnabled(False)
        self.ui.LF_lineEdit.setEnabled(False)
        self.ui.render_pushButton.setEnabled(False)
        self.ui.BO_spinBox.setEnabled(False)
        self.ui.save_pushButton.setEnabled(False)

    def update_label_button(self):
        self.label_image_vtk = None
        self.label_image = None

        file_path = self.ui.LF_lineEdit.text()
        file_exists = check_files(file_path)
        if file_exists:
            self.label_image_vtk = load_image(file_path)
            self.label_image = vtk_img_to_numpy(self.label_image_vtk)
            max_label_value = self.label_image.max()
            for i in range(1, 6):
                getattr(self.ui, f'radioButton_{i}').setEnabled(False)
            for i in range(1, min(int(max_label_value) + 1, LABEL_NUM + 1)):
                getattr(self.ui, f'radioButton_{i}').setEnabled(True)
            self.ui.PF_btn.setEnabled(True)
            self.ui.PF_lineEdit.setEnabled(True)
            return
        elif not file_exists:
            self.show_error_message(f"File does not exist: {file_path}")

        for i in range(1, 6):
            getattr(self.ui, f'radioButton_{i}').setEnabled(False)
        self.ui.PF_btn.setEnabled(False)
        self.ui.PF_lineEdit.setEnabled(False)
    
    def update_pred_button(self):
        self.pred_image_vtk = None

        file_path = self.ui.PF_lineEdit.text()
        file_exists = check_files(file_path)
        if file_exists:
            self.pred_image_vtk = load_image(file_path)
            for i in ['tp', 'fp', 'fn']:
                getattr(self.ui, f'radioButton_{i}').setEnabled(True)
            return
        elif not file_exists:
            self.show_error_message(f"File does not exist: {file_path}")

        for i in ['tp', 'fp', 'fn']:
            getattr(self.ui, f'radioButton_{i}').setEnabled(False)

    def updata_LO_spinBox(self):
        for i in range(1, LABEL_NUM + 1):
            radio_button = getattr(self.ui, f'radioButton_{i}')
            if radio_button.isChecked() and check_files(self.ui.LF_lineEdit.text()):
                self.ui.LO_spinBox.setEnabled(True)
                return
        self.ui.LO_spinBox.setEnabled(False)
        return
        
    def updata_PO_spinBox(self):
        for i in ['tp', 'fp', 'fn']:
            radio_button = getattr(self.ui, f'radioButton_{i}')
            if radio_button.isChecked() and check_files(self.ui.PF_lineEdit.text()):
                self.ui.PO_spinBox.setEnabled(True)
                return
        self.ui.PO_spinBox.setEnabled(False)
        return

    def render_brain(self):
        self.init_actor()
        self.renderer.RemoveAllViewProps()
        self.ui.BO_spinBox.setEnabled(True)
        self.ui.save_pushButton.setEnabled(True)

        brain_file = self.ui.BF_lineEdit.text()
        self.brain_image_vtk = load_image(brain_file)
        self.brain_actor = setup_actor(
            self.brain_image_vtk,
            self.ui.BO_spinBox.value() / 200,
            BRAIN_COLORS
            )
        self.renderer.AddActor(self.brain_actor)

        if self.label_image is not None:
            self.updata_LO_spinBox()
            selected_label = []
            for i in range(1, LABEL_NUM + 1):
                radio_button = getattr(self.ui, f'radioButton_{i}')
                if radio_button.isChecked():
                    selected_label.append(i)
            if selected_label:
                self.label_actor = [None] * (max(selected_label) + 1)
                for l in range(len(selected_label)):
                    if(check_label(self.label_image, selected_label[l])): continue
                    self.label_actor[selected_label[l]] = setup_actor(
                        self.label_image_vtk,
                        self.ui.LO_spinBox.value() / 100,
                        MASK_COLORS[selected_label[l] - 1],
                        selected_label[l]
                        )
                    self.renderer.AddActor(self.label_actor[selected_label[l]])
        
        if self.pred_image_vtk is not None:
            self.updata_PO_spinBox()
            if self.ui.radioButton_tp.isChecked():
                tp = AND(self.label_image_vtk, self.pred_image_vtk)
                if tp is not None:
                    self.tp_actor = setup_actor(
                        tp,
                        self.ui.PO_spinBox.value() / 100,
                        TP_COLOR
                        )
                    self.renderer.AddActor(self.tp_actor)
                    self.ui.PO_spinBox.setEnabled(True)
            if self.ui.radioButton_fp.isChecked():
                fp = false_positive(self.label_image_vtk, self.pred_image_vtk)
                if fp is not None:
                    self.fp_actor = setup_actor(
                        fp,
                        self.ui.PO_spinBox.value()/100,
                        FP_COLOR
                        )
                    self.renderer.AddActor(self.fp_actor)
                    self.ui.PO_spinBox.setEnabled(True)
            if self.ui.radioButton_fn.isChecked():
                fn = false_negative(self.label_image_vtk, self.pred_image_vtk)
                if fn is not None:
                    self.fn_actor = setup_actor(
                        fn,
                        self.ui.PO_spinBox.value()/100,
                        FN_COLOR
                        )
                    self.renderer.AddActor(self.fn_actor)
                    self.ui.PO_spinBox.setEnabled(True)
                        
        set_camera(self.renderer)
        self.render_window.Render()
    
    def set_brain_opacity(self):
        opacity = self.ui.BO_spinBox.value()
        self.brain_actor.GetProperty().SetOpacity(opacity / 200)
        self.render_window.Render()
    
    def set_label_opacity(self):
        opacity = self.ui.LO_spinBox.value()
        for i in range(len(self.label_actor)):
            if self.label_actor[i] is not None:
                self.label_actor[i].GetProperty().SetOpacity(opacity / 100)
        self.render_window.Render()

    def set_pred_opacity(self):
        opacity = self.ui.PO_spinBox.value()
        if self.tp_actor is not None:
            self.tp_actor.GetProperty().SetOpacity(opacity / 100)
        if self.fp_actor is not None:
            self.fp_actor.GetProperty().SetOpacity(opacity / 100)
        if self.fn_actor is not None:
            self.fn_actor.GetProperty().SetOpacity(opacity / 100)
        self.render_window.Render()

    def save_mp4(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save MP4 file", "", "MP4 Files (*.mp4)")
        if file_path:
            window_to_image_filter = vtk.vtkWindowToImageFilter()
            window_to_image_filter.SetInput(self.render_window)
            window_to_image_filter.SetInputBufferTypeToRGB()
            window_to_image_filter.ReadFrontBufferOff()
            window_to_image_filter.SetScale(1)

            self.render_window.SetOffScreenRendering(1)
            self.render_window.SetSize(1920, 1080)
            frames = []

            for _ in range(360):
                self.renderer.GetActiveCamera().Azimuth(1)
                self.render_window.Render()
                window_to_image_filter.Modified()
                window_to_image_filter.Update()
                image_data = window_to_image_filter.GetOutput()
                width, height, _ = image_data.GetDimensions()
                frame = vtkutil.vtk_to_numpy(image_data.GetPointData().GetScalars())
                frame = frame.reshape(height, width, -1)
                frame = frame[::-1]
                frames.append(frame)
            if not file_path.endswith(('.mp4')):
                file_path = file_path + '.mp4'
            imageio.mimsave(file_path, frames, fps=30)
            self.render_window.SetOffScreenRendering(0)
