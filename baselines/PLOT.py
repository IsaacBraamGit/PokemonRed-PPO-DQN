import matplotlib.pyplot as plt
import numpy as np

# Function to smooth the data using a moving average
def moving_average(data, window_size):
    """ Calculate the moving average over a specific window size. """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Path to the log file
file_path = 'models/log_dqn_model_v1.0.txt'

# Read the file contents
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extracting rewards from each line
rewards = []
for line in lines:
    try:
        # Extracting the reward part, which is the fourth element in the tuple
        reward = float(line.split(',')[3].strip())
        rewards.append(reward)
    except Exception as e:
        print(f"Error processing line: {line}\n{e}")

# Plotting the original rewards
plt.figure(figsize=(12, 6))
plt.plot(rewards, label='Rewards')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.title('Rewards Over Episodes')
plt.legend()
plt.show()

# Smoothing the rewards with a moving average
window_size = 100  # Window size for the moving average
smoothed_rewards = moving_average(rewards, window_size)

# Plotting the smoothed rewards
plt.figure(figsize=(12, 6))
plt.plot(smoothed_rewards, label='Smoothed Rewards', color='orange')
plt.xlabel('Episodes')
plt.ylabel('Smoothed Reward')
plt.title(f'Rewards Over Episodes (Smoothed with window size {window_size})')
plt.legend()
plt.show()
