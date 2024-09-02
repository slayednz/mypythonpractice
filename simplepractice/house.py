name = input("What's your name? ").lower().strip().title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

print("Hello, "+name)