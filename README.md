# Pokémon Red with PPO and a DQN battle subnetwork

Based on the work done by PWhiddy. Find his full repo here: https://github.com/PWhiddy/PokemonRedExperiments/tree/master.

## Overview

Welcome to the Pokémon Red Reinforcement Learning Project! Our goal is to advance AI gameplay in the classic 1996 Pokémon Red video game using a Deep Q-Network (DQN) battle network. This project is a work in progress, focusing on enhancing the strategic depth an AI can achieve within the game's complex decision-making environment. We are building upon the foundational work of using Proximal Policy Optimization (PPO) for game navigation and battling, addressing its limitations by integrating a tailored DQN specifically for battle sequences.

## Current Capabilities

Our approach combines the exploration and navigation capabilities of PPO with s strategic battle DQN to significantly improve AI performance in Pokémon battles. The integration aims at:

- Navigating the game world efficiently with PPO, utilizing pixel data for movement and basic interactions.
- Engaging in battles with a more strategic depth through a DQN, designed to understand and exploit the intricacies of Pokémon battles, such as type advantages, move sets, and Pokémon stats.
- Overcoming the limitations of relying solely on pixel data for battle decisions, allowing the AI to develop more complex and effective battle strategies.

## Objectives

Our vision extends beyond merely playing Pokémon Red. We aim to push the boundaries of what AI can achieve in gaming environments characterized by high-dimensional state spaces and complex, rule-based interactions. Specifically, we are interested in:

- Demonstrating the potential of combining different RL techniques to tackle various aspects of complex games.
- Exploring the strategic depth that AI can reach in environments with incomplete information and significant randomness.

## Join Us!

This project is an open invitation to enthusiasts and experts alike in the fields of Reinforcement Learning, game theory, and AI. Whether you are interested in the technical aspects of RL algorithms, the strategic complexities of Pokémon battles, or the broader implications of AI in strategic decision-making, there is a place for you here.

### How You Can Contribute:

- **Algorithm Development**: Help us refine our RL models, explore new algorithms, and push the limits of AI gameplay.
- **Feature and Reward Engineering**: We have probably selected way to many features and reward compononents, but feel free to play around. In _our_model.py, the code of the DQN is visible.
- **Testing and Benchmarking**: Play a role in evaluating our AI's performance and identifying areas for improvement.
- **Cross-Domain Applications**: Explore how the strategies and techniques developed here can be applied to other domains and challenges.

## Acknowledgments

We are building upon the valuable work of researchers and developers in the field, particularly the foundational PPO network developed for Pokémon gameplay by PWhiddy. Thanks for this!

## Stay Tuned

As we mentioned, this project is still evolving. We are excited about the journey ahead and the potential discoveries to be made. Keep an eye on our updates, and don't hesitate to reach out if you are interested in contributing, have ideas, or simply want to learn more about the project.
