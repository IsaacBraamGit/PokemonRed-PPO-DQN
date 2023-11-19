

def perform_actions_in_env(action_list, env):
    obs, rewards, terminated, truncated, info = env.step(action_list[0])
    for action in action_list[1:]:
        obs, rewards, terminated, truncated, info = env.step(action)
    env.wait(300)
    return obs, rewards, terminated, truncated, info
