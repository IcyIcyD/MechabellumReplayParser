from constants.parsing.paths import Paths
from models.actions.move_unit_data import MoveUnitData
from models.base_model import BaseModel


class MoveUnitDatas(BaseModel):

    path = Paths.MOVE_UNIT_DATAS

    def __init__(self, element):
        self.move_unit_data: list[MoveUnitData] = []
        for move_unit_data in element.findall(MoveUnitData.path):
            self.move_unit_data.append(MoveUnitData(move_unit_data))
