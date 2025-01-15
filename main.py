import os
import xml.etree.ElementTree as ET
from tempfile import NamedTemporaryFile

from constants.gameplay.item_ids import ItemIds
from constants.gameplay.officers import Officers
from constants.gameplay.skills import Skills
from constants.gameplay.unit_ids import UNIT_ID_TO_NAME_MAPPER
from constants.parsing.actions import Actions
from models.battle_record import BattleRecord
from utils import Utils


def get_unit_drop_rounds(root: BattleRecord):
    return root.match_datas.match_snapshot_data.unit_reinforce_rounds.ids


def count_tech_stats(model: BattleRecord, tech_stats: dict):

    for player in model.player_records.player_record:

        for unit_data in player.data.unit_datas.unit_data:
            unit_id = unit_data.id
            for unit_tech in [t.data for t in unit_data.techs.tech]:
                tech_stats[unit_id][unit_tech] += 1


def get_tech_stats_report(tech_stats):
    final_str = ""
    final_str += "TECH CHOICES STATS\n"
    for unit in UNIT_ID_TO_NAME_MAPPER.keys():
        tech_dict = tech_stats[unit]
        unit_name = Utils.convert_unit_id_to_name(unit)
        final_str += "[[[[[%s]]]]]\n" % unit_name
        unit_tech_stat = {k: v for k, v in sorted(tech_dict.items(), key=lambda item: item[1], reverse=True)}
        for tech, count in tech_dict.items():
            tech_name = Utils.convert_tech_id_to_name(unit, tech)
            final_str += f"{tech_name}: {count}\n"
        final_str += f"Most popular tech: {Utils.convert_tech_id_to_name(unit, list(unit_tech_stat.keys())[0])}\n"
        final_str += f"Least popular tech: {Utils.convert_tech_id_to_name(unit, list(unit_tech_stat.keys())[-1])}\n"
        final_str += "\n"
    return final_str


def debug_get_unknown_officers(model: BattleRecord):
    final_str = ""
    should_print = False
    for player in model.player_records.player_record:
        unit_drop_rounds = get_unit_drop_rounds(model)
        for round_ in player.player_round_records.player_round_record:
            round_id = round_.round
            relevant_actions = []
            item_ids = ItemIds.__dict__.values()
            skill_ids = Skills.__dict__.values()
            officer_ids = Officers.__dict__.values()
            action_records = round_.action_records.match_action_data
            for action in action_records:
                if action.type in [Actions.UNLOCK_UNIT, Actions.BUY_UNIT, Actions.CHOOSE_REINFORCEMENT]:
                    relevant_actions.append(action)

            for relevant_action in relevant_actions:
                if relevant_action.type == Actions.CHOOSE_REINFORCEMENT:
                    reinforcement_id = relevant_action.model.id
                    if round_id not in unit_drop_rounds:
                        if all([reinforcement_id != 0, reinforcement_id not in item_ids,
                                reinforcement_id not in skill_ids, reinforcement_id not in officer_ids]):
                            final_str += f"[DEBUG] Round {round_id} Unknown reinforcement: {reinforcement_id}. player {player.name}\n"
                            should_print = True
            for officer in round_.player_data.officers:
                if officer not in officer_ids:
                    final_str += f"[DEBUG] Round {round_id} Unknown officer: {officer}. player {player.name}\n"
                    should_print = True
    return final_str if should_print else ""


def get_model(file_name):
    full_replay_name = file_name
    with open(full_replay_name, 'rb') as xmlfile:
        raw_lines = xmlfile.read().splitlines(True)

        while raw_lines[0][0] != '<'.encode('utf-8')[0]:
            raw_lines = raw_lines[1:]
        while any([not any([raw_lines[-1][0] == '<'.encode('utf-8')[0],
                            raw_lines[-1][0] == ' '.encode('utf-8')[0]]),
                   raw_lines[-1][-3] != '>'.encode('utf-8')[0]]):
            raw_lines = raw_lines[:-1]
        raw_data = raw_lines

        with NamedTemporaryFile('w', delete=False, encoding='utf-8') as temp_file:
            temp_path = temp_file.name
            temp_file.write(u'<?xml version="1.0" encoding="utf-8"?>\n')
            for line in raw_data:
                line_str = line.decode('utf-8')
                temp_file.write(line_str)
            temp_file.write(u'</BattleRecord>')  # LMAO HARDCODE

    with open(temp_path, 'r', encoding="utf-8") as temp_file_complete:
        prepared_data = temp_file_complete.read()

    os.remove(temp_path)
    tree = ET.ElementTree(ET.fromstring(prepared_data))
    model = BattleRecord(tree.getroot())
    return model


def get_hp_start_round(model: BattleRecord):
    health_str = ""
    players = []
    for player_record in model.player_records.player_record:
        players.append(player_record.name)
        prev_round_hp = 4500
        for round_data in player_record.player_round_records.player_round_record:
            if round_data.round == 0:
                continue
            current_hp = round_data.player_data.reactor_core
            if round_data.round == 1:
                prev_round_hp = current_hp
            health_str += f"Round {round_data.round}: {current_hp} ({current_hp - prev_round_hp})\n"
            prev_round_hp = current_hp
        health_str += "\n"
    health_str += "\n"
    return health_str


def get_unit_drop_dict(model: BattleRecord):
    drops_dict = {}
    for player_record in model.player_records.player_record:
        unit_drop_rounds = get_unit_drop_rounds(model)
        for round_ in player_record.player_round_records.player_round_record:
            round_id = round_.round
            if round_id not in unit_drop_rounds:
                continue
            action_records = round_.action_records.match_action_data
            for action in action_records:
                if action.type == Actions.CHOOSE_REINFORCEMENT:
                    reinforcement_id = action.model.id
                    if drops_dict.get(reinforcement_id) is None:
                        drops_dict[reinforcement_id] = 1
                    else:
                        drops_dict[reinforcement_id] += 1
    return drops_dict


if __name__ == "__main__":

    REPLAYS_PATH = "./replays"
    TECH_STATS = Utils.get_dict_of_all_techs_count()
    full_drops_dict = {}
    output_string = ""

    if os.path.isdir(REPLAYS_PATH):
        paths = [x[0] for x in os.walk(REPLAYS_PATH)][1:]
    else:
        paths = [REPLAYS_PATH]
    file_names = []
    full_paths = []
    for path in paths:
        file_names.extend(os.listdir(path))
        full_paths.extend(map(lambda pp: os.path.join(path, pp), os.listdir(path)))
    print(len(full_paths))
    for file_name in full_paths:
        # print("[[[[[%s]]]]]" % file_name)
        try:
            model = get_model(file_name)
        except Exception as e:
            print("failure in file name %s" % file_name)
            raise e
        small_drops_dict = get_unit_drop_dict(model)
        for k, v in small_drops_dict.items():
            if full_drops_dict.get(k) is None:
                full_drops_dict[k] = v
            else:
                full_drops_dict[k] += v
        # print(get_hp_start_round(model))
        # debug_line = debug_get_unknown_officers(model)
        # if debug_line:
        #     print(file_name)
        #     print(f"{model.player_records.player_record[0].name} VS {model.player_records.player_record[1].name}")
        #     print(debug_line)
        # count_tech_stats(model, TECH_STATS)
    # print(get_tech_stats_report(TECH_STATS))
    full_drops_dict = {b: bb for b, bb in sorted(full_drops_dict.items(), key=lambda item: item[1], reverse=True)}
    round_sorted_dict = {}
    for g, i in full_drops_dict.items():
        j = str(g)
        j = j[1:]
        round_id = str(int(j[:2]))
        j = j[2:]
        if round_sorted_dict.get(round_id) is None:
            round_sorted_dict[round_id] = {j: i}
        else:
            round_sorted_dict[round_id][j] = i
    round_sorted_dict = {h: hh for h, hh in sorted(round_sorted_dict.items(), key=lambda hhh: int(hhh[0]))}
    for r, blabla in round_sorted_dict.items():
        output_string += "\n\nROUND %s\n\n" % r
        for code, counttt in blabla.items():
            count_drop = code[0]
            level_drop = code[1]
            unit_drop = code[2:]
            s = f"{count_drop}x level {level_drop} {Utils.convert_unit_id_to_name(int(unit_drop))}. Count: {counttt} \n"
            output_string += s
    print(output_string)
    print('END')
