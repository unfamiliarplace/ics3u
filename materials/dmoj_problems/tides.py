# Tides
# https://dmoj.ca/problem/dmopc14c7p2

n_readings = int(input()) # unused

# Get the readings and split them by spaces
readings = input()
readings = readings.split()

# Convert every reading to an int
for i in range(len(readings)):
    readings[i] = int(readings[i])

# Find the lowest and highest values
lowest_value = min(readings)
highest_value = max(readings)

# Find WHERE they are so we only look between those two
i_lowest = readings.index(lowest_value)
i_highest = readings.index(highest_value)

# Between lowest and highest...
for i in range(i_lowest, i_highest):
    current_value = readings[i]
    next_value = readings[i + 1]
    
    # If it's not strictly increasing
    if current_value >= next_value:
        print('unknown')
        break
    
# If no break
else:
    
    # Special case! If the highest value precedes the lowest,
    # our loop would run zero times, so we need to manually set it
    if i_highest < i_lowest:
        print('unknown')
    
    # If we got here, data is fine
    else:
        print(highest_value - lowest_value)
