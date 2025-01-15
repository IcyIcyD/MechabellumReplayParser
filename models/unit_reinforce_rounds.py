from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel


class UnitReinforceRounds(BaseModel):

    path = Paths.UNIT_REINFORCE_ROUNDS

    def __init__(self, element: Element):
        self.ids: list[int] = [int(e.text) for e in element.findall('int')]
