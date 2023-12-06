import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

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
            return float(parts[3])
        except ValueError:
            return None

# Path to the log file
file_path = 'models/log_dqn_model_v1.0.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process the data
entries = combine_lines_into_entries(lines)
rewards = [extract_reward_from_entry(entry) for entry in entries]

# Plotting the rewards
plt.figure(figsize=(12, 6))
plt.plot(rewards, label='Rewards')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.title('Rewards Over Episodes')
plt.legend()
plt.savefig("rewards")
plt.show()
