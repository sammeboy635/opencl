import pygame


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Cube():
    glBegin(GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def showScreen():
    # Remove everything from screen (i.e. displays all white)
    # Remove everything from screen (i.e. displays all white)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset all graphic/shape's position
    Cube()  # Draw a square using our function
    glutSwapBuffers()


def main():
    glutInit()  # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
    display = (800, 600)
    glutInitWindowSize(*display)   # Set the width and height of your window
    # Set the position at which this windows should appear

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0], DOUBLEBUF | OPENGL),None)

    glutInitWindowPosition(0, 0)
    # Give your window a title
    wind = glutCreateWindow("OpenGL Coding Practice")
    # Tell OpenGL to call the showScreen method continuously
    glutDisplayFunc(showScreen)
    # Draw any graphics or shapes in the showScreen function at all times
    glutIdleFunc(showScreen)
    glutMainLoop()


main()
