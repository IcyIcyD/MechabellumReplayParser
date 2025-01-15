from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.action_records import ActionRecords
from models.base_model import BaseModel
from models.player_data import PlayerData


class PlayerRoundRecord(BaseModel):

    path = Paths.PLAYER_ROUND_RECORD

    def __init__(self, element: Element):
        self.round: int = int(element.find("round").text)
        self.player_data: PlayerData = PlayerData(element.find(Paths.PLAYER_DATA))
        self.action_records: ActionRecords = ActionRecords(element.find(Paths.ACTION_RECORDS))
