# 3d-mri-volume-visualizer
This application provides a GUI for visualizing brain, label and prediction images for observing the model predictions using VTK and PySide6. Users can load NIFTI files, visualize them in 3D, and save a rotating view as an MP4 file.
![image](https://github.com/rightpunchChen/3d-mri-volume-visualizer/blob/main/demo.png)
## Requirements
- Python 3.9
- Required Python Libraries:
  - imageio==2.37.0
  - imageio-ffmpeg==0.6.0
  - matplotlib==3.9.4
  - numpy==2.0.2
  - PySide6==6.8.1.1
  - vtk==9.4.1

Install dependencies via pip:
```bash
pip install -r requirements.txt
```
## Usage
Run the following command to start the application:

```bash
python run.py
```
