import math
import random

print("Exercise 1:")
nums = [5, 2, 9, -4]
print(min(nums))
print(max(nums))
print(abs(-25))

print("\nExercise 2:")
print(round(3.5678, 2))
print(pow(3, 4))

print("\nExercise 3:")
print(math.sqrt(25))
print(math.ceil(4.1))
print(math.floor(4.9))

print("\nExercise 4:")
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.pi)
print(math.e)

print("\nExercise 5:")
print(random.random())
print(random.randint(1, 100))

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)
