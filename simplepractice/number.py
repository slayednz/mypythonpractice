def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    y = get_int("What's y ? ")
    print(f"So y is {y} and x is {x}, therefore x + y is {x + y}!")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError or NameError:
            pass

main()
