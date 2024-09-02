def greet(input):
    if "hello" in input:
        print("Hello, there")
    elif "goodbye" in input:
        print("Goodbye bro!")

greet(input("Say something? ").lower())