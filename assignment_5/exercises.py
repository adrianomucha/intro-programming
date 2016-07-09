import math

def to_fahrenheit(degrees_celsius):
    output = degrees_celsius * (9 / 5) +  32
    return output


def to_celsius(degrees_fahrenheit):
    otuput = (degrees_fahrenheit - 32) * 5 /9
    return output

to_fahrenheit(0)

print (to_fahrenheit(0))
print (to_fahrenheit(50))
print (to_fahrenheit(100))


#def get_fall_time(height):
def vertical_height(time_elapsed):
    return (((1/2) * 9.8) * time_elapsed * time_elapsed)

def get_fall_time(height):
    return math.sqrt((2 * height) / (9.8))                      

print(vertical_height(10))
print(get_fall_time(20))

def isVulnerable(tower_height, tower_x, tower_y, target_x, target_y):
    muzzle_velocity = 300

 # update this line to calculate time_in_air using get_fall_time() function
def  time_in_air(height):
    return math.sqrt((2 * height) / (9.8)) 

    tower_range = time_in_air * muzzle_velocity

    delta_x = None  # difference between tower_x and target_x
    delta_y = None  # difference between tower_y and target_y

    separation = None  # the x and y deltas form a triangle, find the hypotenuse
    if separation < tower_range:

        print("The target is closer than the tower range, what should we return?")
    return None
    
    else:
        print("The target is further than the tower range, what should we return?")
    return None
