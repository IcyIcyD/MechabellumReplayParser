from constants.parsing.paths import Paths
from models.actions.map_vector import MapVector
from models.base_model import BaseModel


class Positions(BaseModel):

    path = Paths.POSITIONS

    def __init__(self, element):
        self.map_vector: list[MapVector] = []
        for map_vector in element.findall(MapVector.path):
            self.map_vector.append(MapVector(map_vector))
