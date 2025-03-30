MARS_MULTIPLE:float = 0.378

def main():
    earth_weight_str:str = input("Enter a weight on earth: ")
    earth_weight:float = float(earth_weight_str)
    mars_weight:float = earth_weight * MARS_MULTIPLE
    round_mars = round(mars_weight,2)
    print(f"The equivalent weight on mars : {str(round_mars)}")

if __name__ == "__main__":
    main()