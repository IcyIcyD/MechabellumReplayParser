from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.tech import Tech


class Techs(BaseModel):

    path = Paths.TECHS

    def __init__(self, element: Element):
        self.tech: list[Tech] = []
        for tech in element.findall(Tech.path):
            self.tech.append(Tech(tech))
