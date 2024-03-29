from OpenGL.GL       import *
from OpenGL.GLU      import *
from OpenGL.GLUT     import *
from PyQt5.QtOpenGL  import *

def _init_gl(aspect):
    """TMP"""
    glClearDepth(1.0)# clear value for depth buffer [0, 1]
    #glDepthFunc(GL_LESS)# val for depth buffer comparisons, GL_LESS is def value
    glEnable(GL_DEPTH_TEST)# enable depth comparisons
    #glShadeModel(GL_SMOOTH)# smooth shading is default

    glLightfv(GL_LIGHT0, GL_AMBIENT,  [0.3, 0.3, 0.3, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  [  1,   1,   1, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [  1,   1,   1, 0])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)

    glLineWidth(2.5)

    glMatrixMode(GL_PROJECTION)# load projection matrix
    glLoadIdentity()# make projection matrix := eye()
    #              angleY, aspect, zNear, zFar
    gluPerspective(90.0,   aspect, 0.1,   1000.0)# perspective projection matrix
    glMatrixMode(GL_MODELVIEW)# load model view


def initialize_gl():
    """TMP"""
    _init_gl(1.33)


def resize_gl(w, h):
    """TMP"""
    _init_gl(w / h)
