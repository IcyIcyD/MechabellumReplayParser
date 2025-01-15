from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.player_round_record import PlayerRoundRecord


class PlayerRoundRecords(BaseModel):

    path = Paths.PLAYER_ROUND_RECORDS

    def __init__(self, element: Element):
        self.player_round_record: list[PlayerRoundRecord] = []
        for player_round_record in element.findall(PlayerRoundRecord.path):
            self.player_round_record.append(PlayerRoundRecord(player_round_record))