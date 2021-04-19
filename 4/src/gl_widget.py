from OpenGL.GL       import *
from OpenGL.GLU      import *
from PyQt5.QtOpenGL  import *

def paint_shape():
    """TMP"""
    glColor3f(1.0, 1.5, 0.0)# color for next vertices
    glPolygonMode(GL_FRONT, GL_FILL)# polygon rasterization mode

    glBegin(GL_TRIANGLES)# next vertices will be grouped into triangles
    glVertex3f(2.0, -1.2, -1.0)
    glVertex3f(2.6,  0.0, 5.0)
    glVertex3f(2.9, -1.2, -4.0)
    glEnd()# end glBegin(GL_TRIANGLES)

def paint_gl():
    """TMP"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()# identity matrix
    glTranslatef(-2.5, 0.5, -6.0)# move (0, 0, 0)
    paint_shape()
    glFlush()

def init_gl(aspect):
    """TMP"""
    glClearDepth(1.0)# clear value for depth buffer [0, 1]
    #glDepthFunc(GL_LESS)# val for depth buffer comparisons, GL_LESS is def value
    glEnable(GL_DEPTH_TEST)# enable depth comparisons
    #glShadeModel(GL_SMOOTH)# smooth shading is default

    glMatrixMode(GL_PROJECTION)# load projection matrix
    glLoadIdentity()# make projection matrix := eye()
    #              angleY, aspect, zNear, zFar
    gluPerspective(90.0,   aspect, 0.1,   100.0)# perspective projection matrix
    glMatrixMode(GL_MODELVIEW)# load model view

def initialize_gl():
    """TMP"""
    init_gl(1.33)

def resize_gl(w, h):
    """TMP"""
    init_gl(w / h)
