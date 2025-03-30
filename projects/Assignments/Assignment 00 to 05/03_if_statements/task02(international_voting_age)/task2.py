def main():
    age:int = int(input("Enter old are you? "))
    PERTURKSBOUIPO= 16 
    STANLAU = 25
    MAYENGUA = 48


    if age >= PERTURKSBOUIPO:
        print(f"You can vote in Peturksbouipo where the voting age is {str(PERTURKSBOUIPO)}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {str(PERTURKSBOUIPO)}.")

    if age >= STANLAU:
        print(f"You can vote in Stanlau where the voting age is {str(STANLAU)}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {str(STANLAU)}.")

    if age >= MAYENGUA:
        print(f"You can vote in Mayengua where the voting age is {str(MAYENGUA)}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {str(MAYENGUA)}.")



if __name__ == '__main__':
    main()


 