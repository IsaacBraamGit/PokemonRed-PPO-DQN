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

version_nr = 1.0
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
        self.memory = deque(maxlen=10000)
        self.gamma = 0.7  # discount rate
        self.epsilon = 1  # exploration rate
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
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):

        self.memory.append((state, action, reward, next_state, done))

        line = str((self.e,state, action, reward, next_state, done))
        append_to_file(self.file_path, line)

    def act(self, state, test=False):
        if np.random.rand() <= self.epsilon:
            action = random.randrange(self.action_size)
        else:
            act_values = self.model.predict(state, verbose=0)
            action = np.argmax(act_values[0])
        print(state)

        if test:
            user_input = input("Please enter a number: ")
            action = int(user_input)

        print(action)
        if not self.get_action_validity(action):
            print("not valid")
            action = 12  # pass if not valid

        print("action:", action)
        action_list = self.action_mapper.get_action_sequence(action)
        print("action_list", action_list)

        return action, action_list

    def get_action_validity(self, action: int) -> bool:
        if 0 <= action <= 3:
            # Only actions with PP > 0 are valid
            return self.state_mapper.get_feature_value(self.env, f"in_battle_player_pp_move{action + 1}") > 0
        if 4 <= action <= 9:
            current_pokemon = self.state_mapper.get_current_pokemon(self.env)
            is_switching = action - 3 != current_pokemon
            if not is_switching:
                return False
            # If switching, check if the target Pokémon exists
            target_pokemon_nr = self.state_mapper.get_feature_value(self.env, f"player_pokemon{action - 3}_pokemon_nr")
            return target_pokemon_nr > 0
        if action == 10:
            # Only valid if battle type is not wild
            return self.state_mapper.get_feature_value(self.env, "in_battle_type_of_battle") != 1
        if action == 11:
            # Only valid if more than 0 pokeballs are available
            return self.state_mapper.get_number_of_pokeballs(self.env) > 0

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
        print("LEARNED")

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
        feature_values = self.state_mapper.get_feature_values(self.env)
        wanted_feature_types = ["in_battle",
                                # "player",
                                "enemy_pokemon1",
                                "items_item_1_quantity"]
        state = [v for k, v in feature_values.items() if any([k.startswith(t) for t in wanted_feature_types])]

        # todo: decompose things like move into damage, hit perc, additional effect, to have more generalisation, also for instance poke id
        # todo: feature engineering with hp, type, status, etc

        y_position = self.env.read_m(0xCC24)
        x_position = self.env.read_m(0xCC25)
        selected_menu_item = self.env.read_m(0xCC26)

        # mapping
        # todo: item menu, pokemon menu
        in_text = False
        in_menu = True
        if y_position == 2 and x_position == 11 and selected_menu_item == 2:
            in_text = True
            in_menu = False
        slot = 0

        if x_position == 5:
            in_menu = False
            slot = selected_menu_item

        if x_position == 9:
            if selected_menu_item == 0:
                slot = 1
            if selected_menu_item == 1:
                slot = 3

        if x_position == 15:
            if selected_menu_item == 0:
                slot = 2
            if selected_menu_item == 1:
                slot = 4

        if slot > 2:
            slotbit1 = 1
        else:
            slotbit1 = 0
        if slot % 2 == 0:
            slotbit2 = 1
        else:
            slotbit2 = 0

        # Todo:player_pokemon_internal id to one hot, and enemy
        # Todo: add nr of actions in this battle(like first move should probably be a to open fight menu)
        # Todo: state normalization

        state.extend([
            in_menu, in_text, slotbit1, slotbit2
        ])

        return np.reshape(state, [1, len(state)])

    def get_reward(self, next_state, state):
        # todo: how do we measure stat drops, so it is represented in the state, so we can learn it?
        # health of opponent
        score = state[0][9] - next_state[0][9]

        # punishment for doing somehing that does nothing
        if (state == next_state).all():
            score -= 0.1

        # running away is for cowards
        if state[0][12] and state[0][13]:
            score -= 2

        # todo: don't use a powerfull move when you don't have to, how do we make it worthwhile to switch?
        print("score:", flush=True)
        print(score, flush=True)
        score = score * 100
        return score

    def learn(self, action, terminated, truncated, state, next_state):
        done = False
        if terminated or truncated:
            done = True

        reward = self.get_reward(next_state, state)
        # Store the experience in memory
        self.remember(state, action, reward, next_state, done)

        # state = next_state
        if done:
            self.save(f"models/dqn_model_v{version_nr}_{self.e}.h5")
            print(f"Episode: {self.e} ")

        if len(self.memory) > self.batch_size and self.e % 3 == 0:
            # self.replay(self.batch_size)
            self.executor.submit(self.replay, self.batch_size)
        if self.e % 2000 == 0 and self.e != 0:
            self.save(f"models/dqn_model_v{version_nr}_{self.e}.h5")
        self.e += 1
        # todo: reset env after a while, long enough?
        if self.e % 10_000 == 0:
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
