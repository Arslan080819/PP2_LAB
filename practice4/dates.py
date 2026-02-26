from datetime import datetime, timedelta, timezone

print("Exercise 1:")
now = datetime.now()
print(now)

print("\nExercise 2:")
d = datetime(2024, 12, 31)
print(d)

print("\nExercise 3:")
formatted = now.strftime("%d/%m/%Y")
print(formatted)

print("\nExercise 4:")
future = now + timedelta(days=7)
diff = future - now
print("Days difference:", diff.days)

print("\nExercise 5:")
utc_time = datetime.now(timezone.utc)
print(utc_time)