from xml.etree.ElementTree import Element

from models.actions.positions import Positions


class UpgradeTower:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.index: int = int(element.find('Index').text)
