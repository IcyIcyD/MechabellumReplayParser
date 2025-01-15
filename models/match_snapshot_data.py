from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.unit_reinforce_rounds import UnitReinforceRounds


class MatchSnapshotData(BaseModel):

    path = Paths.MATCH_SNAPSHOT_DATA

    def __init__(self, element: Element):
        self.unit_reinforce_rounds: UnitReinforceRounds = UnitReinforceRounds(element.find('unitReinforceRounds'))
