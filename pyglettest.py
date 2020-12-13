from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

import math


class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(
            4, [0, 1, 2, 2, 3, 0], ('v3f', [-0.5, -0.5, 0.0, 0.5, -0.5, 0.0, 0.5, 0.5, 0.0, -0.5, 0.5, 0.0]))


class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 200)
        self.quad = Quad()

        # The vertical plane rotation ranges from -90 (looking straight down) to
        # 90 (looking straight up). The horizontal rotation range is unbounded.
        self.rotation = (0, 0)
        self.position = (0, 0, 0)

    def on_draw(self):
        self.set_3d()
        self.quad.vertices.draw(GL_TRIANGLES)

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.

        """
        width, height = self.get_size()
        glEnable(GL_DEPTH_TEST)
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y = self.rotation
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.position
        glTranslatef(-x, -y, -z)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called when the player moves the mouse.

        Parameters
        ----------
        x, y : int
            The coordinates of the mouse click. Always center of the screen if
            the mouse is captured.
        dx, dy : float
            The movement of the mouse.

        """
        if self.exclusive:
            m = 0.15
            x, y = self.rotation
            x, y = x + dx * m, y + dy * m
            y = max(-90, min(90, y))
            self.rotation = (x, y)


if __name__ == '__main__':
    window = Window(width=800, height=500, caption='test', resizable=True)
    glClearColor(.5, .6, 1, 1)
    window.on_draw()
    pyglet.app.run()
