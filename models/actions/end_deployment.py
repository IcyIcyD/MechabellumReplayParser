from xml.etree.ElementTree import Element


class EndDeployment:
    def __init__(self, element: Element):
        self.time: int = int(element.find('Time').text)
