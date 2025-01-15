from xml.etree.ElementTree import Element

from models.actions.move_unit_datas import MoveUnitDatas


class ActiveTowerSkill:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.skill_id: int = int(element.find('SkillID').text)
