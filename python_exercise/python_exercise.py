def square(n):
    '''Square a number n'''
    return n**2

def get_first_100():
    '''get a list of the first 100 natural numbers'''
    return list(range(1, 101))

def square_list(list_numbers):
    '''Square each number in a list of numbers, returning a new list'''
    return_value = []
    for number in list_numbers:
       return_value.append(square(number))
       return return_value 

def solve_problem():
    first_100 = get_first_100()
    sum_squares_first_hundred = sum(square_list(first_100))
    square_sum_first_hundred = square(sum(first_100))
    return sum_squares_first_hundred - square_sum_first_hundred

if __name__ == '__main__':
    print(solve_problem())
