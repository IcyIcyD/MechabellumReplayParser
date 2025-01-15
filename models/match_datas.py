from xml.etree.ElementTree import Element

from constants.parsing.paths import Paths
from models.base_model import BaseModel
from models.match_snapshot_data import MatchSnapshotData


class MatchDatas(BaseModel):

    path = Paths.MATCH_DATAS

    def __init__(self, element: Element):
        self.match_snapshot_data: MatchSnapshotData = MatchSnapshotData(element.findall(MatchSnapshotData.path)[1])
