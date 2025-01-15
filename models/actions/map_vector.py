from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel


class MapVector(BaseModel):

    path = Paths.MAP_VECTOR

    def __init__(self, element: Element):
        self.x: int = int(element.find('x').text)
        self.y: int = int(element.find('y').text)
