from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
def drawFunc():

    # 设置点大小
    glPointSize(3)
    # 只绘制端点
    glBegin(GL_POINTS)
    # 第一个点
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,0.5)
    glVertex2f(0.5,0.0)
    glVertex2f(0.5,0.5)
    glVertex2f(0.2,0.2)
    glEnd()
 
    glFlush()
 
if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"show")
    glutDisplayFunc(drawFunc)
    glutMainLoop()