from typing import List
from ..point3d import Point3D


class Polygon:
    def __init__(self, points: List[Point3D]):
        self.points = points