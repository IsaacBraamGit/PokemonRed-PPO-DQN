import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import random
from concurrent.futures import ThreadPoolExecutor
import os
import re
import mappings

#version_nr = "test"
version_nr = 4.1
load_model = True


def append_to_file(file_path, line):
    with open(file_path, "a") as file:
        file.write(line + "\n")


class DQNAgent:
    def __init__(self, env):
        self.executor = ThreadPoolExecutor(max_workers=5)

        self.action_mapper = mappings.ActionMapper()
        self.state_mapper = mappings.StateMapper()
        self.action_size = self.action_mapper.action_size
        self.memory_total = []
        self.memory = deque(maxlen=10_000)
        self.gamma = 0.7  # discount rate
        self.epsilon = 1.0 # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.9995
        self.learning_rate = 1
        self.batch_size = 64

        self.env = env
        self.e = 0
        self.state_size = len(self.get_state()[0])

        self.model = self.load()
        self.target_model = self._build_target_model()
        self.file_path = f"models/log_dqn_model_v{version_nr}.txt"  # Path to your log file

        # todo: set reward weights
        self.enemy_health_weight = 1
        self.enemy_total_health_weight = 1
        self.player_health_weight = 1
        self.player_total_health_weight = 1
        self.enemy_status_weight = 1
        self.player_status_weight = 1
        self.enemy_party_size_weight = 10
        self.player_party_size_weight = 10
        self.enemy_total_level_weight = 1
        self.player_total_level_weight = 10
        #self.enemy_total_experience_weight = 1
        self.player_total_experience_weight = 0.1
        self.total_items_weight = 1

        self.wanted_action = 7
        self.not_val_nr = 0
        self.run = 0
    def get_latest_version(self):
        max_e = -1
        latest_model_path = None

        # Iterate over files in the model directory
        for filename in os.listdir("models"):
            model_pattern = re.compile(rf"dqn_model_v{version_nr}_(\d+)\.h5")
            match = model_pattern.match(filename)
            if match:
                e = int(match.group(1))
                if e > max_e:
                    max_e = e
                    latest_model_path = os.path.join("models", filename)
        print("loading: ", latest_model_path)
        return latest_model_path

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def _build_target_model(self):
        model = self._build_model()
        return model

    def update_target_model(self):
        if self.e % 400 == 0:
            self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):

        self.memory.append((state, action, reward, next_state, done))

        line = str((self.e, state, action, reward, next_state, done,self.epsilon))
        append_to_file(self.file_path, line)

    def act(self, state, test=False):
        if np.random.rand() <= self.epsilon:
            action = random.randrange(self.action_size)
            while not self.get_action_validity(action):
                action = random.randrange(self.action_size)

        else:
            act_values = self.model.predict(state, verbose=0)
            sorted_actions = np.argsort(-act_values[0])

            for potential_action in sorted_actions:
                if self.get_action_validity(potential_action):
                    action = potential_action

                    break
            else:
                raise Exception ("no valid action")
                action = 12  # default action if none are valid

        print(state)

        if test:
            user_input = input("Please enter a number: ")
            action = int(user_input)
            while not self.get_action_validity(action):
                print('There is a time and place for everything, but cant do that now')
                user_input = input("Please enter a number: ")
                action = int(user_input)

        if self.e < 2:
            action = 11





        print("action:", action)
        action_list = self.action_mapper.get_action_sequence(action, state, self.env)

        if action_list == [7]:
            self.not_val_nr += 1
        else:
            self.not_val_nr = 0
        #todo: correct stuck exception
        if self.not_val_nr > 100:
            print("STUCK")
            self.e = 0
            self.env.reset()
            return 12, [7]
        print("action_list", action_list)
        self.wanted_action = action
        return action, action_list

    def get_action_validity(self, action: int) -> bool:
        if 0 <= action <= 3:
            # Only actions with PP > 0 are valid
            return self.state_mapper.get_feature_value(self.env, f"in_battle_player_pp_move{action + 1}") > 0
        if 4 <= action <= 9:
            current_pokemon = self.state_mapper.get_current_pokemon(self.env, self.action_mapper)
            is_switching = action - 3 != current_pokemon
            if not is_switching:
                return False
            # If switching, check if the target Pokémon has more than 0 HP
            target_pokemon_hp = self.state_mapper.get_feature_value(self.env, f"player_pokemon{action - 3}_current_hp")
            return target_pokemon_hp > 0
        if action == 10:
            # Only valid if battle type is not wild
            return self.state_mapper.get_feature_value(self.env, "in_battle_type_of_battle") == 1
        if action == 11:
            # Only valid if more than 0 pokeballs are available
            return self.state_mapper.get_number_of_pokeballs(self.env) > 0 and self.state_mapper.get_feature_value(
                self.env, 'in_battle_type_of_battle') == 1

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        # Extract states and next_states from minibatch
        states = np.array([t[0][0] for t in minibatch])
        next_states = np.array([t[3][0] for t in minibatch])

        # Vectorized prediction for the current states using the main network
        q_values = self.model.predict(states)

        # Double DQN Part: Here we use the target model for the next states
        q_values_next = self.target_model.predict(next_states)
        q_values_next_online = self.model.predict(
            next_states)  # Get the Q-values from the online model for action selection

        # Preparing training data
        x_train = []
        y_train = []

        for i, (state, action, reward, next_state, done) in enumerate(minibatch):
            # Double DQN Update: Choose the best action from the online model's Q-values
            best_action = np.argmax(q_values_next_online[i])

            # Use the chosen action to get the Q-value from the target model for the evaluation
            target = reward if done else reward + self.gamma * q_values_next[i][best_action]

            # Update the q_values for the action taken
            q_values_current = q_values[i]
            q_values_current[action] = target

            x_train.append(state)
            y_train.append(q_values_current)

        # Ensure x_train is correctly reshaped for training
        x_train = np.reshape(x_train, (batch_size, -1))

        # Train the model in one batch
        self.model.fit(x_train, np.array(y_train), batch_size=batch_size, verbose=0)

        # Update the exploration rate
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
            print("EPSILON", self.epsilon)

    def load(self):
        model = self._build_model()
        # todo, save and load model vars, like e and epsilon
        if load_model:
            name = self.get_latest_version()
            if name is not None:
                model.load_weights(name)

        return model

    def save(self, name):
        self.model.save_weights(name)

    def get_state(self):
        # todo: item menu, pokemon menu
        # Todo: state normalization

        feature_values = self.state_mapper.get_feature_values(self.env)

        # Player Pokemon in battle
        player_current_hp = feature_values["in_battle_player_current_hp"]
        player_max_hp = feature_values["in_battle_player_max_hp"]
        player_status = self.state_mapper.get_player_status(self.env)
        pp_move1 = feature_values["in_battle_player_pp_move1"]
        pp_move2 = feature_values["in_battle_player_pp_move2"]
        pp_move3 = feature_values["in_battle_player_pp_move3"]
        pp_move4 = feature_values["in_battle_player_pp_move4"]
        player_attack = feature_values["in_battle_player_attack"]
        player_defense = feature_values["in_battle_player_defense"]
        player_speed = feature_values["in_battle_player_speed"]
        player_special = feature_values["in_battle_player_special"]
        player_type1 = feature_values["in_battle_player_type1"]
        player_type2 = feature_values["in_battle_player_type2"]

        state = [
            player_current_hp, player_max_hp, *player_status, pp_move1, pp_move2, pp_move3, pp_move4, player_attack,
            player_defense, player_speed, player_special
        ]

        # Enemy in battle
        enemy_current_hp = feature_values["in_battle_enemy_current_hp"]
        enemy_max_hp = feature_values["in_battle_enemy_max_hp"]
        enemy_status = self.state_mapper.get_enemy_status(self.env)
        enemy_attack = feature_values["in_battle_enemy_attack"]
        enemy_defense = feature_values["in_battle_enemy_defense"]
        enemy_speed = feature_values["in_battle_enemy_speed"]
        enemy_special = feature_values["in_battle_enemy_special"]
        enemy_type1 = feature_values["in_battle_enemy_type1"]
        enemy_type2 = feature_values["in_battle_enemy_type2"]

        state.extend([
            enemy_current_hp, enemy_max_hp, *enemy_status, enemy_attack, enemy_defense, enemy_speed, enemy_special
        ])

        # Player Pokemon out of battle
        for i in range(1, 7):
            pokemon_hp = feature_values[f"player_pokemon{i}_current_hp"]
            pokemon_max_hp = feature_values[f"player_pokemon{i}_max_hp"]
            pokemon_level = feature_values[f"player_pokemon{i}_actual_level"]
            pokemon_experience = feature_values[f"player_pokemon{i}_experience"]
            pokemon_type1 = feature_values[f"player_pokemon{i}_type1"]
            pokemon_type2 = feature_values[f"player_pokemon{i}_type2"]
            pokemon_effectiveness = self.state_mapper.get_pokemon_effectiveness(pokemon_type1, pokemon_type2,
                                                                                enemy_type1, enemy_type2)

            state.extend([
                pokemon_hp, pokemon_max_hp, pokemon_level, pokemon_experience, pokemon_effectiveness
            ])

        state.append(self.state_mapper.get_number_of_pokemon(self.env, enemy=False))

        # Enemy Pokemon out of battle
        for i in range(1, 7):
            pokemon_hp = feature_values[f"enemy_pokemon{i}_current_hp"]
            pokemon_max_hp = feature_values[f"enemy_pokemon{i}_max_hp"]
            pokemon_level = feature_values[f"enemy_pokemon{i}_actual_level"]
            pokemon_experience = feature_values[f"enemy_pokemon{i}_experience"]
            pokemon_type1 = feature_values[f"enemy_pokemon{i}_type1"]
            pokemon_type2 = feature_values[f"enemy_pokemon{i}_type2"]
            pokemon_effectiveness = self.state_mapper.get_pokemon_effectiveness(pokemon_type1, pokemon_type2,
                                                                                player_type1, player_type2)

            state.extend([
                pokemon_hp, pokemon_max_hp, pokemon_level, pokemon_experience, pokemon_effectiveness
            ])

        state.append(self.state_mapper.get_number_of_pokemon(self.env, enemy=True))

        # Player current moves
        for i in range(1, 5):
            move_details = self.state_mapper.get_move_details(feature_values[f"in_battle_player_move{i}"])
            if move_details is None:
                state.extend([0, 0, 0])
                continue
            move_power = move_details["Power"]
            move_accuracy = move_details["Accuracy"]
            move_type = move_details[f"Type"]
            move_effectiveness = self.state_mapper.get_move_effectiveness(move_type, enemy_type1, enemy_type2)
            state.extend([
                move_power, move_accuracy, move_effectiveness
            ])

        state.append(int(feature_values["in_battle_type_of_battle"] > 1))  # 0 = wild, 1 = trainer / gym leader, etc

        # Add number of pokeballs
        state.append(self.state_mapper.get_number_of_pokeballs(self.env))

        # Add number of items
        state.append(self.state_mapper.get_number_of_items(self.env))

        # Add positioning in menus
        state.extend(self.state_mapper.get_positional_data(self.env))

        return np.reshape(state, [1, len(state)])

    def get_reward(self, state, next_state):
        # Enemy
        enemy_health = min(next_state[0][17] - state[0][17],0)
        enemy_total_health = sum(next_state[0][i + 61] for i in range(0, 7, 5)) - sum(
            state[0][i + 61] for i in range(0, 7, 5))
        enemy_status = sum(next_state[0][i + 19] for i in range(7)) - sum(state[0][i + 19] for i in range(7))
        enemy_party_size = next_state[0][91] - state[0][91]
        enemy_total_level = sum(next_state[0][i + 63] for i in range(0, 7, 5)) - sum(
            state[0][i + 63] for i in range(0, 7, 5))
        enemy_total_experience = sum(next_state[0][i + 64] for i in range(0, 7, 5)) - sum(
            state[0][i + 64] for i in range(0, 7, 5))

        # Player
        player_health = min(next_state[0][0] - state[0][0],0)
        player_total_health = sum(next_state[0][i + 30] for i in range(0, 7, 5)) - sum(
            state[0][i + 30] for i in range(0, 7, 5))
        player_status = sum(next_state[0][i + 2] for i in range(7)) - sum(state[0][i + 2] for i in range(7))
        player_party_size = next_state[0][60] - state[0][60]
        player_total_level = sum(next_state[0][i + 32] for i in range(0, 7, 5)) - sum(
            state[0][i + 32] for i in range(0, 7, 5))
        player_total_experience = sum(next_state[0][i + 33] for i in range(0, 7, 5)) - sum(
            state[0][i + 33] for i in range(0, 7, 5))

        total_items = next_state[0][106] - state[0][106]

        if player_total_level != 0:
            player_total_experience = 0

        score = (
                - self.enemy_health_weight * enemy_health
                - self.enemy_total_health_weight * enemy_total_health #todo: werkt deze altijd goed?
                + self.enemy_status_weight * enemy_status #todo: add ev/iv lowerings
                - self.enemy_party_size_weight * enemy_party_size #todo: werkt niet
                - self.enemy_total_level_weight * enemy_total_level
                #- self.enemy_total_experience_weight * enemy_total_experience
                + self.player_health_weight * player_health
                #+ self.player_total_health_weight * player_total_health #todo: positive if you black out
                - self.player_status_weight * player_status
                + self.player_party_size_weight * player_party_size

                + self.player_total_level_weight * player_total_level#todo: add measurement of how good pokemon is (base_stats? rank?)
                + self.player_total_experience_weight * player_total_experience
                + self.total_items_weight * total_items
                #todo: blacking out gives no loss

        )
        if score != 0:
            print(score)

        print("score:", flush=True)
        print(score, flush=True)
        score = score * 100
        return score

    def learn(self, action, terminated, truncated, state, next_state):
        done = False
        if terminated or truncated:
            done = True

        reward = self.get_reward(state, next_state)
        # Store the experience in memory
        self.remember(state, self.wanted_action, reward, next_state, done)

        # state = next_state
        if done:
            self.save(f"models/dqn_model_v{version_nr}_{self.e}.h5")

        if len(self.memory) > self.batch_size and self.e % 3 == 0:
            # self.replay(self.batch_size)
            self.executor.submit(self.replay, self.batch_size)
        if self.run % 500 == 0 and self.run != 0:
            self.save(f"models/dqn_model_v{version_nr}_{self.e}.h5")
        self.e += 1
        self.run += 1
        # todo: reset env after a while, long enough?
        if self.e % 500 == 0:
            self.e = 0
            self.env.reset()
        print("e=", self.e, flush=True)

    """
def chose_action(env):
    battle_status = env.read_m(0xD057)

    # our first pokemon
    player_pokemon_internal_id = env.read_m(0xCFC0)  # Player's Pokémon internal ID

    our_lvl = env.read_m(0xD18C)
    our_hp = env.read_m(0xD16D)

    move1 = env.read_m(0xD173)  # Move 1
    move2 = env.read_m(0xD174)  # Move 2
    move3 = env.read_m(0xD175)  # Move 3
    move4 = env.read_m(0xD176)  # Move 4

    type1 = env.read_m(0xD170)  # Type 1
    type2 = env.read_m(0xD171)  # Type 2

    experience = env.read_m(0xD17B)  # Experience

    pp_move1 = env.read_m(0xD188)  # PP Move 1
    pp_move2 = env.read_m(0xD189)  # PP Move 2
    pp_move3 = env.read_m(0xD18A)  # PP Move 3
    pp_move4 = env.read_m(0xD18B)  # PP Move 4


    max_hp = env.read_m(0xD18E)  # Max HP high byte

    # openents pokemon:

    enemy_pokemon_internal_id = env.read_m(0xCFD8)  # Enemy's Pokémon internal ID

    enemy_lvl = env.read_m(0xCFF3)  # Enemy Level
    enemy_hp = env.read_m(0xCFE7)  # Enemy's HP
    enemy_name = env.read_m(0xCFE4)  # Enemy's Name

    enemy_type1 = env.read_m(0xCFEA)  # Enemy's Type 1
    enemy_type2 = env.read_m(0xCFEB)  # Enemy's Type 2

    enemy_catch_rate = env.read_m(0xD007)  # Enemy's Catch Rate

    # This is the same address as before, so I'm not sure if you wanted to duplicate it.
    # If it is the enemy's experience it should be a different address.
    enemy_experience = env.read_m(0xD17B)  # Experience (Same as previous, possibly a mistake?)

    enemy_max_hp = env.read_m(0xCFF5)  # Enemy's Max HP

    party_count = env.read_m(0xD163)




    return 4
"""
