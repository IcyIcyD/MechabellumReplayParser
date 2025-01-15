from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class MoveUnit:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.move_unit_datas: MoveUnitDatas = MoveUnitDatas(element.find(MoveUnitDatas.path))
