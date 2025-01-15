from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.data import Data
from models.player_round_records import PlayerRoundRecords


class PlayerRecord(BaseModel):

    path = Paths.PLAYER_RECORD

    def __init__(self, element: Element):
        self.name: str = element.find("name").text
        self.data: Data = Data(element.find(Data.path))
        self.player_round_records: PlayerRoundRecords = PlayerRoundRecords(element.find(PlayerRoundRecords.path))
