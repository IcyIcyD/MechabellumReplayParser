from xml.etree.ElementTree import Element

from constants.parsing.actions import Actions
from constants.parsing.paths import Paths
from models.actions.active_blueprint import ActiveBlueprint
from models.actions.active_tower_skill import ActiveTowerSkill
from models.actions.buy_unit import BuyUnit
from models.actions.cancel_skill import CancelSkill
from models.actions.choose_reinforcement import ChooseReinforcement
from models.actions.choose_start import ChooseStart
from models.actions.end_deployment import EndDeployment
from models.actions.give_up import GiveUp
from models.actions.level_unit import LevelUnit
from models.actions.move_unit import MoveUnit
from models.actions.tech_unit import TechUnit
from models.actions.unlock_unit import UnlockUnit
from models.actions.upgrade_tower import UpgradeTower
from models.actions.use_device import UseDevice
from models.actions.use_item import UseItem
from models.actions.use_skill import UseSkill
from models.base_model import BaseModel


class MatchActionData(BaseModel):

    path = Paths.MATCH_ACTION_DATA
    ACTION_TO_CLASS_MAPPING = {
        Actions.CHOOSE_START: ChooseStart,
        Actions.CHOOSE_REINFORCEMENT: ChooseReinforcement,
        Actions.MOVE_UNIT: MoveUnit,
        Actions.BUY_UNIT: BuyUnit,
        Actions.TECH_UNIT: TechUnit,
        Actions.USE_ITEM: UseItem,
        Actions.ACTIVE_TOWER_SKILL: ActiveTowerSkill,
        Actions.ACTIVE_BLUEPRINT: ActiveBlueprint,
        Actions.LEVEL_UNIT: LevelUnit,
        Actions.END_DEPLOYMENT: EndDeployment,
        Actions.USE_SKILL: UseSkill,
        Actions.USE_DEVICE: UseDevice,
        Actions.UNLOCK_UNIT: UnlockUnit,
        Actions.UPGRADE_TOWER: UpgradeTower,
        Actions.CANCEL_SKILL: CancelSkill,
        Actions.GIVE_UP: GiveUp
    }

    def __init__(self, element: Element):
        self.type = None
        self.model = None
        xsi_type = element.attrib['{http://www.w3.org/2001/XMLSchema-instance}type']
        if xsi_type not in self.ACTION_TO_CLASS_MAPPING.keys():
            print("[DEBUG] action %s missing in mapping" % xsi_type)
        for k in self.ACTION_TO_CLASS_MAPPING.keys():
            if k == xsi_type:
                self.type = k
                break
        self.model = self.ACTION_TO_CLASS_MAPPING[self.type](element)
