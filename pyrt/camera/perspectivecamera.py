"""
Perspective Camera

This is for a standard perspective camera
"""

from ..math import Vec3, Mat4, Ray, createPerspective4
from ..math.matops import createLookAt4, inverse4
from .camera import Camera


class PerspectiveCamera(Camera):

    """This defines a perspective camera"""

    def __init__(self, width: int = 640, height: int = 480, fov: float = 45) -> None:
        """
        Initialize perspective camera

        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        :param fov: field of view (degree)
        """
        Camera.__init__(self)

        self.width = width
        self.height = height
        znear = 0.1
        zfar = 1000.0
        aspect = width / height
        self.projection = createPerspective4(fov, aspect, znear, zfar)

        # initialize with a view matrix
        self.setView(Vec3(0, -10, 0), Vec3(0, 0, 0), Vec3(0, 0, 1))

    def primaryRay(self, x: float, y: float) -> Ray:
        pass

    def setView(self, eye: Vec3, center: Vec3, up: Vec3):
        """
        Set View Matrix using look-at (from eye to center)

        :param eye: current position
        :param center: position where to look at
        :param up: up-axis when looking at
        :return:
        """
        self.view = createLookAt4(eye, center, up)

        self.matrix = self.projection * self.view
        self.matrixinv = inverse4(self.matrix)
        self.viewinv = inverse4(self.view)

    def setProjection(self, fov: float, width: int, height: int, znear: float, zfar: float):
        """
        Redefine perspective projection.

        :param fov: Field of view
        :param width: width in pixels
        :param height: height in pixels
        :param znear: near-plane
        :param zfar: far-plane
        :return:
        """
        self.width = width
        self.height = height
        aspect = self.width / self.height
        self.projection = createPerspective4(fov, aspect, znear, zfar)
        self.matrix = self.projection * self.view
        self.matrixinv = inverse4(self.matrix)
        self.viewinv = inverse4(self.view)

    def getMatrix(self) -> Mat4:
        """
        Returns the view-projection matrix

        :return: view-projection
        """
        return self.matrix