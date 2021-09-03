# COVID SPREAD SIMULATOR
# VERSION A

# Constants
POPULATION = 10000
START_SICK = 5
DAYS = 30
SPREAD_VICTIMS = 3

# Variables
current_sick = START_SICK

# Simulator

# For every day
for i in range(DAYS):

    # For every sick person
    for j in range(current_sick):

        # Add the number of new victims
        current_sick += SPREAD_VICTIMS

    # Make sure we don't have more sick people than population
    if current_sick >= POPULATION:
        current_sick = POPULATION

        # End the loop early -- no point running longer if everyone's sick
        break

    # Daily report
    print(f'After {i + 1} days, {current_sick} people are sick')

# Final report
print(f'After {i + 1} days, {current_sick} people are sick')


