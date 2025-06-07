# Prompt the user for temperature in Celsius and return it in Kelvin

def main() -> None:
    print("\n===============Temprature Converter===============")

    # Ask the user for temperature in celsius and also handles ValueError (as many times as user wants)
    while True:
        temperature_in_celsius = ask_temperature()
        convert_temprature(temperature_in_celsius)

        again = input("Do you want to convert temperature again (y/n)? ")
        if again not in ["y", "yes"]:
            print("\nThanks! for using temperature converter. ❤️")
            break

    
def ask_temperature() -> float:
    """
    Ask the user for temperature in celsius and also handles ValueError (as many times as user wants)
    """
    while True:
        try:
            temperature_in_celsius = float(input("\nEnter temperature in Celsius: "))
        except ValueError:
            print("\n❌-----It is not a valid temperature.-----❌")
        else:
            return temperature_in_celsius


def convert_temprature(temperature) -> None:
    """
    This function takes temperature as an argument and then ask the user for unit in which it is going 
    to convert it.
    """
    while True:
        conversion = input("\nDo you want to convert it into K or F? ").lower()

        if conversion == "k":
            converted_temprature = temperature + 273.15
            print(f"\n{temperature}°C equals to {converted_temprature:.2f} K. 🌡️\n")
            break
        elif conversion == "f":
            converted_temprature = (temperature * (9 / 5)) + 32
            print(f"\n{temperature}°C equals to {converted_temprature:.2f} F. 🌡️\n")
            break
        else:
            print("\nPlease enter K for Kelving and F for Fahrenhiet❌\n")


if __name__ == "__main__":
    main()