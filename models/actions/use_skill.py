from xml.etree.ElementTree import Element

from models.actions.positions import Positions


class UseSkill:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.id: int = int(element.find('ID').text)
        self.skill_index: int = int(element.find('SkillIndex').text)
        self.positions: Positions = Positions(element.find(Positions.path))
