import sys

def default():
    print("Ahoj")

def dog():
    print("Haf")

def main():
    if sys.argv[1] == "dog":
        dog()
    else:
        default()

if __name__ == "__main__":
    main()

