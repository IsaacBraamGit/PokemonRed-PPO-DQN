
pokemon_caught = 1


def handle_text():
    return


def perform_actions_in_env(overall_action,action_list, env, small_agent, pokemon_caught):
    pokemon_named = False
    for action in action_list:
        env.wait(10)
        obs, rewards, terminated, truncated, info = env.step(action)
    env.wait(100)

    if action_list[0] == 7:
        obs, rewards, terminated, truncated, info = env.step(7)
        return obs, rewards, terminated, truncated, info, pokemon_caught
    menu, slotbit2,health = 0, 0, 10

    battle_status = 1
    while (menu == 0 or (menu == 1 and slotbit2 == 1)) and battle_status >= 1:
        y_pos = env.read_m(0xCC24)
        x_pos = env.read_m(0xCC25)
        print("pos")
        print(x_pos)
        print(y_pos)

        if health == 0 and menu == 1 and slotbit2 == 1:
            env.wait(100)
            obs, rewards, terminated, truncated, info = env.step(4)
            env.wait(100)
            return obs, rewards, terminated, truncated, info, pokemon_caught

        else:
            if x_pos == 0 and y_pos == 1 and health > 0:
                print("here")
                env.wait(100)
                obs, rewards, terminated, truncated, info = env.step(5)
                env.wait(100)
                obs, rewards, terminated, truncated, info = env.step(5)
                env.wait(100)
                obs, rewards, terminated, truncated, info = env.step(5)
                return obs, rewards, terminated, truncated, info, pokemon_caught
        # name pokemon
        if overall_action == 11:
            if health != 0 and y_pos == 3 and x_pos == 1 and not pokemon_named and overall_action == 11:
                print("NAMING")
                for i in range(0,pokemon_caught):
                    obs, rewards, terminated, truncated, info = env.step(2)
                    env.wait(100)
                pokemon_caught += 1
                pokemon_named = True
        battle_status = env.read_m(0xD057)
        obs, rewards, terminated, truncated, info = env.step(4)
        state = small_agent.get_state()
        print(state)
        menu, slotbit2, health = state[0][-3], state[0][-1], state[0][0]
    # todo: sometimes the enemy is faster than us and we need to wait after another action
    #obs, rewards, terminated, truncated, info = env.step(4)
    return obs, rewards, terminated, truncated, info, pokemon_caught
