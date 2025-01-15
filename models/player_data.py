from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.units import Units


class PlayerData(BaseModel):

    path = Paths.PLAYER_DATA

    def __init__(self, element: Element):
        self.reactor_core: int = int(element.find("reactorCore").text)
        self.supply: int = int(element.find("supply").text)
        self.units: Units = Units(element.find(Paths.UNITS))
        self.officers: list[int] = [int(e.text) for e in element.find('officers').findall('int')]
