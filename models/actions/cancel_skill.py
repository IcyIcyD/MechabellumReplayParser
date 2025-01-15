from xml.etree.ElementTree import Element


class CancelSkill:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.id: int = int(element.find('ID').text)
        self.skill_index: int = int(element.find('SkillIndex').text)
