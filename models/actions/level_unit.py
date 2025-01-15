from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class LevelUnit:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.uidx: int = int(element.find('UIDX').text)
