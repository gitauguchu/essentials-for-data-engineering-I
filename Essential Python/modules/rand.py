#Generates random numbers or shuffles lists adding a dash of predictability to our programs
import random

#Generating random numbers within a range
random_number = random.randint(1, 10)
print(random_number)

#Shuffling lists
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list", my_list, sep=":")

#Generating a random float between 0 and 1
random_float = random.random()
print("Random float", random_float, sep=":")

#Choosing a random element from a sequence
my_sequence = ["apple", "banana", "orange", "pineapple"]
random_element = random.choice(my_sequence)
print(random_element)

#Generating a random sample from a population
sample = random.sample(range(1, 101), 5)
print("Random sample", sample, sep=":")

#Randomly select an element with replacement
random_element_with_replacement = random.choices(["A", "B", "C", "D"], k=3) #Selects 3 elements with replacement
print("Random element with replacement", random_element_with_replacement, sep=":")

#Set the random seed for reproducibility
random.seed(1234)

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

#Resetting the seed to the same value will produce the same sequence of random numbers
random.seed(1234)

print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))