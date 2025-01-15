from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class UseItem:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.item: int = int(element.find('EquipmentID').text)
        self.index: int = int(element.find('UnitIndex').text)
