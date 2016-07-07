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
                
