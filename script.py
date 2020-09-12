import sys

def default():
    print("HERE")
    print("Ahoj")

def cat():
    print("Mnau")

def dog():
    print("Haf")

def main():
    if sys.argv[1] == "dog":
        dog()
    if sys.argv[1] == "cat":
        cat()
    else:
        default()


if __name__ == "__main__":
    main()

