
pokemon_caught = 1


def handle_text():
    return


def perform_actions_in_env(overall_action,action_list, env, small_agent, pokemon_caught):
    pokemon_named = False
    for action in action_list:
        env.wait(50)
        obs, rewards, terminated, truncated, info = env.step(action)
    env.wait(100)

    if action_list[0] == 7:
        obs, rewards, terminated, truncated, info = env.step(7)
        return obs, rewards, terminated, truncated, info, pokemon_caught
    menu, slotbit2,health = 0, 0, 10

    battle_status = 1
    y_pos = env.read_m(0xCC24)
    x_pos = env.read_m(0xCC25)
    while ((menu == 0 or (menu == 1 and slotbit2 == 1)) and battle_status >= 1) or (y_pos == 1 and x_pos == 3):
        y_pos = env.read_m(0xCC24)
        x_pos = env.read_m(0xCC25)

        if health == 0 and menu == 1 and slotbit2 == 1:
            env.wait(100)
            #obs, rewards, terminated, truncated, info = env.step(4)
            env.wait(100)

            health = state[0][0]
            y_pos = env.read_m(0xCC24)
            x_pos = env.read_m(0xCC25)

            #14 9 correct?
            if health == 0:
                while (y_pos == 10 and x_pos == 14) or (y_pos == 12 and x_pos ==12):
                    print("HERE3")
                    obs, rewards, terminated, truncated, info = env.step(4)
                    env.wait(100)
                    y_pos = env.read_m(0xCC24)
                    x_pos = env.read_m(0xCC25)
            return obs, rewards, terminated, truncated, info, pokemon_caught

        else:
            if x_pos == 0 and y_pos == 1 and health > 0:

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
                for i in range(0,pokemon_caught):
                    obs, rewards, terminated, truncated, info = env.step(2)
                    env.wait(100)
                pokemon_caught += 1
                pokemon_named = True
        battle_status = env.read_m(0xD057)
        obs, rewards, terminated, truncated, info = env.step(4)
        state = small_agent.get_state()
        menu, slotbit2, health = state[0][-3], state[0][-1], state[0][0]
    return obs, rewards, terminated, truncated, info, pokemon_caught
