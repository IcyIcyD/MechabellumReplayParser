from xml.etree.ElementTree import Element

from models.actions.extra_position import ExtraPosition
from models.position import Position


class UseDevice:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.id: int = int(element.find('ContraptionID').text)
        self.position: Position = Position(element.find(Position.path))
        self.extra_position: ExtraPosition = ExtraPosition(element.find(ExtraPosition.path))
