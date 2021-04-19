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
        glColor3f(color.red() / 255, color.green() / 255, color.blue() / 255)# color 3i was showing wrong color
        glBegin(GL_LINES)
        for p1, p2 in pairwise(points):
            glVertex2f(p1.x / 100, p1.y / 100)
            glVertex2f(p2.x / 100, p2.y / 100)
        glEnd()


    @staticmethod
    def fill(points: List[IPoint], color: QColor):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""
        glColor3f(color.red() / 255, color.green() / 255, color.blue() / 255)# color 3i was showing wrong color
        glPolygonMode(GL_FRONT, GL_FILL)# polygon rasterization mode

        glBegin(GL_POLYGON)# next vertices will represent a single polygon
        for p1, p2 in pairwise(points):
            glVertex2f(p1.x / 100, p1.y / 100)
            glVertex2f(p2.x / 100, p2.y / 100)
        glEnd()# end glBegin(GL_POLYGON)


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
        gluPerspective(110.0,   aspect, 0.1,   100.0)# perspective projection matrix
        glMatrixMode(GL_MODELVIEW)# load model view


    @staticmethod
    def initialize_gl():
        """TMP"""
        OpenGLCanvas._init_gl(1.33)


    @staticmethod
    def resize_gl(w, h):
        """TMP"""
        OpenGLCanvas._init_gl(w / h)
