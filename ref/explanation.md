## Generating IVs

There is an IV (Inherent Value) for each stat in a pkmn, these are unchangeable values that represent a pkmn's genes that modify their stats and vary from .75 to 1.25.

IVs are generated randomly when you capture a pkmn by selecting a random number between 0 and 50, summing that with the equalizer value (we'll see about that in a minute), dividing the total by 100 and summing .75 to the result. By that, we get a value between .75 and 1.25

### Simulating the process

Let's simulate the creation of the IVs of our Bulbasaur

IVs are used in stat calculation to multiply a pkmns stat

They are separated in levels, for easy understanding

- Bad           (.75 - .84)
- Under Average (.85 - .94)
- Average       (.95 - 1.05)
- Above average (1.06 - 1.15)
- Excellent     (1.16 - 1.25)

After the IVs are generated, if the average is still lower than .95, the *pkmn* will have the **determined** hidden trait, this trait increases EV gain for the next 10 levels after its capture.

However, if their IV spread average is higher than 1.1, they'll have the **lazy** hidden trait, this trait impedes EV gain for the next 10 levels after capture.

## EV

Just like IVs, there are EV values for each pkmn stat, these are variable values that apply a static bonus to the pkmn total stat when they level up
the EV is added to the ev_sum of the pkmn on that stat and cant exceed 2 per level. Different events can alter a pkmn's EV.

Captured wild *pkmn* will have 0 EV in every stat and an ev_sum of 0


## pkmn_stats.json

poke_stats is the base stats of a pokemon, including its battle stats, species,
types and id for reference in other json

## pkmn_lvlup.json

poke_lvlup is what the pokemon gets when it levels up

Base Rules:

*pkmn* level_rewards can **never** be below .75
*pkmn* level_rewards generally don't go over 2, unless they are stage 3 evolved, in which case, it can be higher
*pkmn* level_rewards are based on the base stats of the species and the stage of their evolution, except some specific cases (e.g. kakuna and metapod//*pkmn* with only one stage)


the final value of a stat is calculated like this:

base_stat = stat from poke_stats.json
level = the pkmn level
level_rewards = the numbers in poke_lvlup on that stat
iv = pkmn inherent value for that stat (can range from .75 to 1.25)
ev_sum = sum of pkmn effort values for that stat, a pkmn ev can be raised in many different ways, but cannot be raised to more than 2 per level (e.g. a level 10 Bulbasaur could not have more than 20 EV in HP, any more EV that would be awarded are lost. That is, if it was caught at level 1. EV are only carried and applied when pkmn level up, then are reset)

((base_stat + (level * level_rewards)) * iv) + ev_sum

## Creating a Pokémon

All *pkmn* have a level, species and stats.

A *pkmn* is created by instantiating the appropriat class, it can be a: 

- WildPokemon for wild *pkmn*. They have no IVs or EVs nor names (they use their species' name in battle);
 
- SpecificPokemon for trainer *pkmn* or scripted *pkmn* battles. They have IVs but not EVs and can have names, although not mandatory;

- PlayerPokemon for the player's *pkmn*. They have IVs, EVs and ev_sum, personality traits, hidden traits and names (if assigned one)

Let's again, use a lvl 10 Bulbasaur as an example, for this example, we'll assume the Bulbasaur has gone through extreme training and has an ev_sum on each stat of 
[hp: 12, att: 5, def: 2, spd: 0, sp: 4]

and an iv spread of 
[hp: .79, att: 1.07, def: 1.23, spd: 1.22, sp: .86]

So, using the base stats of the Bulbasaur, which are
[hp: 9, att: 10, def: 10, spd: 9, sp: 13]

and having the level_rewards values for bulbasaur as
[hp: 1.3, att: 1.4, def: 1.4, spd: 1.0, sp: 1.9]

we can plug these values in out calcultator

HP => ((9 + (10 * 1.3)) * 0.79) + 12 => 29 (29.38)

## pkmn_evolve.json

the reference of every pkmn's requirements to evolve and what species it evolves to 