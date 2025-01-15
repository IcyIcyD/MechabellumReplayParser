from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.techs import Techs


class UnitData(BaseModel):

    path = Paths.UNIT_DATA

    def __init__(self, element: Element):
        self.id: int = int(element.find("id").text)
        self.techs: Techs = Techs(element.find(Techs.path))
