"""
valid_actions = [
    WindowEvent.PRESS_ARROW_DOWN,
    WindowEvent.PRESS_ARROW_LEFT,
    WindowEvent.PRESS_ARROW_RIGHT,
    WindowEvent.PRESS_ARROW_UP,
    WindowEvent.PRESS_BUTTON_A,
    WindowEvent.PRESS_BUTTON_B,
]
"""


class ActionMapper:
    def __init__(self):
        self.menu = 1
        self.fight_menu = 1
        self.pokemon_menu = 1
        self.bag_menu = 1
        self.pokemon_nr = 1

        self.actions = {
            0: ["m1", 4, "f1", 4, 4],     # attack 1
            1: ["m1", 4, "f2", 4, 4],     # attack 2
            2: ["m1", 4, "f3", 4, 4],     # attack 3
            3: ["m1", 4, "f4", 4, 4],     # attack 4
            4: ["m2", 4, "p1", 4, 4, 4],  # pokemon 1
            5: ["m2", 4, "p2", 4, 4, 4],  # pokemon 2
            6: ["m2", 4, "p3", 4, 4, 4],  # pokemon 3
            7: ["m2", 4, "p4", 4, 4, 4],  # pokemon 4
            8: ["m2", 4, "p5", 4, 4, 4],  # pokemon 5
            9: ["m2", 4, "p6", 4, 4, 4],  # pokemon 6
            10: ["m4", 4, 4],             # run
            11: ["m3", 4, 4, 4],          # pokeball
            12: [7]                       # pass
            # 13: ["m3", 4, "b2"]         # healing
        }

        self.action_size = len(self.actions)

    def reset(self):
        self.menu = 1
        self.fight_menu = 1
        self.pokemon_menu = 1
        self.bag_menu = 1

    def get_action_sequence(self, action):
        action_list = self.actions[action]
        # transforms action string
        new_list = []
        for l in action_list:
            if isinstance(l, str):
                actions = self.go_to(l)
                for a in actions:
                    new_list.append(a)
            else:
                new_list.append(l)
        return new_list

    def go_to(self, space):
        list = []
        want = int(space[1])
        letter = space[0]
        # in first menu
        if letter == "m":
            if self.menu == want:
                return list
            if want % 2 == 0 and self.menu % 2 == 1:
                # right
                list.append(2)
                self.menu += 1
            if want % 2 == 1 and self.menu % 2 == 0:
                # left
                list.append(1)
                self.menu -= 1
            if want < 3 and self.menu > 2:
                # up
                list.append(3)
                self.menu += 2
            if want > 2 and self.menu < 3:
                # down
                list.append(0)
                self.menu -= 1
            return list

        if letter == "f":
            if self.fight_menu == want:
                return list
            while want > self.fight_menu:
                # up
                list.append(3)
                self.fight_menu += 1
            while want < self.fight_menu:
                # down
                list.append(0)
                self.fight_menu -= 1
            return list

        if letter == "p":
            if self.pokemon_menu == want:
                return list
            while want > self.pokemon_menu:
                # up
                list.append(3)
                self.pokemon_menu += 1
            while want < self.pokemon_menu:
                # down
                list.append(0)
                self.pokemon_menu -= 1
            return list


class StateMapper:
    def __init__(self):
        self.features = {
            "in_battle": {
                "player": {
                    "pokemon_nr": 0xD014,
                    "current_hp": [0xD015, 0xD016],  # Range
                    "status": 0xD018,
                    "level": 0xD022,
                    "max_hp": [0xD023, 0xD024],  # Range
                    "attack": [0xD025, 0xD026],  # Range
                    "defense": [0xD027, 0xD028],  # Range
                    "speed": [0xD029, 0xD02A],  # Range
                    "pp_move1": 0xD02D,
                    "pp_move2": 0xD02E,
                    "pp_move3": 0xD02F,
                    "pp_move4": 0xD030,
                },
                "enemy": {
                    "current_hp": [0xCFE6, 0xCFE7],  # Range
                    "level": 0xCFF3,
                    "status": 0xCFE9,
                    "type_1": 0xCFEA,
                    "type_2": 0xCFEB,
                    "max_hp": [0xCFF4, 0xCFF5],  # Range
                    "attack": [0xCFF6, 0xCFF7],  # Range
                    "defense": [0xCFF8, 0xCFF9],  # Range
                    "speed": [0xCFFA, 0xCFFB],  # Range
                    "pp_move1": 0xFFE,
                    "pp_move2": 0xFFF,
                    "pp_move3": 0xD000,
                    "pp_move4": 0xD001,
                    "catch_rate": 0xD007,
                    "base_experience": 0xD008,
                },
                "type_of_battle": 0xD057
            },
            "player": {
                "pokemon1": {
                    "pokemon_nr": 0xD16B,
                    "current_hp": [0xD16C, 0xD16D],
                    "status": 0xD16F,
                    "type1": 0xD170,
                    "type2": 0xD171,
                    "experience": [0xD179, 0xD17B],
                    "hp_ev": [0xD17C, 0xD17D],
                    "attack_ev": [0xD17E, 0xD17F],
                    "defense_ev": [0xD180, 0xD181],
                    "speed_ev": [0xD182, 0xD183],
                    "special_ev": [0xD184, 0xD185],
                    "attack_defense_iv": 0xD186,
                    "speed_special_iv": 0xD187,
                    "pp_move1": 0xD188,
                    "pp_move2": 0xD189,
                    "pp_move3": 0xD18A,
                    "pp_move4": 0xD18B,
                    "actual_level": 0xD18C,
                    "max_hp": [0xD18D, 0xD18E],
                    "attack": [0xD18F, 0xD190],
                    "defense": [0xD191, 0xD192],
                    "speed": [0xD193, 0xD194],
                    "special": [0xD195, 0xD196]
                },
                "pokemon2": {
                    "pokemon_nr": 0xD197,
                    "current_hp": [0xD198, 0xD199],
                    "status": 0xD19B,
                    "type1": 0xD19C,
                    "type2": 0xD19D,
                    "experience": [0xD1A5, 0xD1A7],
                    "hp_ev": [0xD1A8, 0xD1A9],
                    "attack_ev": [0xD1AA, 0xD1AB],
                    "defense_ev": [0xD1AC, 0xD1AD],
                    "speed_ev": [0xD1AE, 0xD1AF],
                    "special_ev": [0xD1B0, 0xD1B1],
                    "attack_defense_iv": 0xD1B2,
                    "speed_special_iv": 0xD1B3,
                    "pp_move1": 0xD1B4,
                    "pp_move2": 0xD1B5,
                    "pp_move3": 0xD1B6,
                    "pp_move4": 0xD1B7,
                    "actual_level": 0xD1B8,
                    "max_hp": [0xD1B9, 0xD1BA],
                    "attack": [0xD1BB, 0xD1BC],
                    "defense": [0xD1BD, 0xD1BE],
                    "speed": [0xD1BF, 0xD1C0],
                    "special": [0xD1C1, 0xD1C2]
                },
                "pokemon3": {
                    "pokemon_nr": 0xD1C3,
                    "current_hp": [0xD1C4, 0xD1C5],
                    "status": 0xD1C7,
                    "type1": 0xD1C8,
                    "type2": 0xD1C9,
                    "experience": [0xD1D1, 0xD1D3],
                    "hp_ev": [0xD1D4, 0xD1D5],
                    "attack_ev": [0xD1D6, 0xD1D7],
                    "defense_ev": [0xD1D8, 0xD1D9],
                    "speed_ev": [0xD1DA, 0xD1DB],
                    "special_ev": [0xD1DC, 0xD1DD],
                    "attack_defense_iv": 0xD1DE,
                    "speed_special_iv": 0xD1DF,
                    "pp_move1": 0xD1E0,
                    "pp_move2": 0xD1E1,
                    "pp_move3": 0xD1E2,
                    "pp_move4": 0xD1E3,
                    "actual_level": 0xD1E4,
                    "max_hp": [0xD1E5, 0xD1E6],
                    "attack": [0xD1E7, 0xD1E8],
                    "defense": [0xD1E9, 0xD1EA],
                    "speed": [0xD1EB, 0xD1EC],
                    "special": [0xD1ED, 0xD1EE]
                },
                "pokemon4": {
                    "pokemon_nr": 0xD1EF,
                    "current_hp": [0xD1F0, 0xD1F1],
                    "status": 0xD1F3,
                    "type1": 0xD1F4,
                    "type2": 0xD1F5,
                    "experience": [0xD1FD, 0xD1FF],
                    "hp_ev": [0xD200, 0xD201],
                    "attack_ev": [0xD202, 0xD203],
                    "defense_ev": [0xD204, 0xD205],
                    "speed_ev": [0xD206, 0xD207],
                    "special_ev": [0xD208, 0xD209],
                    "attack_defense_iv": 0xD20A,
                    "speed_special_iv": 0xD20B,
                    "pp_move1": 0xD20C,
                    "pp_move2": 0xD20D,
                    "pp_move3": 0xD20E,
                    "pp_move4": 0xD20F,
                    "actual_level": 0xD210,
                    "max_hp": [0xD211, 0xD212],
                    "attack": [0xD213, 0xD214],
                    "defense": [0xD215, 0xD216],
                    "speed": [0xD217, 0xD218],
                    "special": [0xD219, 0xD21A]
                },
                "pokemon5": {
                    "pokemon_nr": 0xD21B,
                    "current_hp": [0xD21C, 0xD21D],
                    "status": 0xD21F,
                    "type1": 0xD220,
                    "type2": 0xD221,
                    "experience": [0xD229, 0xD22B],
                    "hp_ev": [0xD22C, 0xD22D],
                    "attack_ev": [0xD22E, 0xD22F],
                    "defense_ev": [0xD230, 0xD231],
                    "speed_ev": [0xD232, 0xD233],
                    "special_ev": [0xD234, 0xD235],
                    "attack_defense_iv": 0xD236,
                    "speed_special_iv": 0xD237,
                    "pp_move1": 0xD238,
                    "pp_move2": 0xD239,
                    "pp_move3": 0xD23A,
                    "pp_move4": 0xD23B,
                    "actual_level": 0xD23C,
                    "max_hp": [0xD23D, 0xD23E],
                    "attack": [0xD23F, 0xD240],
                    "defense": [0xD241, 0xD242],
                    "speed": [0xD243, 0xD244],
                    "special": [0xD245, 0xD246]
                },
                "pokemon6": {
                    "pokemon_nr": 0xD247,
                    "current_hp": [0xD248, 0xD249],
                    "status": 0xD24B,
                    "type1": 0xD24C,
                    "type2": 0xD24D,
                    "experience": [0xD255, 0xD257],
                    "hp_ev": [0xD258, 0xD259],
                    "attack_ev": [0xD25A, 0xD25B],
                    "defense_ev": [0xD25C, 0xD25D],
                    "speed_ev": [0xD25E, 0xD25F],
                    "special_ev": [0xD260, 0xD261],
                    "attack_defense_iv": 0xD262,
                    "speed_special_iv": 0xD263,
                    "pp_move1": 0xD264,
                    "pp_move2": 0xD265,
                    "pp_move3": 0xD266,
                    "pp_move4": 0xD267,
                    "actual_level": 0xD268,
                    "max_hp": [0xD269, 0xD26A],
                    "attack": [0xD26B, 0xD26C],
                    "defense": [0xD26D, 0xD26E],
                    "speed": [0xD26F, 0xD270],
                    "special": [0xD271, 0xD272]
                }
            },
            "enemy": {
                "pokemon1": {
                    "pokemon_nr": 0xD8A4,
                    "current_hp": [0xD8A5, 0xD8A6],
                    "status": 0xD8A8,
                    "type1": 0xD8A9,
                    "type2": 0xD8AA,
                    "experience": [0xD8B2, 0xD8B4],
                    "hp_ev": [0xD8B5, 0xD8B6],
                    "attack_ev": [0xD8B7, 0xD8B8],
                    "defense_ev": [0xD8B9, 0xD8BA],
                    "speed_ev": [0xD8BB, 0xD8BC],
                    "special_ev": [0xD8BD, 0xD8BE],
                    "attack_defense_iv": 0xD8BF,
                    "speed_special_iv": 0xD8C0,
                    "pp_move1": 0xD8C1,
                    "pp_move2": 0xD8C2,
                    "pp_move3": 0xD8C3,
                    "pp_move4": 0xD8C4,
                    "actual_level": 0xD8C5,
                    "max_hp": [0xD8C6, 0xD8C7],
                    "attack": [0xD8C8, 0xD8C9],
                    "defense": [0xD8CA, 0xD8CB],
                    "speed": [0xD8CC, 0xD8CD],
                    "special": [0xD8CE, 0xD8CF]
                },
                "pokemon2": {
                    "pokemon_nr": 0xD8D0,
                    "current_hp": [0xD8D1, 0xD8D2],
                    "status": 0xD8D4,
                    "type1": 0xD8D5,
                    "type2": 0xD8D6,
                    "experience": [0xD8DE, 0xD8E0],
                    "hp_ev": [0xD8E1, 0xD8E2],
                    "attack_ev": [0xD8E3, 0xD8E4],
                    "defense_ev": [0xD8E5, 0xD8E6],
                    "speed_ev": [0xD8E7, 0xD8E8],
                    "special_ev": [0xD8E9, 0xD8EA],
                    "attack_defense_iv": 0xD8EB,
                    "speed_special_iv": 0xD8EC,
                    "pp_move1": 0xD8ED,
                    "pp_move2": 0xD8EE,
                    "pp_move3": 0xD8EF,
                    "pp_move4": 0xD8F0,
                    "actual_level": 0xD8F1,
                    "max_hp": [0xD8F2, 0xD8F3],
                    "attack": [0xD8F4, 0xD8F5],
                    "defense": [0xD8F6, 0xD8F7],
                    "speed": [0xD8F8, 0xD8F9],
                    "special": [0xD8FA, 0xD8FB]
                },
                "pokemon3": {
                    "pokemon_nr": 0xD8FC,
                    "current_hp": [0xD8FD, 0xD8FE],
                    "status": 0xD900,
                    "type1": 0xD901,
                    "type2": 0xD902,
                    "experience": [0xD90A, 0xD90C],
                    "hp_ev": [0xD90D, 0xD90E],
                    "attack_ev": [0xD90F, 0xD910],
                    "defense_ev": [0xD911, 0xD912],
                    "speed_ev": [0xD913, 0xD914],
                    "special_ev": [0xD915, 0xD916],
                    "attack_defense_iv": 0xD917,
                    "speed_special_iv": 0xD918,
                    "pp_move1": 0xD919,
                    "pp_move2": 0xD91A,
                    "pp_move3": 0xD91B,
                    "pp_move4": 0xD91C,
                    "actual_level": 0xD91D,
                    "max_hp": [0xD91E, 0xD91F],
                    "attack": [0xD920, 0xD921],
                    "defense": [0xD922, 0xD923],
                    "speed": [0xD924, 0xD925],
                    "special": [0xD926, 0xD927]
                },
                "pokemon4": {
                    "pokemon_nr": 0xD928,
                    "current_hp": [0xD929, 0xD92A],
                    "status": 0xD92C,
                    "type1": 0xD92D,
                    "type2": 0xD92E,
                    "experience": [0xD936, 0xD938],
                    "hp_ev": [0xD939, 0xD93A],
                    "attack_ev": [0xD93B, 0xD93C],
                    "defense_ev": [0xD93D, 0xD93E],
                    "speed_ev": [0xD93F, 0xD940],
                    "special_ev": [0xD941, 0xD942],
                    "attack_defense_iv": 0xD943,
                    "speed_special_iv": 0xD944,
                    "pp_move1": 0xD945,
                    "pp_move2": 0xD946,
                    "pp_move3": 0xD947,
                    "pp_move4": 0xD948,
                    "actual_level": 0xD949,
                    "max_hp": [0xD94A, 0xD94B],
                    "attack": [0xD94C, 0xD94D],
                    "defense": [0xD94E, 0xD94F],
                    "speed": [0xD950, 0xD951],
                    "special": [0xD952, 0xD953]
                },
                "pokemon5": {
                    "pokemon_nr": 0xD954,
                    "current_hp": [0xD955, 0xD956],
                    "status": 0xD958,
                    "type1": 0xD959,
                    "type2": 0xD95A,
                    "experience": [0xD962, 0xD964],
                    "hp_ev": [0xD965, 0xD966],
                    "attack_ev": [0xD967, 0xD968],
                    "defense_ev": [0xD969, 0xD96A],
                    "speed_ev": [0xD96B, 0xD96C],
                    "special_ev": [0xD96D, 0xD96E],
                    "attack_defense_iv": 0xD96F,
                    "speed_special_iv": 0xD970,
                    "pp_move1": 0xD971,
                    "pp_move2": 0xD972,
                    "pp_move3": 0xD973,
                    "pp_move4": 0xD974,
                    "actual_level": 0xD975,
                    "max_hp": [0xD976, 0xD977],
                    "attack": [0xD978, 0xD979],
                    "defense": [0xD97A, 0xD97B],
                    "speed": [0xD97C, 0xD97D],
                    "special": [0xD97E, 0xD97F]
                },
                "pokemon6": {
                    "pokemon_nr": 0xD980,
                    "current_hp": [0xD981, 0xD982],
                    "status": 0xD984,
                    "type1": 0xD985,
                    "type2": 0xD986,
                    "experience": [0xD98E, 0xD990],
                    "hp_ev": [0xD991, 0xD992],
                    "attack_ev": [0xD993, 0xD994],
                    "defense_ev": [0xD995, 0xD996],
                    "speed_ev": [0xD997, 0xD998],
                    "special_ev": [0xD999, 0xD99A],
                    "attack_defense_iv": 0xD99B,
                    "speed_special_iv": 0xD99C,
                    "pp_move1": 0xD99D,
                    "pp_move2": 0xD99E,
                    "pp_move3": 0xD99F,
                    "pp_move4": 0xD9A0,
                    "actual_level": 0xD9A1,
                    "max_hp": [0xD9A2, 0xD9A3],
                    "attack": [0xD9A4, 0xD9A5],
                    "defense": [0xD9A6, 0xD9A7],
                    "speed": [0xD9A8, 0xD9A9],
                    "special": [0xD9AA, 0xD9AB]
                }
            },
            "items": {
                "total_items": 0xD31D,
                "item_1": {
                    "item_id": 0xD31E,
                    "quantity": 0xD31F
                },
                "item_2": {
                    "item_id": 0xD320,
                    "quantity": 0xD321
                },
                "item_3": {
                    "item_id": 0xD322,
                    "quantity": 0xD323
                },
                "item_4": {
                    "item_id": 0xD324,
                    "quantity": 0xD325
                },
                "item_5": {
                    "item_id": 0xD326,
                    "quantity": 0xD327
                },
                "item_6": {
                    "item_id": 0xD328,
                    "quantity": 0xD329
                },
                "item_7": {
                    "item_id": 0xD32A,
                    "quantity": 0xD32B
                },
                "item_8": {
                    "item_id": 0xD32C,
                    "quantity": 0xD32D
                },
                "item_9": {
                    "item_id": 0xD32E,
                    "quantity": 0xD32F
                },
                "item_10": {
                    "item_id": 0xD330,
                    "quantity": 0xD331
                },
                "item_11": {
                    "item_id": 0xD332,
                    "quantity": 0xD333
                },
                "item_12": {
                    "item_id": 0xD334,
                    "quantity": 0xD335
                },
                "item_13": {
                    "item_id": 0xD336,
                    "quantity": 0xD337
                },
                "item_14": {
                    "item_id": 0xD338,
                    "quantity": 0xD339
                },
                "item_15": {
                    "item_id": 0xD33A,
                    "quantity": 0xD33B
                },
                "item_16": {
                    "item_id": 0xD33C,
                    "quantity": 0xD33D
                },
                "item_17": {
                    "item_id": 0xD33E,
                    "quantity": 0xD33F
                },
                "item_18": {
                    "item_id": 0xD340,
                    "quantity": 0xD341
                },
                "item_19": {
                    "item_id": 0xD342,
                    "quantity": 0xD343
                },
                "item_20": {
                    "item_id": 0xD344,
                    "quantity": 0xD345
                },
                "end_of_list": 0xD346
            }
        }
        self.flattened_features = self.flatten_features()
        self.feature_size = len(self.flatten_features())
        self.item_mappings = {
            # name: id
            "Poke Ball": 4,
            "Antidote": 11
        }
        self.type_mappings = {
            0: "Normal",
            2: "Flying",
        }

    def flatten_features(self):
        flat = {}
        for feature in self.features:
            for sub_feature in self.features[feature]:
                if isinstance(self.features[feature][sub_feature], int):
                    flat[feature + "_" + sub_feature] = self.features[feature][sub_feature]
                else:
                    for sub_sub_feature in self.features[feature][sub_feature]:
                        flat[feature + "_" + sub_feature + "_" + sub_sub_feature] = self.features[feature][sub_feature][
                            sub_sub_feature]
        return flat

    def get_features(self):
        return self.features

    def get_feature_values(self, env):
        feature_values = {}
        for feature, mem_address in self.flattened_features.items():
            if isinstance(mem_address, int):
                feature_values[feature] = env.read_m(mem_address)
            elif isinstance(mem_address, list):
                feature_values[feature] = 256 * env.read_m(mem_address[0]) + (
                    env.read_m(mem_address[1]))
            else:
                raise ValueError("mem_address is neither int nor list")
        return feature_values

    def get_feature_value(self, env, feature_name):
        # Filters flattened features for the feature name and returns the value of the feature
        for feature, mem_address in self.flattened_features.items():
            if feature == feature_name:
                if isinstance(mem_address, int):
                    feature_value = env.read_m(mem_address)
                elif isinstance(mem_address, list):
                    feature_value = 256 * env.read_m(mem_address[0]) + (
                        env.read_m(mem_address[1]))
                else:
                    raise ValueError("mem_address is neither int nor list")
        return feature_value

    def get_current_pokemon(self, env) -> int:
        for i in range(1, 7):
            if env.read_m(self.flattened_features["in_battle_player_pokemon_nr"]) == env.read_m(self.flattened_features[f"player_pokemon{i}_pokemon_nr"]):
                return i

    def get_number_of_pokeballs(self, env) -> int:
        for i in range(1, 21):
            if env.read_m(self.flattened_features[f"items_item_{i}_item_id"]) == self.item_mappings["Poke Ball"]:
                return env.read_m(self.flattened_features[f"items_item_{i}_quantity"])
        return 0


if __name__ == "__main__":
    state_mapper = StateMapper()
    print(state_mapper.flatten_features())
