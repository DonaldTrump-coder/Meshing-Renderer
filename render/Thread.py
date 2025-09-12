from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
from render.rendermode import Rendering_mode

class RenderThread(QThread):
    frame_ready = pyqtSignal(np.ndarray)

    def __init__(self, filename):
        super().__init__()
        self.rendering_mode = Rendering_mode.NONE # Initialized Rendering Mode
        self.file=filename
        self.running=True
        # parsing file:

    def set_2DGS_RGB(self,checked):
        if checked:
            self.rendering_mode = Rendering_mode.CKPT_RGB
        else:
            self.rendering_mode = Rendering_mode.NONE

    def set_2DGS_Disp(self,checked):
        if checked:
            self.rendering_mode = Rendering_mode.CKPT_GS
        else:
            self.rendering_mode = Rendering_mode.NONE

    def set_2DGS_Depth(self,checked):
        if checked:
            self.rendering_mode = Rendering_mode.CKPT_DEPTH
        else:
            self.rendering_mode = Rendering_mode.NONE

    def set_mesh_RGB(self,checked):
        if checked:
            self.rendering_mode = Rendering_mode.MESH
        else:
            self.rendering_mode = Rendering_mode.NONE

    def run(self):
        while self.running:
            # rendering cores:
            if self.rendering_mode is Rendering_mode.NONE:
                pass

    def stop(self):
        self.running=False
        self.wait()