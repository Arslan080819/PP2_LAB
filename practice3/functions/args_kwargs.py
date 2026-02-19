def show_numbers(*args):
    for number in args:
        print(number)

def show_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_numbers(1, 2, 3, 4)
show_information(name="Arslan", age=20, city="Almaty")
