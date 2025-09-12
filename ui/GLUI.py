from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
import numpy as np

class GLWidget(QOpenGLWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.image = None
        self.texture_id = None

    def initialize(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)  # 背景色
        glEnable(GL_DEPTH_TEST)
    
    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def set_image(self, img:np.ndarray):
        self.image = img
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear
        if self.image is None:
            return
        
        h, w, c = self.image.shape
        if self.texture_id is None:
            self.texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        img = np.flipud(img)
        # 上传图像数据到 GPU
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, self.image)

        # 启用纹理绘制一个矩形（覆盖整个窗口）
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(-1, -1)
        glTexCoord2f(1, 0); glVertex2f(1, -1)
        glTexCoord2f(1, 1); glVertex2f(1, 1)
        glTexCoord2f(0, 1); glVertex2f(-1, 1)
        glEnd()
        glDisable(GL_TEXTURE_2D)