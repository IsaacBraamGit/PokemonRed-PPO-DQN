import matplotlib.pyplot as plt
import numpy as np

# Models to be plotted
models = [4.0]

# Function to combine lines into entries
def combine_lines_into_entries(lines):
    entries = []
    current_entry = ""
    for line in lines:
        current_entry += line.strip()
        if line.strip().endswith(')'):
            entries.append(current_entry)
            current_entry = ""
    return entries

# Function to extract rewards from each entry
def extract_reward_from_entry(entry):
    parts = []
    current_part = ''
    bracket_level = 0
    for char in entry:
        if char == '[':
            bracket_level += 1
        elif char == ']':
            bracket_level -= 1
        if char == ',' and bracket_level == 0:
            parts.append(current_part.strip())
            current_part = ''
        else:
            current_part += char
    parts.append(current_part.strip())
    if len(parts) > 3:
        try:
            if parts[3] == None:
                return 0
            return float(parts[3])
        except ValueError:
            return 0

# Function for moving average
def moving_average(data, window_size):
    """ Calculate the moving average over a specific window size. """
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Set up the plot
# Collect all reward lists
all_rewards = []

# Set up the plot
plt.figure(figsize=(12, 6))

# Loop through each model
for model in models:
    file_path = f'models/log_dqn_model_v{model}.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process the data
    entries = combine_lines_into_entries(lines)
    rewards = [extract_reward_from_entry(entry) for entry in entries]
    all_rewards.append(rewards)
    reward = [r for r in rewards if isinstance(r,float)]
    # Calculate smoothed rewards
    #smoothed = moving_average(rewards, 500)
    smoothed = [sum(filter(None, reward[n:n+1000]))/1000 for n in range(len(rewards))]
    #smoothed = [r/100 for r in smoothed if isinstance(r,int)]

    # Plotting the rewards
    plt.plot(smoothed, label=f'Model version {model}')


# Finalizing the plot
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.title('Smoothed Rewards Over Episodes for Multiple Models')
plt.legend()
plt.show()
