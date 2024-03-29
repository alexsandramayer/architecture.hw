from typing import List

from .flash import Flash
from .polygonal_model import PolygonalModel
from .camera import Camera


class Scene:
    def __init__(self, id: int, models: List[PolygonalModel], flashes: List[Flash], cameras: List[Camera]):
        self.id = id
        if len(models) > 0:
            self.Models = models
        else:
            raise Exception("Должна быть одна модель")
        self.Flashes = flashes
        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть одна модель")

    def method1(self, flash):
        return flash

    def method2(self, flash, camera):
        return flash