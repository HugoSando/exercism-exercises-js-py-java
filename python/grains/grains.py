def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    elif isinstance(number, float):
        raise ValueError("number must be int")
    
    grains_on_square = 1
    
    for i in range(number - 1):
        grains_on_square *= 2

    return grains_on_square

def total():
    total = 0
    grains_on_square = 1
    
    for i in range(64):
        total += grains_on_square
        grains_on_square *= 2

    return total
