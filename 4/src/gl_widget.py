from OpenGL.GL       import *
from OpenGL.GLU      import *
from PyQt5.QtOpenGL  import *

def _init_gl(aspect):
    """TMP"""
    glClearDepth(1.0)# clear value for depth buffer [0, 1]
    #glDepthFunc(GL_LESS)# val for depth buffer comparisons, GL_LESS is def value
    glEnable(GL_DEPTH_TEST)# enable depth comparisons
    #glShadeModel(GL_SMOOTH)# smooth shading is default

    glMatrixMode(GL_PROJECTION)# load projection matrix
    glLoadIdentity()# make projection matrix := eye()
    #              angleY, aspect, zNear, zFar
    gluPerspective(110.0,   aspect, 0.1,   100.0)# perspective projection matrix
    glMatrixMode(GL_MODELVIEW)# load model view


def initialize_gl():
    """TMP"""
    _init_gl(1.33)


def resize_gl(w, h):
    """TMP"""
    _init_gl(w / h)
