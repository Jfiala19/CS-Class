#9/27/18 Question2 https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
import random
c = [x for x in range(1, 101)]
random.shuffle(c)
print("Your list has been shuffled\n\n", *c)