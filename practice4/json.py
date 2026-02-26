import json

print("Exercise 1:")
x = '{"name":"John","age":30}'
y = json.loads(x)
print(y)

print("\nExercise 2:")
data = {"name": "Arslan", "age": 20}
json_str = json.dumps(data, indent=4)
print(json_str)

print("\nExercise 3:")
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
print("Written to file")

print("\nExercise 4:")
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded)

print("\nExercise 5:")
try:
    with open("sample-data.json", "r") as f:
        sample = json.load(f)
        print(sample)
except FileNotFoundError:
    print("sample-data.json not found")
