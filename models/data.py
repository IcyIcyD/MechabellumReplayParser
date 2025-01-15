from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.unit_datas import UnitDatas


class Data(BaseModel):

    path = Paths.DATA

    def __init__(self, element: Element):
        self.unit_datas: UnitDatas = UnitDatas(element.find(UnitDatas.path))
