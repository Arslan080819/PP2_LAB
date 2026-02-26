print("Exercise 1:")
my_list = [10, 20, 30]
it = iter(my_list)
print(next(it))
print(next(it))
print(next(it))

print("\nExercise 2:")
my_tuple = ("apple", "banana", "cherry")
it2 = iter(my_tuple)
for item in it2:
    print(item)

print("\nExercise 3:")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
obj = MyNumbers()
for x in obj:
    print(x)

print("\nExercise 4:")
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num)

print("\nExercise 5:")
squares = (x**2 for x in range(6))
for s in squares:
    print(s)
