from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel


class Tech(BaseModel):

    path = Paths.TECH

    def __init__(self, element: Element):
        self.data: str = element.attrib["data"]
