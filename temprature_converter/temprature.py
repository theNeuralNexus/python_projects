# Prompt the user for temprature in Celsius and return it in Kelvin

def main() -> None:
    print("\n===============Temprature Converter===============")

    # Ask the user for temprature in celsius and also handles ValueError (as many times as user wants)
    while True:
        try:
            temprature_in_celsius = float(input("\nEnter temprature in Celsius: "))
        except ValueError:
            print("\n❌-----It is not a valid temprature.-----❌")
            continue
        
        convert_temprature(temprature_in_celsius)

        again = input("Do you want to convert temprature again? ")
        if again != "y":
            print("\nThanks! for using temprature converter. ❤️")
            break


def convert_temprature(temprature):
    """
    This function takes temprature as an argument and then ask the user for unit in which it is going 
    to convert it.
    """
    conversion = input("\nDo you want to convert it into K or F? ").lower()

    if conversion == "k":
        converted_temprature = temprature + 273.15
        print(f"\n{temprature} C equals to {converted_temprature:.2f} K. 🌡️\n")
    elif conversion == "f":
        converted_temprature = (temprature * (9 / 5)) + 32
        print(f"\n{temprature} C equals to {converted_temprature:.2f} F. 🌡️\n")
    else:
        print("\nNot possible unit.❌\n")


if __name__ == "__main__":
    main()