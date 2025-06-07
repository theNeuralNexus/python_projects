# Prompt the user for temprature in Celsius and return it in Kelvin

def main() -> None:
    print("\n===============Temprature Converter===============")

    while True:
        try:
            temprature_in_celsius = float(input("\nEnter temprature in Celsius: "))
        except ValueError:
            print("\n❌-----It is not a valid temprature.-----❌")
            continue
        
        conversion = input("\nDo you want to convert it into K or F? ").lower()

        if conversion == "k":
            converted_temprature = temprature_in_celsius + 273.15
            print(f"\n{temprature_in_celsius} C equals to {converted_temprature:.2f} K. 🌡️\n")
        elif conversion == "f":
            converted_temprature = (temprature_in_celsius * (9 / 5)) + 32
            print(f"\n{temprature_in_celsius} C equals to {converted_temprature:.2f} F. 🌡️\n")
        else:
            print("\nNot possible unit.❌\n")
        
        again = input("Do you want to convert temprature again? ")
        if again != "y":
            print("\nThanks! for using temprature converter. ❤️")
            break


if __name__ == "__main__":
    main()