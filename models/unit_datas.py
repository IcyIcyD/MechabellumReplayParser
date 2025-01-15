from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.unit_data import UnitData


class UnitDatas(BaseModel):

    path = Paths.UNIT_DATAS

    def __init__(self, element: Element):
        self.unit_data: list[UnitData] = []
        for unit_data in element.findall(UnitData.path):
            self.unit_data.append(UnitData(unit_data))
