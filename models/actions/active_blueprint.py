from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class ActiveBlueprint:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.id: int = int(element.find('ID').text)
