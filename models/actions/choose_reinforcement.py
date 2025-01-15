from xml.etree.ElementTree import Element


class ChooseReinforcement:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
        self.id: int = int(element.find('ID').text)
