from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.position import Position
from utils import Utils


class NewUnitData(BaseModel):

    path = Paths.NEW_UNIT_DATA

    def __init__(self, element: Element):
        self.id: int = int(element.find('id').text)
        self.index: int = int(element.find('Index').text)
        self.exp: int = int(element.find('Exp').text)
        self.level: int = int(element.find('Level').text)
        self.equipment_id: int = int(element.find('EquipmentID').text)
        self.is_rotate: bool = Utils.str_to_bool(element.find('IsRotate').text)
        self.sell_supply: int = int(element.find('SellSupply').text)
        self.position: Position = Position(element.find(Position.path))
