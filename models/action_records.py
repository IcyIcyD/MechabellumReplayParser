from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.match_action_data import MatchActionData


class ActionRecords(BaseModel):

    path = Paths.ACTION_RECORDS

    def __init__(self, element: Element):
        self.match_action_data: list[MatchActionData] = []
        for match_action_data in element.findall(MatchActionData.path):
            self.match_action_data.append(MatchActionData(match_action_data))