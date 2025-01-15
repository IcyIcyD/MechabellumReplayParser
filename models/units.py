from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.new_unit_data import NewUnitData


class Units(BaseModel):

    path = Paths.UNITS

    def __init__(self, element: Element):
        self.new_unit_data: list[NewUnitData] = []
        for new_unit_data in element.findall(NewUnitData.path):
            self.new_unit_data.append(NewUnitData(new_unit_data))
