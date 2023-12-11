import matplotlib.pyplot as plt
import numpy as np
def moving_average(data, window_size):
    """ Calculate the moving average over a specific window size. """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def read_rewards(file_path):
    with open(file_path, 'r') as file:
        rewards = []
        for line in file:
            if not "(" in line:
                rewards.append(float(line.split(",")[0].strip()))
            else:
                for i in range(6):
                    rewards.append(float(line.split(",")[0].strip()[1:]))

        #rewards = [float(line.split(",")[0].strip()) for line in file if not "(" in line]
    return rewards
def read_rewards_dqn(file_path):
    with open(file_path, 'r') as file:
        rewards = [float(line.strip()) for line in file]
    return rewards

def plot_rewards(rewards1, rewards2, labels):
    plt.figure(figsize=(10, 6))
    plt.plot(rewards1, label=labels[0])
    plt.plot(rewards2, label=labels[1])
    plt.xlabel('Time Step')
    plt.ylabel('Reward')
    plt.title('Rewards Over Time')
    plt.legend()
    plt.show()

# File paths
file_path1 = 'models/log_ppo_dqn.txt' # Update with actual file path
file_path2 = 'models/log_ppo.txt'    # Update with actual file path

# Read rewards
rewards_ppo_dqn = read_rewards(file_path1)
rewards_ppo = read_rewards(file_path2)
rewards_ppo_dqn = moving_average(rewards_ppo_dqn, 500)
rewards_ppo = moving_average(rewards_ppo, 500)

# Plot rewards
plot_rewards(rewards_ppo_dqn, rewards_ppo, ['PPO-DQN', 'PPO'])
