from constants.gameplay.technologies import UNIT_ID_TO_TECH_CLASS_MAPPER
from constants.gameplay.unit_ids import UNIT_ID_TO_NAME_MAPPER


class Utils:

    @staticmethod
    def convert_unit_id_to_name(unit_id):
        if unit_id not in UNIT_ID_TO_NAME_MAPPER.keys():
            raise AttributeError(f"Not valid unit id: {unit_id}")
        return UNIT_ID_TO_NAME_MAPPER[unit_id]

    @staticmethod
    def convert_tech_id_to_name(unit_id, tech_id):
        if unit_id not in UNIT_ID_TO_NAME_MAPPER.keys():
            raise AttributeError(f"Not valid unit id: {unit_id}")
        const_class = UNIT_ID_TO_TECH_CLASS_MAPPER[unit_id]
        if not const_class:
            print("[DEBUG] UNIT_ID_TO_TECH_CLASS_MAPPER no mapping to unit %s" % unit_id)
        for k, v in const_class.__dict__.items():
            if v == tech_id:
                return k

    @staticmethod
    def get_dict_of_all_techs_count():
        result_dict = {}
        for unit_id in UNIT_ID_TO_NAME_MAPPER.keys():
            unit_dict = {}
            unit_techs = []
            unit_techs_raw = UNIT_ID_TO_TECH_CLASS_MAPPER[unit_id].__dict__.items()
            for k, v in unit_techs_raw:
                if isinstance(v, str):
                    if not k.startswith("_"):
                        unit_techs.append(v)
            for tech in unit_techs:
                unit_dict[tech] = 0
            result_dict[unit_id] = unit_dict
        return result_dict

    @staticmethod
    def str_to_bool(string):
        if string == "false":
            return False
        elif string == "true":
            return True
        else:
            raise AttributeError("String %s is not boolean" % string)

    @staticmethod
    def parse_unit_drop_reinforcement(reinforcement_id: int):
        reinforcement_str = str(reinforcement_id)
        no_junk = reinforcement_str[2:]
        return {
            'round': int(no_junk[0]),
            'amount': int(no_junk[1]),
            'level': int(no_junk[2]),
            'unit': Utils.convert_unit_id_to_name(int(no_junk[3:]))
        }
