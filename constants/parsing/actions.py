class Actions:
    CHOOSE_START: str = "PAD_ChooseAdvanceTeam"
    CHOOSE_REINFORCEMENT: str = "PAD_ChooseReinforceItem"
    MOVE_UNIT: str = "PAD_MoveUnit"
    BUY_UNIT: str = "PAD_BuyUnit"
    TECH_UNIT: str = "PAD_UpgradeTechnology"
    USE_ITEM: str = "PAD_UseEquipment"
    ACTIVE_TOWER_SKILL: str = "PAD_ActiveEnergyTowerSkill"
    ACTIVE_BLUEPRINT: str = "PAD_ActiveBlueprint"
    LEVEL_UNIT: str = "PAD_UpgradeUnit"
    END_DEPLOYMENT: str = "PAD_FinishDeploy"
    USE_SKILL: str = "PAD_ReleaseCommanderSkill"
    USE_DEVICE: str = 'PAD_ReleaseContraption'
    UNLOCK_UNIT: str = 'PAD_UnlockUnit'
    UPGRADE_TOWER: str = 'PAD_StrengthenTower'
    CANCEL_SKILL: str = 'PAD_CancelReleaseCommanderSkill'
    GIVE_UP: str = 'PAD_GiveUp'
