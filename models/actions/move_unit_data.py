from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.position import Position
from utils import Utils


class MoveUnitData(BaseModel):

    path = Paths.MOVE_UNIT_DATA

    def __init__(self, element: Element):
        self.index: int = int(element.find("unitIndex").text)
        self.is_rotate = Utils.str_to_bool(element.find("isRotate").text)
        self.id: int = int(element.find('unitID').text)
        self.data: Position = Position(element.find(Position.path.lower()))
