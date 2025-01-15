from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.match_datas import MatchDatas
from models.player_records import PlayerRecords


class BattleRecord(BaseModel):

    path = Paths.ROOT

    def __init__(self, element: Element):
        self.player_records: PlayerRecords = PlayerRecords(element.find(PlayerRecords.path))
        self.match_datas: MatchDatas = MatchDatas(element.find(MatchDatas.path))
