import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import random
from concurrent.futures import ThreadPoolExecutor
import os
import re
version_nr = 1
load_model = True
class DQNAgent:
    def __init__(self, action_size, env):
        self.executor = ThreadPoolExecutor(max_workers=5)

        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 0.0001  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.9999
        self.learning_rate = 0.1
        self.batch_size = 64

        self.env = env
        self.state = self.get_state()
        self.e = 0
        self.state_size = len(self.state[0])

        self.model = self.load()

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

    def remember(self, state, action, reward, next_state, done):
        print((state, action, reward, next_state, done))
        if reward> 0:
            print("FFF")
        self.memory.append((state, action, reward, next_state, done))

    def act(self):
        print("")
        print("act")
        self.state = self.get_state()

        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(self.state,verbose=0)
        print("action=",np.argmax(act_values[0]))
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        # Extract states and next_states from minibatch
        states = np.array([t[0][0] for t in minibatch])
        next_states = np.array([t[3][0] for t in minibatch])

        # Vectorized prediction for the current and next states
        q_values = self.model.predict(states)
        q_values_next = self.model.predict(next_states)

        # Preparing training data
        x_train = []
        y_train = []

        for i, (state, action, reward, next_state, done) in enumerate(minibatch):
            # Update the target for the action based on whether the episode is done
            target = reward if done else reward + self.gamma * np.amax(q_values_next[i])

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
            print("EPSILON",self.epsilon)
        print("LEARNED")

    def load(self):
        model = self._build_model()
        # todo, save and load model vars, like e and epsilon
        if load_model:
            name = self.get_latest_version()
            if name != None:
                model.load_weights(name)

        return model

    def save(self, name):
        self.model.save_weights(name)

    def get_state(self):
        # Read all the memory addresses to create the state vector
        # todo: all in one call for speed, but save mapping somewhere

        # todo: decompose things like move into damage, hit perc, additional effect, to have more generalisation, also for instance poke id
        battle_status = self.env.read_m(0xD057)
        player_pokemon_internal_id = self.env.read_m(0xCFC0)
        our_lvl = self.env.read_m(0xD18C)
        our_hp = self.env.read_m(0xD16D)
        move1 = self.env.read_m(0xD173)
        move2 = self.env.read_m(0xD174)
        move3 = self.env.read_m(0xD175)
        move4 = self.env.read_m(0xD176)
        type1 = self.env.read_m(0xD170)
        type2 = self.env.read_m(0xD171)
        experience = self.env.read_m(0xD17B)
        pp_move1 = self.env.read_m(0xD188)
        pp_move2 = self.env.read_m(0xD189)
        pp_move3 = self.env.read_m(0xD18A)
        pp_move4 = self.env.read_m(0xD18B)
        max_hp = self.env.read_m(0xD18E)
        enemy_pokemon_internal_id = self.env.read_m(0xCFD8)
        enemy_lvl = self.env.read_m(0xCFF3)
        enemy_hp = self.env.read_m(0xCFE7)
        enemy_max_hp = self.env.read_m(0xCFF5)  # Enemy's Max HP

        party_count = self.env.read_m(0xD163)
        #D007 - The enemy Pokémon's catch rate. This ranges from 0 to 255 ($00-$FF) and the higher it is the easier it is to catch the target Pokémon.

        y_position = self.env.read_m(0xCC24)
        x_position = self.env.read_m(0xCC25)
        selected_menu_item = self.env.read_m(0xCC26)
        tile_hidden_by_cursor = self.env.read_m(0xCC27)
        last_menu_item_id = self.env.read_m(0xCC28)
        bitmask_key_port_current_menu = self.env.read_m(0xCC29)
        previously_selected_menu_item = self.env.read_m(0xCC2A)
        last_cursor_position_party_pc = self.env.read_m(0xCC2B)
        last_cursor_position_item_screen = self.env.read_m(0xCC2C)
        last_cursor_position_start_battle_menu = self.env.read_m(0xCC2D)
        current_pokemon_index_party = self.env.read_m(0xCC2F)
        pointer_cursor_tile_buffer = self.env.read_m(0xCC30) + (
                    self.env.read_m(0xCC31) << 8)  # Combining two bytes into a pointer
        first_displayed_menu_item_id = self.env.read_m(0xCC36)
        item_highlighted_with_select = self.env.read_m(0xCC35)

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
        """
        print(in_text,in_menu,slot,"y_position",y_position,
            "x_position", x_position,
            "selected_menu_item", selected_menu_item,
            "tile_hidden_by_cursor", tile_hidden_by_cursor,
            "last_menu_item_id", last_menu_item_id,
            "bitmask_key_port_current_menu", bitmask_key_port_current_menu,
            "previously_selected_menu_item", previously_selected_menu_item,
            "last_cursor_position_party_pc", last_cursor_position_party_pc,
            "last_cursor_position_item_screen", last_cursor_position_item_screen,
            "last_cursor_position_start_battle_menu", last_cursor_position_start_battle_menu,
            "current_pokemon_index_party", current_pokemon_index_party,
            "pointer_cursor_tile_buffer", pointer_cursor_tile_buffer,
            "first_displayed_menu_item_id", first_displayed_menu_item_id,
            "item_highlighted_with_select", item_highlighted_with_select
        )
        """
        # ...and so on for all other variables you want to track

        # Combine all variables into a single state array
        #Todo:player_pokemon_internal id to one hot, and enemy

        # Todo: add nr of actions in this battle(like first move should probably be a to open fight menu)
        state = np.array([
            battle_status, player_pokemon_internal_id, our_lvl, our_hp, move1,
            move2, move3, move4, type1, type2,
            experience, pp_move1, pp_move2, pp_move3, pp_move4,
            max_hp, enemy_pokemon_internal_id, enemy_lvl, enemy_hp, enemy_max_hp,
            in_menu,in_text,slotbit1,slotbit2
        ])

        # Normalize or preprocess the state array as necessary
        # For example, state = state / np.max(state) if you want to normalize

        return np.reshape(state, [1, len(state)])

    def get_reward(self, next_state, state):
        #health of opponent
        score = state[0][18] - next_state[0][18]

        #punishment for doing somehing that does nothing
        if (state == next_state).all():
           score -= 0.1

        # running away is for cowards
        if state[0][22] and state[0][23]:
            score -=2

        # todo: don't use a powerfull move when you don't have to, how do we make it worthwhile to switch?
        print("score:",flush=True)
        print(score,flush=True)
        return score

    def async_learn(self, action, terminated, truncated, state, next_state):
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
            #self.replay(self.batch_size)
            self.executor.submit(self.replay,self.batch_size)
        if self.e % 2000 == 0 and self.e != 0:
            self.save(f"models/dqn_model_v{version_nr}_{self.e}.h5")
        self.e += 1
        #todo: reset env after a while, long enough?
        if self.e % 10_000 == 0:
           self.env.reset()
        print("e=",self.e, flush=True)

    def learn(self, action, terminated,truncated,next_state):
        state = self.state
        #self.executor.submit(self.async_learn, action, terminated, truncated, state, next_state)

        self.async_learn( action, terminated, truncated, state, next_state)

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