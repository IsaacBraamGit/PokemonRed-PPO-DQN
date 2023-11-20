

def perform_actions_in_env(action_list, env):
    for action in action_list[:-1]:
        env.step(action)
    if not action_list[-1] == 7:
        env.wait(600)
    # todo: sometimes the enemy is faster than us and we need to wait after another action
    obs, rewards, terminated, truncated, info = env.step(action_list[-1])
    return obs, rewards, terminated, truncated, info
