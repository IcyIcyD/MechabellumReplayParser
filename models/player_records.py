from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.player_record import PlayerRecord


class PlayerRecords(BaseModel):

    path = Paths.PLAYER_RECORDS

    def __init__(self, element):
        self.player_record: list[PlayerRecord] = []
        for player_record in element.findall(PlayerRecord.path):
            self.player_record.append(PlayerRecord(player_record))
