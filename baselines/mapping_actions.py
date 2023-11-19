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



class action_mapper:
    def __init__(self):
        self.menu = 1
        self.fight_menu = 1
        self.pokemon_menu = 1
        self.bag_menu = 1

        self.actions = {
        0: ["m1", 4, "f1", 4],     # attack 1[1,4,1,4]
        1: ["m1", 4, "f2", 4],     # attack 2
        2: ["m1", 4, "f3", 4],     # attack 3
        3: ["m1", 4, "f4", 4],     # attack 4
        4: ["m2", 4, "p1", 4, 4],  # pokemon 1
        5: ["m2", 4, "p2", 4, 4],  # pokemon 2
        6: ["m2", 4, "p3", 4, 4],  # pokemon 3
        7: ["m2", 4, "p4", 4, 4],  # pokemon 4
        8: ["m2", 4, "p5", 4, 4],  # pokemon 5
        9: ["m2", 4, "p6", 4, 4], # pokemon 6
        10: ["m4", 4],       # run
        11: ["m3", 4, 4]       # pokeball
        # 13: ["m3", 4, "b2"]      # healing
        }

    def get_action_sequence(self, action):
        list = self.actions(action)
        # transforms action string
        new_list = []
        for l in list:
            if isinstance(l, str):
                actions = self.go_to(l)
                for a in actions:
                    new_list.append(a)
            else:
                new_list.append(l)



    def go_to(self,space):
        list = []
        want = int(space[1])
        letter = space[0]
        # in first menu
        if letter == "m":
            if self.menu == want:
                return list
            if want % 2 == 0 and self.menu % 2 == 1:
                #right
                self.append(2)
                self.menu += 1
            if want % 2 == 1 and self.menu % 2 == 0:
                #left
                self.append(1)
                self.menu -= 1
            if want < 3 and self.menu > 2:
                # up
                self.append(3)
                self.menu += 2
            if want > 2 and self.menu < 3:
                # down
                self.append(0)
                self.menu -= 1
            return list

        if letter == "f":
            if self.fight_menu == want:
                return list
            while want > self.fight_menu :
                #up
                self.append(3)
                self.fight_menu += 1
            while want < self.fight_menu :
                #down
                self.append(0)
                self.fight_menu -= 1
            return list

        if letter == "p":
            if self.pokemon_menu == want:
                return list
            while want > self.pokemon_menu :
                #up
                self.append(3)
                self.pokemon_menu += 1
            while want < self.pokemon_menu :
                #down
                self.append(0)
                self.pokemon_menu -= 1
            return list





