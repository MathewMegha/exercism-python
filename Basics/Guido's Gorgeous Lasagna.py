
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): Time the lasagna has already been baking.

    Returns:
        int: The remaining bake time in minutes.

    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
     Calculate preparation time based on number of layers.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The preparation time in minutes.

    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    #Task 5
    """
    Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time




#Task 1
print(EXPECTED_BAKE_TIME)

#Task 2
print(bake_time_remaining(20))

#Task 3
print(preparation_time_in_minutes(3))

#Task 4
print(elapsed_time_in_minutes(3, 20))
