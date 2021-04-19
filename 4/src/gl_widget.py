from OpenGL.GL            import *
from OpenGL.GLU           import *
from PyQt5.QtOpenGL       import *
from graphics._interfaces import ICanvas, IPoint
from typing               import List
from PyQt5.QtGui          import QColor
from more_itertools       import pairwise


class OpenGLCanvas(ICanvas):
    """
    wrapper(adapter) to use with IGraphicsItem
    """


    @staticmethod
    def draw_lines(points: List[IPoint], color: QColor):
        """draws lines between i-th and (i-1)-th points"""
        glColor3i(color.red(), color.green(), color.blue())
        glBegin(GL_LINES)
        for p1, p2 in pairwise(points):
            glVertex2f(p1.x, p1.y)
            glVertex2f(p2.x, p2.y)
        glEnd()


    @staticmethod
    def fill(points: List[IPoint], color: QColor):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""
        glColor3i(color.red(), color.green(), color.blue())
        glPolygonMode(GL_FRONT, GL_FILL)# polygon rasterization mode

        glBegin(GL_POLYGON)# next vertices will be grouped into triangles
        for p1, p2 in pairwise(points):
            glVertex2f(p1.x, p1.y)
            glVertex2f(p2.x, p2.y)
        glEnd()# end glBegin(GL_TRIANGLES)


    @staticmethod
    def paint_shape():
        """TMP"""
        glColor3f(1.0, 1.5, 0.0)# color for next vertices
        glPolygonMode(GL_FRONT, GL_FILL)# polygon rasterization mode

        glBegin(GL_TRIANGLES)# next vertices will be grouped into triangles
        glVertex3f(2.0, -1.2, -1.0)
        glVertex3f(2.6,  0.0, 5.0)
        glVertex3f(2.9, -1.2, -4.0)
        glEnd()# end glBegin(GL_TRIANGLES)


    @staticmethod
    def paint_gl():
        """TMP"""
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()# identity matrix
        glTranslatef(-2.5, 0.5, -6.0)# move (0, 0, 0)
        OpenGLCanvas.paint_shape()
        glFlush()


    @staticmethod
    def _init_gl(aspect):
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


    @staticmethod
    def initialize_gl():
        """TMP"""
        OpenGLCanvas._init_gl(1.33)


    @staticmethod
    def resize_gl(w, h):
        """TMP"""
        OpenGLCanvas._init_gl(w / h)
