from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class BuyUnit:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.uid: int = int(element.find('UID').text)
