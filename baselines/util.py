def handle_text():
    return


def perform_actions_in_env(action_list, env, small_agent):
    for action in action_list:
        obs, rewards, terminated, truncated, info = env.step(action)
    env.wait(100)

    if action_list[0] == 7:
        obs, rewards, terminated, truncated, info = env.step(7)
        return obs, rewards, terminated, truncated, info
    menu, slotbit2,health = 0, 0, 10
    battle_status = 1
    while (menu == 0 or (menu == 1 and slotbit2 == 1)) and battle_status >= 1:
        if health == 0 and menu == 1 and slotbit2 == 1:
            env.wait(100)
            obs, rewards, terminated, truncated, info = env.step(4)
            env.wait(100)
            return obs, rewards, terminated, truncated, info
        battle_status = env.read_m(0xD057)
        obs, rewards, terminated, truncated, info = env.step(4)
        state = small_agent.get_state()
        print(state)
        menu, slotbit2, health = state[0][-3], state[0][-1], state[0][0]
    # todo: sometimes the enemy is faster than us and we need to wait after another action
    #obs, rewards, terminated, truncated, info = env.step(4)
    return obs, rewards, terminated, truncated, info
