# Prompt the user for temprature in Celsius and return it in Kelvin

def main() -> None:
    print("\n===============Temprature Converter===============")


    while True:
        try:
            temprature_in_celsius = float(input("\nEnter temprature in Celsius: "))
        except ValueError:
            print("\n❌-----It is not a valid temprature.-----❌")
            continue
        
        temprature_in_kelvin = temprature_in_celsius + 273.15
        temprature_in_fahrenheit = (temprature_in_celsius * (9 / 5)) + 32
        print(f"\n{temprature_in_celsius} C equals to {temprature_in_kelvin} K and {temprature_in_fahrenheit} F.")
        
        again = input("Do you want to convert temprature again? ")
        if again != "y":
            break


if __name__ == "__main__":
    main()