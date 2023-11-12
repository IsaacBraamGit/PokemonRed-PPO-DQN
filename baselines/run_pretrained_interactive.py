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
import time
OUR_SMALL_AGENT = True

def make_env(rank, env_conf, seed=0):
    """
    Utility function for multiprocessed env.
    :param env_id: (str) the environment ID
    :param num_env: (int) the number of environments you wish to have in subprocesses
    :param seed: (int) the initial seed for RNG
    :param rank: (int) index of the subprocess
    """
    def _init():
        env = RedGymEnv(env_conf)
        #env.seed(seed + rank)
        return env
    set_random_seed(seed)
    return _init

if __name__ == '__main__':
    sess_path = Path(f'isaac_session')
    #sess_path = Path(f'isaac_session_{str(uuid.uuid4())[:8]}')
    ep_length = 2**23

    env_config = {
                'headless': False, 'save_final_state': False, 'early_stop': False,
                'action_freq': 24, 'init_state': '../has_pokedex_nballs.state', 'max_steps': ep_length,
                'print_rewards': False, 'save_video': False, 'fast_video': False, 'session_path': sess_path,
                'gb_path': '../PokemonRed.gb', 'debug': False, 'sim_frame_dist': 2_000_000.0, 'extra_buttons': True
            }
    
    num_cpu = 1 #64 #46 # Also sets the number of episodes per training iteration
    env = make_env(0, env_config)() #SubprocVecEnv([make_env(i, env_config) for i in range(num_cpu)])
    small_agent = _our_model.DQNAgent(6, env)
    #env_checker.check_env(env)
    file_name = 'session_4da05e87_main_good/poke_439746560_steps.zip'
        #'session_Isaac_32e86aec/poke_688128_steps.zip'
    
    print('\nloading checkpoint')
    model = PPO.load(file_name, env=env, custom_objects={'lr_schedule': 0, 'clip_range': 0})
        
    #keyboard.on_press_key("M", toggle_agent)
    obs, info = env.reset()
    obs_last = obs
    last_action_time = time.time()
    last_state = small_agent.state
    action = 4  # pass action
    while True:


        try:
            with open("agent_enabled.txt", "r") as f:
                agent_enabled = f.readlines()[0].startswith("yes")
        except:
            agent_enabled = True


        if agent_enabled:

            battle_status = env.read_m(0xD057)
            if battle_status != 0 and OUR_SMALL_AGENT:
                current_time = time.time()
                time_elapsed = current_time - last_action_time


                next_state = small_agent.get_state()

                #env.render()
                obs, rewards, terminated, truncated, info = env.step(7)
                if not (last_state == next_state).all():
                    last_state = next_state
                    last_action_time = time.time()

                if time_elapsed > 0.5:
                    small_agent.learn(action, terminated, truncated, next_state)
                    action = small_agent.act()
                    obs, rewards, terminated, truncated, info = env.step(action)
                    last_action_time = time.time()
                    print("action ", action)
            else:
                action_big_model, _states = model.predict(obs, deterministic=False)
                obs, rewards, terminated, truncated, info = env.step(action_big_model)
                env.render()
                action = 7 # action for
            if truncated:
                break
        env.render()
    env.close()
