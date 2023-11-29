from bs4 import BeautifulSoup

# Your HTML content
html_content = """
<table class="wikitable prettytable sortable jquery-tablesorter" style="width:100%;text-align:center;">
<thead><tr>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Move</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Type</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Power</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Accuracy</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">PP</th>
<th class="unsortable">Description
</th></tr></thead><tbody>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Absorb_(move)" class="extiw" title="bulbapedia:Absorb (move)">Absorb</a></td>
<td>Grass</td>
<td>20</td>
<td>100%</td>
<td>20</td>
<td>User recovers half of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Acid_(move)" class="extiw" title="bulbapedia:Acid (move)">Acid</a></td>
<td>Poison</td>
<td>40</td>
<td>100%</td>
<td>20</td>
<td>10% chance of lowering opponent's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Acid_Armor_(move)" class="extiw" title="bulbapedia:Acid Armor (move)">Acid Armor</a></td>
<td>Poison</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises user's defense by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Agility_(move)" class="extiw" title="bulbapedia:Agility (move)">Agility</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Raises user's speed by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Amnesia_(move)" class="extiw" title="bulbapedia:Amnesia (move)">Amnesia</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Raises user's special by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Aurora_Beam_(move)" class="extiw" title="bulbapedia:Aurora Beam (move)">Aurora Beam</a></td>
<td>Ice</td>
<td>65</td>
<td>100%</td>
<td>20</td>
<td>10% chance of lowering opponent's attack by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Barrage_(move)" class="extiw" title="bulbapedia:Barrage (move)">Barrage</a></td>
<td>Normal</td>
<td>15</td>
<td>85%</td>
<td>20</td>
<td>Attacks opponent repeatedly.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Barrier_(move)" class="extiw" title="bulbapedia:Barrier (move)">Barrier</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Raises user's defense by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bide_(move)" class="extiw" title="bulbapedia:Bide (move)">Bide</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>User doesn't attack for 2-3 turns, then attacks with double the damage received from the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bind_(move)" class="extiw" title="bulbapedia:Bind (move)">Bind</a></td>
<td>Normal</td>
<td>15</td>
<td>75%</td>
<td>10</td>
<td>Attacks for 2-5 turns; opponent cannot attack until Bind finishes.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bite_(move)" class="extiw" title="bulbapedia:Bite (move)">Bite</a></td>
<td>Normal</td>
<td>60</td>
<td>100%</td>
<td>25</td>
<td>30% chance the opponent flinches afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Blizzard_(move)" class="extiw" title="bulbapedia:Blizzard (move)">Blizzard</a></td>
<td>Ice</td>
<td>120</td>
<td>90%</td>
<td>5</td>
<td>10% chance of freezing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Body_Slam_(move)" class="extiw" title="bulbapedia:Body Slam (move)">Body Slam</a></td>
<td>Normal</td>
<td>85</td>
<td>100%</td>
<td>15</td>
<td>30% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bone_Club_(move)" class="extiw" title="bulbapedia:Bone Club (move)">Bone Club</a></td>
<td>Ground</td>
<td>65</td>
<td>85%</td>
<td>20</td>
<td>10% chance the opponent flinches afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bonemerang_(move)" class="extiw" title="bulbapedia:Bonemerang (move)">Bonemerang</a></td>
<td>Ground</td>
<td>50</td>
<td>90%</td>
<td>10</td>
<td>Attacks opponent twice in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bubble_(move)" class="extiw" title="bulbapedia:Bubble (move)">Bubble</a></td>
<td>Water</td>
<td>20</td>
<td>100%</td>
<td>30</td>
<td>10% chance of lowering opponent's speed by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Bubblebeam_(move)" class="extiw" title="bulbapedia:Bubblebeam (move)">Bubblebeam</a></td>
<td>Water</td>
<td>60</td>
<td>100%</td>
<td>20</td>
<td>10% chance of lowering opponent's speed by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Clamp_(move)" class="extiw" title="bulbapedia:Clamp (move)">Clamp</a></td>
<td>Water</td>
<td>35</td>
<td>75%</td>
<td>10</td>
<td>Attacks for 2-5 turns; opponent cannot attack until Clamp finishes.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Comet_Punch_(move)" class="extiw" title="bulbapedia:Comet Punch (move)">Comet Punch</a></td>
<td>Normal</td>
<td>18</td>
<td>85%</td>
<td>15</td>
<td>Attacks opponent 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Confuse_Ray_(move)" class="extiw" title="bulbapedia:Confuse Ray (move)">Confuse Ray</a></td>
<td>Ghost</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>Confuses the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Confusion_(move)" class="extiw" title="bulbapedia:Confusion (move)">Confusion</a></td>
<td>Psychic</td>
<td>50</td>
<td>100%</td>
<td>25</td>
<td>10% chance of confusing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Constrict_(move)" class="extiw" title="bulbapedia:Constrict (move)">Constrict</a></td>
<td>Normal</td>
<td>10</td>
<td>100%</td>
<td>35</td>
<td>10% chance of lowering opponent's speed by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Conversion_(move)" class="extiw" title="bulbapedia:Conversion (move)">Conversion</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>User's type changes into opponent's type.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Counter_(move)" class="extiw" title="bulbapedia:Counter (move)">Counter</a></td>
<td>Fighting</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Attacks second, inflicting double the damage of opponent's attack when hit with a Normal or Fighting move.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Crabhammer_(move)" class="extiw" title="bulbapedia:Crabhammer (move)">Crabhammer</a></td>
<td>Water</td>
<td>90</td>
<td>85%</td>
<td>10</td>
<td>Critical hit chance multiplied by 8.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Cut_(move)" class="extiw" title="bulbapedia:Cut (move)">Cut</a></td>
<td>Normal</td>
<td>50</td>
<td>95%</td>
<td>30</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Defense_Curl_(move)" class="extiw" title="bulbapedia:Defense Curl (move)">Defense Curl</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises user's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Dig_(move)" class="extiw" title="bulbapedia:Dig (move)">Dig</a></td>
<td>Ground</td>
<td>100</td>
<td>100%</td>
<td>10</td>
<td>User goes underground for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Disable_(move)" class="extiw" title="bulbapedia:Disable (move)">Disable</a></td>
<td>Normal</td>
<td>0</td>
<td>55%</td>
<td>20</td>
<td>Randomly disables one of the opponent's attacks for 2-5 turns.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Dizzy_Punch_(move)" class="extiw" title="bulbapedia:Dizzy Punch (move)">Dizzy Punch</a></td>
<td>Normal</td>
<td>70</td>
<td>100%</td>
<td>20</td>
<td>20% chance of confusing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Double-Edge_(move)" class="extiw" title="bulbapedia:Double-Edge (move)">Double-Edge</a></td>
<td>Normal</td>
<td>100</td>
<td>100%</td>
<td>10</td>
<td>User takes 1/4th of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Double_Kick_(move)" class="extiw" title="bulbapedia:Double Kick (move)">Double Kick</a></td>
<td>Fighting</td>
<td>30</td>
<td>100%</td>
<td>30</td>
<td>Attacks twice in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Doubleslap_(move)" class="extiw" title="bulbapedia:Doubleslap (move)">Doubleslap</a></td>
<td>Normal</td>
<td>15</td>
<td>85%</td>
<td>10</td>
<td>Attacks 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Double_Team_(move)" class="extiw" title="bulbapedia:Double Team (move)">Double Team</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>15</td>
<td>Raises user's evasion by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Dragon_Rage_(move)" class="extiw" title="bulbapedia:Dragon Rage (move)">Dragon Rage</a></td>
<td>Dragon</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>Does 40 HP of damage on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Dream_Eater_(move)" class="extiw" title="bulbapedia:Dream Eater (move)">Dream Eater</a></td>
<td>Psychic</td>
<td>100</td>
<td>100%</td>
<td>15</td>
<td>Half of damage dealt to opponent is recovered as health; opponent must be asleep for it to work.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Drill_Peck_(move)" class="extiw" title="bulbapedia:Drill Peck (move)">Drill Peck</a></td>
<td>Flying</td>
<td>80</td>
<td>100%</td>
<td>20</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Earthquake_(move)" class="extiw" title="bulbapedia:Earthquake (move)">Earthquake</a></td>
<td>Ground</td>
<td>100</td>
<td>100%</td>
<td>10</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Egg_Bomb_(move)" class="extiw" title="bulbapedia:Egg Bomb (move)">Egg Bomb</a></td>
<td>Normal</td>
<td>100</td>
<td>75%</td>
<td>10</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Ember_(move)" class="extiw" title="bulbapedia:Ember (move)">Ember</a></td>
<td>Fire</td>
<td>40</td>
<td>100%</td>
<td>25</td>
<td>10% of burning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Explosion_(move)" class="extiw" title="bulbapedia:Explosion (move)">Explosion</a></td>
<td>Normal</td>
<td>170</td>
<td>100%</td>
<td>5</td>
<td>User faints and opponent's defense is halved after attack.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fire_Blast_(move)" class="extiw" title="bulbapedia:Fire Blast (move)">Fire Blast</a></td>
<td>Fire</td>
<td>120</td>
<td>85%</td>
<td>5</td>
<td>10% chance of burning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fire_Punch_(move)" class="extiw" title="bulbapedia:Fire Punch (move)">Fire Punch</a></td>
<td>Fire</td>
<td>75</td>
<td>100%</td>
<td>15</td>
<td>10% chance of burning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fire_Spin_(move)" class="extiw" title="bulbapedia:Fire Spin (move)">Fire Spin</a></td>
<td>Fire</td>
<td>15</td>
<td>70%</td>
<td>15</td>
<td>Attacks for 2-5 turns; opponent cannot attack until Fire Spin finishes.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fissure_(move)" class="extiw" title="bulbapedia:Fissure (move)">Fissure</a></td>
<td>Ground</td>
<td>0</td>
<td>30%</td>
<td>5</td>
<td>One-shots the opponent unless the attack is not first or the opponent is a Normal or Fighting type.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Flamethrower_(move)" class="extiw" title="bulbapedia:Flamethrower (move)">Flamethrower</a></td>
<td>Fire</td>
<td>95</td>
<td>100%</td>
<td>15</td>
<td>10% chance of burning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Flash_(move)" class="extiw" title="bulbapedia:Flash (move)">Flash</a></td>
<td>Normal</td>
<td>0</td>
<td>70%</td>
<td>20</td>
<td>Lowers opponent accuracy by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fly_(move)" class="extiw" title="bulbapedia:Fly (move)">Fly</a></td>
<td>Flying</td>
<td>70</td>
<td>95%</td>
<td>15</td>
<td>User goes in the air for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Focus_Energy_(move)" class="extiw" title="bulbapedia:Focus Energy (move)">Focus Energy</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>User's critical hit chance is divided by 4.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fury_Attack_(move)" class="extiw" title="bulbapedia:Fury Attack (move)">Fury Attack</a></td>
<td>Normal</td>
<td>15</td>
<td>85%</td>
<td>20</td>
<td>Attacks 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Fury_Swipes_(move)" class="extiw" title="bulbapedia:Fury Swipes (move)">Fury Swipes</a></td>
<td>Normal</td>
<td>15</td>
<td>85%</td>
<td>15</td>
<td>Attacks 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Glare_(move)" class="extiw" title="bulbapedia:Glare (move)">Glare</a></td>
<td>Normal</td>
<td>0</td>
<td>75%</td>
<td>30</td>
<td>Paralyzes the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Growl_(move)" class="extiw" title="bulbapedia:Growl (move)">Growl</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Lowers opponent's attack by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Growth_(move)" class="extiw" title="bulbapedia:Growth (move)">Growth</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises user's special by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Guillotine_(move)" class="extiw" title="bulbapedia:Guillotine (move)">Guillotine</a></td>
<td>Normal</td>
<td>0</td>
<td>30%</td>
<td>5</td>
<td>One-shots the opponent unless the attack is not first or the opponent is a Normal or Fighting type.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Gust_(move)" class="extiw" title="bulbapedia:Gust (move)">Gust</a></td>
<td>Normal</td>
<td>40</td>
<td>100%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Harden_(move)" class="extiw" title="bulbapedia:Harden (move)">Harden</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises the user's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Haze_(move)" class="extiw" title="bulbapedia:Haze (move)">Haze</a></td>
<td>Ice</td>
<td>70</td>
<td>100%</td>
<td>30</td>
<td>All stat boosts and reductions of both fighters are removed; the user's status infliction is removed.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Headbutt_(move)" class="extiw" title="bulbapedia:Headbutt (move)">Headbutt</a></td>
<td>Normal</td>
<td>70</td>
<td>100%</td>
<td>15</td>
<td>30% chance the opponent flinches afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Hi_Jump_Kick_(move)" class="extiw" title="bulbapedia:Hi Jump Kick (move)">Hi Jump Kick</a></td>
<td>Fighting</td>
<td>85</td>
<td>90%</td>
<td>20</td>
<td>If attack misses, user takes 1 HP of damage.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Horn_Attack_(move)" class="extiw" title="bulbapedia:Horn Attack (move)">Horn Attack</a></td>
<td>Normal</td>
<td>65</td>
<td>100%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Horn_Drill_(move)" class="extiw" title="bulbapedia:Horn Drill (move)">Horn Drill</a></td>
<td>Normal</td>
<td>0</td>
<td>30%</td>
<td>5</td>
<td>One-shots the opponent unless the attack is not first or the opponent is a Normal or Fighting type.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Hydro_Pump_(move)" class="extiw" title="bulbapedia:Hydro Pump (move)">Hydro Pump</a></td>
<td>Water</td>
<td>120</td>
<td>80%</td>
<td>5</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Hyper_Beam_(move)" class="extiw" title="bulbapedia:Hyper Beam (move)">Hyper Beam</a></td>
<td>Normal</td>
<td>150</td>
<td>90%</td>
<td>5</td>
<td>After attacking, user must take his next turn recharging unless the opponent faints.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Hyper_Fang_(move)" class="extiw" title="bulbapedia:Hyper Fang (move)">Hyper Fang</a></td>
<td>Normal</td>
<td>80</td>
<td>90%</td>
<td>15</td>
<td>10% the opponent finches afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Hypnosis_(move)" class="extiw" title="bulbapedia:Hypnosis (move)">Hypnosis</a></td>
<td>Psychic</td>
<td>0</td>
<td>60%</td>
<td>20</td>
<td>Opponent falls asleep.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Ice_Beam_(move)" class="extiw" title="bulbapedia:Ice Beam (move)">Ice Beam</a></td>
<td>Ice</td>
<td>95</td>
<td>100%</td>
<td>15</td>
<td>10% chance of freezing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Ice_Punch_(move)" class="extiw" title="bulbapedia:Ice Punch (move)">Ice Punch</a></td>
<td>Ice</td>
<td>75</td>
<td>100%</td>
<td>15</td>
<td>10% chance of freezing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Jump_Kick_(move)" class="extiw" title="bulbapedia:Jump Kick (move)">Jump Kick</a></td>
<td>Fighting</td>
<td>70</td>
<td>95%</td>
<td>25</td>
<td>If attack misses, user takes 1/8th of the damage toward the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Karate_Chop_(move)" class="extiw" title="bulbapedia:Karate Chop (move)">Karate Chop</a></td>
<td>Normal</td>
<td>50</td>
<td>100%</td>
<td>25</td>
<td>Critical hit chance multiplied by 8.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Kinesis_(move)" class="extiw" title="bulbapedia:Kinesis (move)">Kinesis</a></td>
<td>Psychic</td>
<td>0</td>
<td>80%</td>
<td>15</td>
<td>Lowers opponent's accuracy by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Leech_Life_(move)" class="extiw" title="bulbapedia:Leech Life (move)">Leech Life</a></td>
<td>Bug</td>
<td>20</td>
<td>100%</td>
<td>15</td>
<td>User recovers half of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Leech_Seed_(move)" class="extiw" title="bulbapedia:Leech Seed (move)">Leech Seed</a></td>
<td>Grass</td>
<td>0</td>
<td>90%</td>
<td>10</td>
<td>After the turn ends, 1/8th of the opponent's maximum HP is taken and added to the user's HP.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Leer_(move)" class="extiw" title="bulbapedia:Leer (move)">Leer</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Lowers the opponent's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Lick_(move)" class="extiw" title="bulbapedia:Lick (move)">Lick</a></td>
<td>Ghost</td>
<td>20</td>
<td>100%</td>
<td>30</td>
<td>30% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Light_Screen_(move)" class="extiw" title="bulbapedia:Light Screen (move)">Light Screen</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>User's special stat is doubled.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Lovely_Kiss_(move)" class="extiw" title="bulbapedia:Lovely Kiss (move)">Lovely Kiss</a></td>
<td>Normal</td>
<td>0</td>
<td>75%</td>
<td>15</td>
<td>Opponent falls asleep.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Low_Kick_(move)" class="extiw" title="bulbapedia:Low Kick (move)">Low Kick</a></td>
<td>Fighting</td>
<td>50</td>
<td>90%</td>
<td>20</td>
<td>30% chance the opponent flinches afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Meditate_(move)" class="extiw" title="bulbapedia:Meditate (move)">Meditate</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises user's attack by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mega_Drain_(move)" class="extiw" title="bulbapedia:Mega Drain (move)">Mega Drain</a></td>
<td>Grass</td>
<td>40</td>
<td>100%</td>
<td>10</td>
<td>User recovers half of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mega_Kick_(move)" class="extiw" title="bulbapedia:Mega Kick (move)">Mega Kick</a></td>
<td>Normal</td>
<td>120</td>
<td>75%</td>
<td>5</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mega_Punch_(move)" class="extiw" title="bulbapedia:Mega Punch (move)">Mega Punch</a></td>
<td>Normal</td>
<td>80</td>
<td>85%</td>
<td>20</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Metronome_(move)" class="extiw" title="bulbapedia:Metronome (move)">Metronome</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>User does a random move.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mimic_(move)" class="extiw" title="bulbapedia:Mimic (move)">Mimic</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>Mimic is replaced with one of the opponent's moves at random.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Minimize_(move)" class="extiw" title="bulbapedia:Minimize (move)">Minimize</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Raises user's evasion by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mirror_Move_(move)" class="extiw" title="bulbapedia:Mirror Move (move)">Mirror Move</a></td>
<td>Flying</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>User attacks with the opponent's last move.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Mist_(move)" class="extiw" title="bulbapedia:Mist (move)">Mist</a></td>
<td>Ice</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Opponent cannot reduce user's stats.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Night_Shade_(move)" class="extiw" title="bulbapedia:Night Shade (move)">Night Shade</a></td>
<td>Ghost</td>
<td>0</td>
<td>100%</td>
<td>15</td>
<td>Damages the opponent a fixed amount of HP depending on the user's level.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Pay_Day_(move)" class="extiw" title="bulbapedia:Pay Day (move)">Pay Day</a></td>
<td>Normal</td>
<td>40</td>
<td>100%</td>
<td>20</td>
<td>Receive bonus money equal to the user's level multiplied by 2 after battle.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Peck_(move)" class="extiw" title="bulbapedia:Peck (move)">Peck</a></td>
<td>Flying</td>
<td>35</td>
<td>100%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Petal_Dance_(move)" class="extiw" title="bulbapedia:Petal Dance (move)">Petal Dance</a></td>
<td>Grass</td>
<td>90</td>
<td>100%</td>
<td>20</td>
<td>Attacks for 2-3 turns; after the attack, the user becomes confused.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Pin_Missile_(move)" class="extiw" title="bulbapedia:Pin Missile (move)">Pin Missile</a></td>
<td>Bug</td>
<td>14</td>
<td>85%</td>
<td>20</td>
<td>Attacks 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Poison_Gas_(move)" class="extiw" title="bulbapedia:Poison Gas (move)">Poison Gas</a></td>
<td>Poison</td>
<td>0</td>
<td>55%</td>
<td>40</td>
<td>Poisons the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Poisonpowder_(move)" class="extiw" title="bulbapedia:Poisonpowder (move)">Poisonpowder</a></td>
<td>Poison</td>
<td>0</td>
<td>75%</td>
<td>35</td>
<td>Poisons the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Poison_Sting_(move)" class="extiw" title="bulbapedia:Poison Sting (move)">Poison Sting</a></td>
<td>Poison</td>
<td>15</td>
<td>100%</td>
<td>35</td>
<td>30% chance of poisoning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Pound_(move)" class="extiw" title="bulbapedia:Pound (move)">Pound</a></td>
<td>Normal</td>
<td>40</td>
<td>100%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Psybeam_(move)" class="extiw" title="bulbapedia:Psybeam (move)">Psybeam</a></td>
<td>Psychic</td>
<td>65</td>
<td>100%</td>
<td>20</td>
<td>10% chance of confusing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Psychic_(move)" class="extiw" title="bulbapedia:Psychic (move)">Psychic</a></td>
<td>Psychic</td>
<td>90</td>
<td>100%</td>
<td>10</td>
<td>30% chance of lowering the opponent's special by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Psywave_(move)" class="extiw" title="bulbapedia:Psywave (move)">Psywave</a></td>
<td>Psychic</td>
<td>0</td>
<td>80%</td>
<td>15</td>
<td>Randomly does damage from 1 to 1.5 times the user's level.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Quick_Attack_(move)" class="extiw" title="bulbapedia:Quick Attack (move)">Quick Attack</a></td>
<td>Normal</td>
<td>40</td>
<td>100%</td>
<td>30</td>
<td>Always attacks the opponent first.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Rage_(move)" class="extiw" title="bulbapedia:Rage (move)">Rage</a></td>
<td>Normal</td>
<td>20</td>
<td>100%</td>
<td>20</td>
<td>User is enraged, having its attack increase by 1 from every hit.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Razor_Leaf_(move)" class="extiw" title="bulbapedia:Razor Leaf (move)">Razor Leaf</a></td>
<td>Grass</td>
<td>55</td>
<td>95%</td>
<td>25</td>
<td>Critical hit chance is multiplied by 8.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Razor_Wind_(move)" class="extiw" title="bulbapedia:Razor Wind (move)">Razor Wind</a></td>
<td>Normal</td>
<td>80</td>
<td>75%</td>
<td>15</td>
<td>User charges for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Recover_(move)" class="extiw" title="bulbapedia:Recover (move)">Recover</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Recovers half of the user's maximum HP.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Reflect_(move)" class="extiw" title="bulbapedia:Reflect (move)">Reflect</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>User's defense stat is doubled.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Rest_(move)" class="extiw" title="bulbapedia:Rest (move)">Rest</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>User recovers all HP and falls asleep for 2 turns, overwriting any status effects.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Roar_(move)" class="extiw" title="bulbapedia:Roar (move)">Roar</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Wild Pokémon flee from battle after use.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Rock_Slide_(move)" class="extiw" title="bulbapedia:Rock Slide (move)">Rock Slide</a></td>
<td>Rock</td>
<td>75</td>
<td>90%</td>
<td>10</td>
<td>30% chance of opponent flinching afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Rock_Throw_(move)" class="extiw" title="bulbapedia:Rock Throw (move)">Rock Throw</a></td>
<td>Rock</td>
<td>50</td>
<td>90%</td>
<td>15</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Rolling_Kick_(move)" class="extiw" title="bulbapedia:Rolling Kick (move)">Rolling Kick</a></td>
<td>Fighting</td>
<td>60</td>
<td>85%</td>
<td>15</td>
<td>30% chance of opponent flinching afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sand-Attack_(move)" class="extiw" title="bulbapedia:Sand-Attack (move)">Sand-Attack</a></td>
<td>Ground</td>
<td>0</td>
<td>100%</td>
<td>15</td>
<td>Lowers opponent's accuracy by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Scratch_(move)" class="extiw" title="bulbapedia:Scratch (move)">Scratch</a></td>
<td>Normal</td>
<td>40</td>
<td>100%</td>
<td>30</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Screech_(move)" class="extiw" title="bulbapedia:Screech (move)">Screech</a></td>
<td>Normal</td>
<td>0</td>
<td>85%</td>
<td>40</td>
<td>Lowers opponent's defense by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Seismic_Toss_(move)" class="extiw" title="bulbapedia:Seismic Toss (move)">Seismic Toss</a></td>
<td>Fighting</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Damages the opponent a fixed amount of HP depending on the user's level.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Selfdestruct_(move)" class="extiw" title="bulbapedia:Selfdestruct (move)">Selfdestruct</a></td>
<td>Normal</td>
<td>130</td>
<td>100%</td>
<td>5</td>
<td>User faints and opponent's defense is halved after attack.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sharpen_(move)" class="extiw" title="bulbapedia:Sharpen (move)">Sharpen</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Raises user's attack by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sing_(move)" class="extiw" title="bulbapedia:Sing (move)">Sing</a></td>
<td>Normal</td>
<td>0</td>
<td>55%</td>
<td>15</td>
<td>Opponent falls asleep.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Skull_Bash_(move)" class="extiw" title="bulbapedia:Skull Bash (move)">Skull Bash</a></td>
<td>Normal</td>
<td>100</td>
<td>100%</td>
<td>15</td>
<td>User lowers head for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sky_Attack_(move)" class="extiw" title="bulbapedia:Sky Attack (move)">Sky Attack</a></td>
<td>Flying</td>
<td>140</td>
<td>95%</td>
<td>5</td>
<td>User charges for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Slam_(move)" class="extiw" title="bulbapedia:Slam (move)">Slam</a></td>
<td>Normal</td>
<td>80</td>
<td>75%</td>
<td>20</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Slash_(move)" class="extiw" title="bulbapedia:Slash (move)">Slash</a></td>
<td>Normal</td>
<td>70</td>
<td>100%</td>
<td>20</td>
<td>Critical hit chance multiplied by 8.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sleep_Powder_(move)" class="extiw" title="bulbapedia:Sleep Powder (move)">Sleep Powder</a></td>
<td>Grass</td>
<td>0</td>
<td>75%</td>
<td>15</td>
<td>Opponent falls asleep.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sludge_(move)" class="extiw" title="bulbapedia:Sludge (move)">Sludge</a></td>
<td>Poison</td>
<td>65</td>
<td>100%</td>
<td>20</td>
<td>30% chance of poisoning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Smog_(move)" class="extiw" title="bulbapedia:Smog (move)">Smog</a></td>
<td>Poison</td>
<td>20</td>
<td>70%</td>
<td>20</td>
<td>40% chance of poisoning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Smokescreen_(move)" class="extiw" title="bulbapedia:Smokescreen (move)">Smokescreen</a></td>
<td>Poison</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Lowers opponent's accuracy by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Softboiled_(move)" class="extiw" title="bulbapedia:Softboiled (move)">Softboiled</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>Recovers half of the user's maximum HP.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Solarbeam_(move)" class="extiw" title="bulbapedia:Solarbeam (move)">Solarbeam</a></td>
<td>Grass</td>
<td>120</td>
<td>100%</td>
<td>10</td>
<td>User charges for the first turn, then attacks on the second turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Sonicboom_(move)" class="extiw" title="bulbapedia:Sonicboom (move)">Sonicboom</a></td>
<td>Normal</td>
<td>0</td>
<td>90%</td>
<td>20</td>
<td>Does 20 HP of damage on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Spike_Cannon_(move)" class="extiw" title="bulbapedia:Spike Cannon (move)">Spike Cannon</a></td>
<td>Normal</td>
<td>20</td>
<td>100%</td>
<td>15</td>
<td>Attacks 2-5 times in succession.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Splash_(move)" class="extiw" title="bulbapedia:Splash (move)">Splash</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Does nothing significant.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Spore_(move)" class="extiw" title="bulbapedia:Spore (move)">Spore</a></td>
<td>Grass</td>
<td>0</td>
<td>100%</td>
<td>15</td>
<td>Opponent falls asleep.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Stomp_(move)" class="extiw" title="bulbapedia:Stomp (move)">Stomp</a></td>
<td>Normal</td>
<td>65</td>
<td>100%</td>
<td>20</td>
<td>30% chance of opponent flinching afterward.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Strength_(move)" class="extiw" title="bulbapedia:Strength (move)">Strength</a></td>
<td>Normal</td>
<td>80</td>
<td>100%</td>
<td>15</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/String_Shot_(move)" class="extiw" title="bulbapedia:String Shot (move)">String Shot</a></td>
<td>Bug</td>
<td>0</td>
<td>95%</td>
<td>40</td>
<td>Lowers opponent's speed by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Struggle_(move)" class="extiw" title="bulbapedia:Struggle (move)">Struggle</a></td>
<td>Normal</td>
<td>50</td>
<td>100%</td>
<td>0</td>
<td>When user is out of PP, Struggle is used automatically; user takes 1/4th of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Stun_Spore_(move)" class="extiw" title="bulbapedia:Stun Spore (move)">Stun Spore</a></td>
<td>Grass</td>
<td>0</td>
<td>75%</td>
<td>30</td>
<td>Paralyzes the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Submission_(move)" class="extiw" title="bulbapedia:Submission (move)">Submission</a></td>
<td>Fighting</td>
<td>80</td>
<td>80%</td>
<td>25</td>
<td>User takes 1/4th of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Substitute_(move)" class="extiw" title="bulbapedia:Substitute (move)">Substitute</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>User takes 1/4th of its maximum HP and creates a substitute that remains in battle until the opponent defeats it.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Super_Fang_(move)" class="extiw" title="bulbapedia:Super Fang (move)">Super Fang</a></td>
<td>Normal</td>
<td>0</td>
<td>90%</td>
<td>10</td>
<td>Reduces opponent's current HP by 1/2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Supersonic_(move)" class="extiw" title="bulbapedia:Supersonic (move)">Supersonic</a></td>
<td>Normal</td>
<td>0</td>
<td>55%</td>
<td>20</td>
<td>Confuses the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Surf_(move)" class="extiw" title="bulbapedia:Surf (move)">Surf</a></td>
<td>Water</td>
<td>95</td>
<td>100%</td>
<td>15</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Swift_(move)" class="extiw" title="bulbapedia:Swift (move)">Swift</a></td>
<td>Normal</td>
<td>60</td>
<td>100%</td>
<td>20</td>
<td>Attack ignores evade and accuracy boosts and can hit opponents using Fly or Dig
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Swords_Dance_(move)" class="extiw" title="bulbapedia:Swords Dance (move)">Swords Dance</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>30</td>
<td>Raises user's attack by 2.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Tackle_(move)" class="extiw" title="bulbapedia:Tackle (move)">Tackle</a></td>
<td>Normal</td>
<td>35</td>
<td>95%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Tail_Whip_(move)" class="extiw" title="bulbapedia:Tail Whip (move)">Tail Whip</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Lowers the opponent's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Take_Down_(move)" class="extiw" title="bulbapedia:Take Down (move)">Take Down</a></td>
<td>Normal</td>
<td>90</td>
<td>85%</td>
<td>20</td>
<td>User takes 1/4th of damage inflicted on opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Teleport_(move)" class="extiw" title="bulbapedia:Teleport (move)">Teleport</a></td>
<td>Psychic</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>User escapes from wild battles.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thrash_(move)" class="extiw" title="bulbapedia:Thrash (move)">Thrash</a></td>
<td>Normal</td>
<td>90</td>
<td>100%</td>
<td>20</td>
<td>Attacks for 2-3 turns; after the attack, the user becomes confused.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thunder_(move)" class="extiw" title="bulbapedia:Thunder (move)">Thunder</a></td>
<td>Electric</td>
<td>120</td>
<td>70%</td>
<td>10</td>
<td>10% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thunderbolt_(move)" class="extiw" title="bulbapedia:Thunderbolt (move)">Thunderbolt</a></td>
<td>Electric</td>
<td>95</td>
<td>100%</td>
<td>15</td>
<td>10% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thunderpunch_(move)" class="extiw" title="bulbapedia:Thunderpunch (move)">Thunderpunch</a></td>
<td>Electric</td>
<td>75</td>
<td>100%</td>
<td>15</td>
<td>10% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thundershock_(move)" class="extiw" title="bulbapedia:Thundershock (move)">Thundershock</a></td>
<td>Electric</td>
<td>40</td>
<td>100%</td>
<td>40</td>
<td>10% chance of paralyzing the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Thunder_Wave_(move)" class="extiw" title="bulbapedia:Thunder Wave (move)">Thunder Wave</a></td>
<td>Electric</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Paralyzes the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Toxic_(move)" class="extiw" title="bulbapedia:Toxic (move)">Toxic</a></td>
<td>Poison</td>
<td>0</td>
<td>85%</td>
<td>10</td>
<td>Poisons the opponent; damage inflicted on the opponent increases by 1/16th of the opponent's maximum HP each turn.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Transform_(move)" class="extiw" title="bulbapedia:Transform (move)">Transform</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>10</td>
<td>User becomes the opponent's form with his stats (except HP) and moves with 5 PP for each move.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Tri_Attack_(move)" class="extiw" title="bulbapedia:Tri Attack (move)">Tri Attack</a></td>
<td>Normal</td>
<td>80</td>
<td>100%</td>
<td>10</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Twineedle_(move)" class="extiw" title="bulbapedia:Twineedle (move)">Twineedle</a></td>
<td>Bug</td>
<td>25</td>
<td>100%</td>
<td>20</td>
<td>Attacks twice in succession; 20% chance of poisoning the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Vicegrip_(move)" class="extiw" title="bulbapedia:Vicegrip (move)">Vicegrip</a></td>
<td>Normal</td>
<td>55</td>
<td>100%</td>
<td>30</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Vine_Whip_(move)" class="extiw" title="bulbapedia:Vine Whip (move)">Vine Whip</a></td>
<td>Grass</td>
<td>35</td>
<td>100%</td>
<td>10</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Waterfall_(move)" class="extiw" title="bulbapedia:Waterfall (move)">Waterfall</a></td>
<td>Water</td>
<td>80</td>
<td>100%</td>
<td>15</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Water_Gun_(move)" class="extiw" title="bulbapedia:Water Gun (move)">Water Gun</a></td>
<td>Water</td>
<td>40</td>
<td>100%</td>
<td>25</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Whirlwind_(move)" class="extiw" title="bulbapedia:Whirlwind (move)">Whirlwind</a></td>
<td>Normal</td>
<td>0</td>
<td>100%</td>
<td>20</td>
<td>Wild Pokémon flee from battle after use.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Wing_Attack_(move)" class="extiw" title="bulbapedia:Wing Attack (move)">Wing Attack</a></td>
<td>Flying</td>
<td>35</td>
<td>100%</td>
<td>35</td>
<td>Attacks the opponent.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Withdraw_(move)" class="extiw" title="bulbapedia:Withdraw (move)">Withdraw</a></td>
<td>Water</td>
<td>0</td>
<td>100%</td>
<td>40</td>
<td>Raises the user's defense by 1.
</td></tr>
<tr>
<td><a href="https://bulbapedia.bulbagarden.net/wiki/Wrap_(move)" class="extiw" title="bulbapedia:Wrap (move)">Wrap</a></td>
<td>Normal</td>
<td>15</td>
<td>85%</td>
<td>15</td>
<td>Attacks for 2-5 turns; opponent cannot attack until Wrap finishes.
</td></tr></tbody><tfoot></tfoot></table>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'lxml')

# Find the table
table = soup.find('table', class_='wikitable prettytable sortable jquery-tablesorter')

# Iterate through each row in the table and extract information
moves = {}
for row in table.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    move_name = cols[0].get_text(strip=True)
    move_type = cols[1].get_text(strip=True)
    move_power = cols[2].get_text(strip=True)
    move_accuracy = cols[3].get_text(strip=True)
    move_pp = cols[4].get_text(strip=True)
    move_description = cols[5].get_text(strip=True)

    # Add the data to the dictionary
    moves[move_name] = {
        'Type': move_type,
        'Power': int(move_power),
        'Accuracy': int(move_accuracy[:-1]) / 100,
    }

# Print the result
print(moves)
