import sys

def default():
    print("Ahoj")

def cat():
    print("Mnau")

def main():
    if sys.argv[1] == "cat":
        cat()
    else:
        default()

if __name__ == "__main__":
    main()

