from random import random, uniform, randint,choice, choices, shuffle, sample

# array = [round(randint(1,16), 1) for _ range(3)] # randint : return a int random element from 1 to 16 included
array = [round(uniform(1,16),1) for _ in range(3)] # uniform : return a float random element from 1 to 16 included
random_float_number = random() # form 0.0 to 1.0 (excluded)
shuffle(array) # shuffle : shuffle the original array 
# choices : returns the selected item ; k <= len(array) or k > len(array)
# sample : without returning the selected item ; k <= len(array)
print(choices(array,k = 4))
print(sample(array, k = 2))