import random
import random_walk

def get_random_direction():
    direction = ""
    probability = random.random()

    if probability < 0.25:
        direction = "west"
   
    elif probability < 0.5:
        direction = "north" 
     
    elif probability < 0.75:
        direction = "south"
    
    else:
        direction = "east"

    return direction

print(get_random_direction())

random_dir = get_random_direction()

def get_direction_displacement(direction_key):
    displacements = {
        'west': (-1, 0),
        'east': (1, 0),
        'north': (0, 1),
        'south': (0, -1)
        }
    # access the dictionary
    # UPDATE HERE: how do you use the key to access a dictionary?
    # replace None with the answer
    return displacements[direction_key]


displacement = get_direction_displacement('east')

example_location = [1,0]

change_in_x = -1
change_in_y = 0
example_location[0] += change_in_x
example_location[1] += change_in_y

def take_walk(steps):
    current_location = [0, 0]
    for step_index in range(steps):
        direction = get_random_direction()

        displacement = get_direction_displacement(direction)

        # extract the numerical values from the tuple
        delta_x = displacement[0]
        delta_y = displacement[1]

        # UPDATE current_location HERE
        # consult example in 'Storing and Updating State' for method to update
        # current_location

    return current_location

    if __name__ == "__main__":
        steps = 10
        current_location = take_walk(steps)

        print("Done with walk, printing end location: ")
        print(current_location)
