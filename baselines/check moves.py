move_mappings = {1: 'Pound', 2: 'Karate Chop', 3: 'Double Slap', 4: 'Comet Punch', 5: 'Mega Punch',
                      6: 'Pay Day', 7: 'Fire Punch', 8: 'Ice Punch', 9: 'Thunder Punch', 10: 'Scratch',
                      11: 'Vicegrip', 12: 'Guillotine', 13: 'Razor Wind', 14: 'Swords Dance', 15: 'Cut',
                      16: 'Gust', 17: 'Wing Attack', 18: 'Whirlwind', 19: 'Fly', 20: 'Bind', 21: 'Slam',
                      22: 'Vine Whip', 23: 'Stomp', 24: 'Double Kick', 25: 'Mega Kick', 26: 'Jump Kick',
                      27: 'Rolling Kick', 28: 'Sand Attack', 29: 'Headbutt', 30: 'Horn Attack',
                      31: 'Fury Attack', 32: 'Horn Drill', 33: 'Tackle', 34: 'Body Slam', 35: 'Wrap',
                      36: 'Take Down', 37: 'Thrash', 38: 'Double-Edge', 39: 'Tail Whip', 40: 'Poison Sting',
                      41: 'Twineedle', 42: 'Pin Missile', 43: 'Leer', 44: 'Bite', 45: 'Growl', 46: 'Roar',
                      47: 'Sing', 48: 'Supersonic', 49: 'Sonic Boom', 50: 'Disable', 51: 'Acid', 52: 'Ember',
                      53: 'Flamethrower', 54: 'Mist', 55: 'Water Gun', 56: 'Hydro Pump', 57: 'Surf',
                      58: 'Ice Beam', 59: 'Blizzard', 60: 'Psybeam', 61: 'Bubblebeam', 62: 'Aurora Beam',
                      63: 'Hyper Beam', 64: 'Peck', 65: 'Drill Peck', 66: 'Submission', 67: 'Low Kick',
                      68: 'Counter', 69: 'Seismic Toss', 70: 'Strength', 71: 'Absorb', 72: 'Mega Drain',
                      73: 'Leech Seed', 74: 'Growth', 75: 'Razor Leaf', 76: 'Solar Beam', 77: 'Poison Powder',
                      78: 'Stun Spore', 79: 'Sleep Powder', 80: 'Petal Dance', 81: 'String Shot',
                      82: 'Dragon Rage', 83: 'Fire Spin', 84: 'Thunder Shock', 85: 'Thunder Bolt',
                      86: 'Thunder Wave', 87: 'Thunder', 88: 'Rock Throw', 89: 'Earthquake', 90: 'Fissure',
                      91: 'Dig', 92: 'Toxic', 93: 'Confusion', 94: 'Psychic', 95: 'Hypnosis', 96: 'Meditate',
                      97: 'Agility', 98: 'Quick Attack', 99: 'Rage', 100: 'Teleport', 101: 'Night Shade',
                      102: 'Mimic', 103: 'Screech', 104: 'Double Team', 105: 'Recover', 106: 'Harden',
                      107: 'Minimize', 108: 'Smokescreen', 109: 'Confuse Ray', 110: 'Withdraw',
                      111: 'Defense Curl', 112: 'Barrier', 113: 'Light Screen', 114: 'Haze', 115: 'Reflect',
                      116: 'Focus Energy', 117: 'Bide', 118: 'Metronome', 119: 'Mirror Move',
                      120: 'Self-Destruct', 121: 'Egg Bomb', 122: 'Lick', 123: 'Smog', 124: 'Sludge',
                      125: 'Bone Club', 126: 'Fire Blast', 127: 'Waterfall', 128: 'Clamp', 129: 'Swift',
                      130: 'Skull Bash', 131: 'Spike Cannon', 132: 'Constrict', 133: 'Amnesia', 134: 'Kinesis',
                      135: 'Soft-Boiled', 136: 'High Jump Kick', 137: 'Glare', 138: 'Dream Eater',
                      139: 'Poison Gas', 140: 'Barrage', 141: 'Leech Life', 142: 'Lovely Kiss',
                      143: 'Sky Attack', 144: 'Transform', 145: 'Bubble', 146: 'Dizzy Punch', 147: 'Spore',
                      148: 'Flash', 149: 'Psywave', 150: 'Splash', 151: 'Acid Armor', 152: 'Crabhammer',
                      153: 'Explosion', 154: 'Fury Swipes', 155: 'Bonemerang', 156: 'Rest', 157: 'Rock Slide',
                      158: 'Hyper Fang', 159: 'Sharpen', 160: 'Conversion', 161: 'Tri Attack',
                      162: 'Super Fang', 163: 'Slash', 164: 'Substitute', 165: 'Struggle'}

move_details = {'Absorb': {'Type': 'Grass', 'Power': 20, 'Accuracy': 1.0},
                     'Acid': {'Type': 'Poison', 'Power': 40, 'Accuracy': 1.0},
                     'Acid Armor': {'Type': 'Poison', 'Power': 0, 'Accuracy': 1.0},
                     'Agility': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Amnesia': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Aurora Beam': {'Type': 'Ice', 'Power': 65, 'Accuracy': 1.0},
                     'Barrage': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.85},
                     'Barrier': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Bide': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Bind': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.75},
                     'Bite': {'Type': 'Normal', 'Power': 60, 'Accuracy': 1.0},
                     'Blizzard': {'Type': 'Ice', 'Power': 120, 'Accuracy': 0.9},
                     'Body Slam': {'Type': 'Normal', 'Power': 85, 'Accuracy': 1.0},
                     'Bone Club': {'Type': 'Ground', 'Power': 65, 'Accuracy': 0.85},
                     'Bonemerang': {'Type': 'Ground', 'Power': 50, 'Accuracy': 0.9},
                     'Bubble': {'Type': 'Water', 'Power': 20, 'Accuracy': 1.0},
                     'Bubblebeam': {'Type': 'Water', 'Power': 60, 'Accuracy': 1.0},
                     'Clamp': {'Type': 'Water', 'Power': 35, 'Accuracy': 0.75},
                     'Comet Punch': {'Type': 'Normal', 'Power': 18, 'Accuracy': 0.85},
                     'Confuse Ray': {'Type': 'Ghost', 'Power': 0, 'Accuracy': 1.0},
                     'Confusion': {'Type': 'Psychic', 'Power': 50, 'Accuracy': 1.0},
                     'Constrict': {'Type': 'Normal', 'Power': 10, 'Accuracy': 1.0},
                     'Conversion': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Counter': {'Type': 'Fighting', 'Power': 0, 'Accuracy': 1.0},
                     'Crabhammer': {'Type': 'Water', 'Power': 90, 'Accuracy': 0.85},
                     'Cut': {'Type': 'Normal', 'Power': 50, 'Accuracy': 0.95},
                     'Defense Curl': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Dig': {'Type': 'Ground', 'Power': 100, 'Accuracy': 1.0},
                     'Disable': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.55},
                     'Dizzy Punch': {'Type': 'Normal', 'Power': 70, 'Accuracy': 1.0},
                     'Double-Edge': {'Type': 'Normal', 'Power': 100, 'Accuracy': 1.0},
                     'Double Kick': {'Type': 'Fighting', 'Power': 30, 'Accuracy': 1.0},
                     'Double Slap': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.85},
                     'Double Team': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Dragon Rage': {'Type': 'Dragon', 'Power': 0, 'Accuracy': 1.0},
                     'Dream Eater': {'Type': 'Psychic', 'Power': 100, 'Accuracy': 1.0},
                     'Drill Peck': {'Type': 'Flying', 'Power': 80, 'Accuracy': 1.0},
                     'Earthquake': {'Type': 'Ground', 'Power': 100, 'Accuracy': 1.0},
                     'Egg Bomb': {'Type': 'Normal', 'Power': 100, 'Accuracy': 0.75},
                     'Ember': {'Type': 'Fire', 'Power': 40, 'Accuracy': 1.0},
                     'Explosion': {'Type': 'Normal', 'Power': 170, 'Accuracy': 1.0},
                     'Fire Blast': {'Type': 'Fire', 'Power': 120, 'Accuracy': 0.85},
                     'Fire Punch': {'Type': 'Fire', 'Power': 75, 'Accuracy': 1.0},
                     'Fire Spin': {'Type': 'Fire', 'Power': 15, 'Accuracy': 0.7},
                     'Fissure': {'Type': 'Ground', 'Power': 0, 'Accuracy': 0.3},
                     'Flamethrower': {'Type': 'Fire', 'Power': 95, 'Accuracy': 1.0},
                     'Flash': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.7},
                     'Fly': {'Type': 'Flying', 'Power': 70, 'Accuracy': 0.95},
                     'Focus Energy': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Fury Attack': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.85},
                     'Fury Swipes': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.85},
                     'Glare': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.75},
                     'Growl': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Growth': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Guillotine': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.3},
                     'Gust': {'Type': 'Normal', 'Power': 40, 'Accuracy': 1.0},
                     'Harden': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Haze': {'Type': 'Ice', 'Power': 70, 'Accuracy': 1.0},
                     'Headbutt': {'Type': 'Normal', 'Power': 70, 'Accuracy': 1.0},
                     'High Jump Kick': {'Type': 'Fighting', 'Power': 85, 'Accuracy': 0.9},
                     'Horn Attack': {'Type': 'Normal', 'Power': 65, 'Accuracy': 1.0},
                     'Horn Drill': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.3},
                     'Hydro Pump': {'Type': 'Water', 'Power': 120, 'Accuracy': 0.8},
                     'Hyper Beam': {'Type': 'Normal', 'Power': 150, 'Accuracy': 0.9},
                     'Hyper Fang': {'Type': 'Normal', 'Power': 80, 'Accuracy': 0.9},
                     'Hypnosis': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 0.6},
                     'Ice Beam': {'Type': 'Ice', 'Power': 95, 'Accuracy': 1.0},
                     'Ice Punch': {'Type': 'Ice', 'Power': 75, 'Accuracy': 1.0},
                     'Jump Kick': {'Type': 'Fighting', 'Power': 70, 'Accuracy': 0.95},
                     'Karate Chop': {'Type': 'Normal', 'Power': 50, 'Accuracy': 1.0},
                     'Kinesis': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 0.8},
                     'Leech Life': {'Type': 'Bug', 'Power': 20, 'Accuracy': 1.0},
                     'Leech Seed': {'Type': 'Grass', 'Power': 0, 'Accuracy': 0.9},
                     'Leer': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Lick': {'Type': 'Ghost', 'Power': 20, 'Accuracy': 1.0},
                     'Light Screen': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Lovely Kiss': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.75},
                     'Low Kick': {'Type': 'Fighting', 'Power': 50, 'Accuracy': 0.9},
                     'Meditate': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Mega Drain': {'Type': 'Grass', 'Power': 40, 'Accuracy': 1.0},
                     'Mega Kick': {'Type': 'Normal', 'Power': 120, 'Accuracy': 0.75},
                     'Mega Punch': {'Type': 'Normal', 'Power': 80, 'Accuracy': 0.85},
                     'Metronome': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Mimic': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Minimize': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Mirror Move': {'Type': 'Flying', 'Power': 0, 'Accuracy': 1.0},
                     'Mist': {'Type': 'Ice', 'Power': 0, 'Accuracy': 1.0},
                     'Night Shade': {'Type': 'Ghost', 'Power': 0, 'Accuracy': 1.0},
                     'Pay Day': {'Type': 'Normal', 'Power': 40, 'Accuracy': 1.0},
                     'Peck': {'Type': 'Flying', 'Power': 35, 'Accuracy': 1.0},
                     'Petal Dance': {'Type': 'Grass', 'Power': 90, 'Accuracy': 1.0},
                     'Pin Missile': {'Type': 'Bug', 'Power': 14, 'Accuracy': 0.85},
                     'Poison Gas': {'Type': 'Poison', 'Power': 0, 'Accuracy': 0.55},
                     'Poison Powder': {'Type': 'Poison', 'Power': 0, 'Accuracy': 0.75},
                     'Poison Sting': {'Type': 'Poison', 'Power': 15, 'Accuracy': 1.0},
                     'Pound': {'Type': 'Normal', 'Power': 40, 'Accuracy': 1.0},
                     'Psybeam': {'Type': 'Psychic', 'Power': 65, 'Accuracy': 1.0},
                     'Psychic': {'Type': 'Psychic', 'Power': 90, 'Accuracy': 1.0},
                     'Psywave': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 0.8},
                     'Quick Attack': {'Type': 'Normal', 'Power': 40, 'Accuracy': 1.0},
                     'Rage': {'Type': 'Normal', 'Power': 20, 'Accuracy': 1.0},
                     'Razor Leaf': {'Type': 'Grass', 'Power': 55, 'Accuracy': 0.95},
                     'Razor Wind': {'Type': 'Normal', 'Power': 80, 'Accuracy': 0.75},
                     'Recover': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Reflect': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Rest': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Roar': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Rock Slide': {'Type': 'Rock', 'Power': 75, 'Accuracy': 0.9},
                     'Rock Throw': {'Type': 'Rock', 'Power': 50, 'Accuracy': 0.9},
                     'Rolling Kick': {'Type': 'Fighting', 'Power': 60, 'Accuracy': 0.85},
                     'Sand Attack': {'Type': 'Ground', 'Power': 0, 'Accuracy': 1.0},
                     'Scratch': {'Type': 'Normal', 'Power': 40, 'Accuracy': 1.0},
                     'Screech': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.85},
                     'Seismic Toss': {'Type': 'Fighting', 'Power': 0, 'Accuracy': 1.0},
                     'Self-Destruct': {'Type': 'Normal', 'Power': 130, 'Accuracy': 1.0},
                     'Sharpen': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Sing': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.55},
                     'Skull Bash': {'Type': 'Normal', 'Power': 100, 'Accuracy': 1.0},
                     'Sky Attack': {'Type': 'Flying', 'Power': 140, 'Accuracy': 0.95},
                     'Slam': {'Type': 'Normal', 'Power': 80, 'Accuracy': 0.75},
                     'Slash': {'Type': 'Normal', 'Power': 70, 'Accuracy': 1.0},
                     'Sleep Powder': {'Type': 'Grass', 'Power': 0, 'Accuracy': 0.75},
                     'Sludge': {'Type': 'Poison', 'Power': 65, 'Accuracy': 1.0},
                     'Smog': {'Type': 'Poison', 'Power': 20, 'Accuracy': 0.7},
                     'Smokescreen': {'Type': 'Poison', 'Power': 0, 'Accuracy': 1.0},
                     'Soft-Boiled': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Solar Beam': {'Type': 'Grass', 'Power': 120, 'Accuracy': 1.0},
                     'Sonic Boom': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.9},
                     'Spike Cannon': {'Type': 'Normal', 'Power': 20, 'Accuracy': 1.0},
                     'Splash': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Spore': {'Type': 'Grass', 'Power': 0, 'Accuracy': 1.0},
                     'Stomp': {'Type': 'Normal', 'Power': 65, 'Accuracy': 1.0},
                     'Strength': {'Type': 'Normal', 'Power': 80, 'Accuracy': 1.0},
                     'String Shot': {'Type': 'Bug', 'Power': 0, 'Accuracy': 0.95},
                     'Struggle': {'Type': 'Normal', 'Power': 50, 'Accuracy': 1.0},
                     'Stun Spore': {'Type': 'Grass', 'Power': 0, 'Accuracy': 0.75},
                     'Submission': {'Type': 'Fighting', 'Power': 80, 'Accuracy': 0.8},
                     'Substitute': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Super Fang': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.9},
                     'Supersonic': {'Type': 'Normal', 'Power': 0, 'Accuracy': 0.55},
                     'Surf': {'Type': 'Water', 'Power': 95, 'Accuracy': 1.0},
                     'Swift': {'Type': 'Normal', 'Power': 60, 'Accuracy': 1.0},
                     'Swords Dance': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Tackle': {'Type': 'Normal', 'Power': 35, 'Accuracy': 0.95},
                     'Tail Whip': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Take Down': {'Type': 'Normal', 'Power': 90, 'Accuracy': 0.85},
                     'Teleport': {'Type': 'Psychic', 'Power': 0, 'Accuracy': 1.0},
                     'Thrash': {'Type': 'Normal', 'Power': 90, 'Accuracy': 1.0},
                     'Thunder': {'Type': 'Electric', 'Power': 120, 'Accuracy': 0.7},
                     'Thunder Bolt': {'Type': 'Electric', 'Power': 95, 'Accuracy': 1.0},
                     'Thunder Punch': {'Type': 'Electric', 'Power': 75, 'Accuracy': 1.0},
                     'Thunder Shock': {'Type': 'Electric', 'Power': 40, 'Accuracy': 1.0},
                     'Thunder Wave': {'Type': 'Electric', 'Power': 0, 'Accuracy': 1.0},
                     'Toxic': {'Type': 'Poison', 'Power': 0, 'Accuracy': 0.85},
                     'Transform': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Tri Attack': {'Type': 'Normal', 'Power': 80, 'Accuracy': 1.0},
                     'Twineedle': {'Type': 'Bug', 'Power': 25, 'Accuracy': 1.0},
                     'Vicegrip': {'Type': 'Normal', 'Power': 55, 'Accuracy': 1.0},
                     'Vine Whip': {'Type': 'Grass', 'Power': 35, 'Accuracy': 1.0},
                     'Waterfall': {'Type': 'Water', 'Power': 80, 'Accuracy': 1.0},
                     'Water Gun': {'Type': 'Water', 'Power': 40, 'Accuracy': 1.0},
                     'Whirlwind': {'Type': 'Normal', 'Power': 0, 'Accuracy': 1.0},
                     'Wing Attack': {'Type': 'Flying', 'Power': 35, 'Accuracy': 1.0},
                     'Withdraw': {'Type': 'Water', 'Power': 0, 'Accuracy': 1.0},
                     'Wrap': {'Type': 'Normal', 'Power': 15, 'Accuracy': 0.85}}


def check_move_names(move_mappings, move_details):
    mismatched_names = []
    for move_id, move_name in move_mappings.items():
        # Check if the move name in move_mappings exists in move_details
        if move_name not in move_details:
            mismatched_names.append(move_name)
    return mismatched_names

# Using the function to find mismatches
mismatched_moves = check_move_names(move_mappings, move_details)

# Printing mismatched moves
print("Mismatched Moves:", mismatched_moves)