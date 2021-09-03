# COVID SPREAD SIMULATOR
# VERSION B

# Imports
import random

# Constants
POPULATION = 10000
START_SICK = 5
DAYS = 30
SPREAD_VICTIMS = 3
CHANCE_SPREAD = 25 # %

# Variables
current_sick = START_SICK

# Simulator

# For every day
for i in range(DAYS):

    # For every sick person
    for j in range(current_sick):

        # For each possible victim
        for k in range(SPREAD_VICTIMS):

            # Roll a die
            die_roll = random.randint(1, 100)

            # If it's under the chance to spread, add 1 sick person
            if die_roll < CHANCE_SPREAD:
                current_sick += 1

    # Make sure we don't have more sick people than population
    if current_sick >= POPULATION:
        current_sick = POPULATION

        # End the loop early -- no point running longer if everyone's sick
        break

    # Daily report
    print(f'After {i + 1} days, {current_sick} people are sick')

# Final report
print(f'After {i + 1} days, {current_sick} people are sick')


