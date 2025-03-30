MINIMUM_HEIGHT:int = 50

def main():
    while True:
        height:int = int(input("How tall are you? "))
        if height >= MINIMUM_HEIGHT:
            print("You are tall enough to ride!")
            break
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()