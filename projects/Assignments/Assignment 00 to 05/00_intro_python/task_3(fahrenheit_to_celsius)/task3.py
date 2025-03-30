def main():
    print("Temperature Converter !")
    print ("Welcome this Temperature converter convert tempterature from  Fahrenhiet toCelsius. ")
    temp_f:float = float(input("Enter temperature in fahrenheit."))
    temp_c:float = (temp_f - 32) * 5.0/9.0 
    print(f"Temperature: {temp_f}F = {temp_c}C")
    
if __name__ == '__main__':
    main()