from os.path import exists
from pathlib import Path
import uuid
from red_gym_env import RedGymEnv
from stable_baselines3 import A2C, PPO
import _our_model
from stable_baselines3.common import env_checker
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.callbacks import CheckpointCallback
from util import perform_actions_in_env
import time
OUR_SMALL_AGENT = True
pokemon_caught = 1

def make_env(env_conf, seed=0):
    def _init():
        return RedGymEnv(env_conf)
    set_random_seed(seed)
    return _init


if __name__ == '__main__':
    sess_path = Path(f'isaac_session')
    ep_length = 2**230000

    env_config = {
                'headless': False, 'save_final_state': False, 'early_stop': False,
                'action_freq': 24, 'init_state': '../has_pokedex_nballs.state', 'max_steps': ep_length,
                'print_rewards': False, 'save_video': False, 'fast_video': False, 'session_path': sess_path,
                'gb_path': '../PokemonRed.gb', 'debug': False, 'sim_frame_dist': 2_000_000.0, 'extra_buttons': True
            }

    num_cpu = 1  # 64 #46 # Also sets the number of episodes per training iteration
    env = make_env(env_config)()  # SubprocVecEnv([make_env(i, env_config) for i in range(num_cpu)])
    small_agent = _our_model.DQNAgent(env)
    file_name = 'session_4da05e87_main_good/poke_439746560_steps.zip'
    
    print('\nloading checkpoint')
    model = PPO.load(file_name, env=env, custom_objects={'lr_schedule': 0, 'clip_range': 0})

    obs, info = env.reset()
    step = 0
    previous_battle_status = 0

    while True:
        action = 7  # pass action
        try:
            with open("agent_enabled.txt", "r") as f:
                agent_enabled = f.readlines()[0].startswith("yes")
        except:
            agent_enabled = False
        if agent_enabled:
            battle_status = env.read_m(0xD057)
            state = small_agent.get_state()
            if battle_status != 0 and OUR_SMALL_AGENT:
                if previous_battle_status == 0:
                    env.wait(360)
                    env.step(4)
                    env.wait(360)
                action, action_list = small_agent.act(state, False)
                _, rewards, terminated, truncated, _, pokemon_caught = perform_actions_in_env(action,action_list, env, small_agent, pokemon_caught)
                # TODO think about how to handle rewards to compare to the big model
                next_state = small_agent.get_state()
                small_agent.learn(action, terminated, truncated, state, next_state)
                state = next_state
                small_agent.update_target_model()
            else:
                action_big_model, _states = model.predict(obs)
                obs, rewards, terminated, truncated, info = env.step(action_big_model)
                env.render()

            if step % 30_000 == 0 and step != 0:
                env.reset()
            if truncated:
                break

            step += 1
            if previous_battle_status == 1 and battle_status == 0:
                small_agent.action_mapper.reset()
            # if switch
            if 3 < action < 10:
                small_agent.action_mapper.reset_on_switch()
            previous_battle_status = battle_status
        else:
            obs, rewards, terminated, truncated, info = env.step(action)
        env.render()
    env.close()
