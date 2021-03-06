import random

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





displacement = get_direction_displacement(random_dir)



