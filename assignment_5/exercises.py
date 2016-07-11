import math

def to_fahrenheit(degrees_celsius):
    output = degrees_celsius * (9 / 5) + 32
    return output

def to_celsius(degrees_fahrenheit):
    output = (degrees_fahrenheit - 32) * 5 / 9
    return output 

print(to_celsius(11))
print(to_fahrenheit(11))

def get_fall_time(vertical_height):
    # gravity isn't going to change, units in m/(s^2)
    acceleration_by_gravity = 9.8

    time_elapsed = math.sqrt((2 * vertical_height) /  acceleration_by_gravity)
    # replace with logic of above equation
    return time_elapsed

print(get_fall_time(10))


def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

    time_in_air = get_fall_time(tower_height)

    tower_range = time_in_air * muzzle_velocity

    delta_x = tower_x - target_x  # difference between tower_x and target_x
    delta_y = tower_y - target_y  # difference between tower_y and target_y
    
    separation = math.sqrt((delta_x ** 2) + (delta_y **2)) 
    
    if separation < tower_range:
        print("The target is closer than the tower range, what should we return?")
        return True
    
    else:
        print("The target is further than the tower range, what should we return?")
        return False

isVulnerable(10,9,8,7,6)
