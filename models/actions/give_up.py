from xml.etree.ElementTree import Element


class GiveUp:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
