"""
Temperature Converter – Bad Version

This code has issues that violate three key principles:

1. KISS (Keep It Simple, Stupid)
2. DRY (Don't Repeat Yourself)
3. YAGNI (You Aren't Going to Need It)

"""

def celsius_to_fahrenheit(celsius_str):
    """
    Converts Celsius to Fahrenheit.

    :param: celsius_str (str): Temperature in Celsius as a string.
    :return: float representing temperature in Fahrenheit.
    """
    # KISS Violation: Parsing and validating input again here, instead of doing it once in main.
    # This makes the code more complex than necessary, reducing clarity.
    try:
        if "." in celsius_str:
            celsius = float(celsius_str)
        else:
            celsius = int(celsius_str)
    except ValueError:
        # Instead of handling this simply, an exception is raised in hopes
        # that main to catches it. Another layer of complexity.
        raise ValueError("Invalid Celsius input.")

    # DRY Violation: The conversion formula is done inline here.
    # similar logic in fahrenheit_to_celsius,
    # rather than using a shared helper function.
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit_str):
    """
    Converts Fahrenheit to Celsius.

    :param: fahrenheit_str (str): Temperature in Fahrenheit as a string.
    :return: float representing temperature in Celsius.
    """
    # KISS Violation again: Repeating input parsing and validation
    # that could be centralized in main or a separate function.
    try:
        if "." in fahrenheit_str:
            fahrenheit = float(fahrenheit_str)
        else:
            fahrenheit = int(fahrenheit_str)
    except ValueError:
        raise ValueError("Invalid Fahrenheit input.")

    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius_str):
    """
    Converts Celsius to Kelvin.

    :param: celsius_str (str): Temperature in Celsius as a string.
    :return: float representing temperature in Kelvin.
    """
    # YAGNI Violation: The converter is for Fahrenheit <-> Celsius no need for Kelvin,
    # but it is included anyway "just in case it is implemented in the future."
    # This adds unneeded complexity and code to maintain.
    try:
        if "." in celsius_str:
            celsius = float(celsius_str)
        else:
            celsius = int(celsius_str)
    except ValueError:
        raise ValueError("Invalid Celsius input for Kelvin conversion.")

    return celsius + 273.15

def main():
    """
    Main function to run the temperature converter.
    Prompts the user for input and displays results.
    """
    while True:
        # KISS Violation: The menu is straightforward, but
        # repeated input parsing logic within each function
        # instead of handling it once here.
        print("\nWelcome to the Fahrenheit/Celsius Temperature Converter.")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, 3, 4): "))
        except ValueError:
            print("Invalid input. Please enter the number 1, 2, 3, or 4.")
            continue

        if choice == 1:
            # DRY Violation: Going to re-parse the temperature
            # in celsius_to_fahrenheit, duplicating logic.
            celsius_str = input("Enter temperature in Celsius: ")
            try:
                fahrenheit = celsius_to_fahrenheit(celsius_str)
                print(f"{float(celsius_str):.2f}°C is {fahrenheit:.2f}°F.")
            except ValueError as e:
                print(e)

        elif choice == 2:
            # Same pattern repeated for Fahrenheit to Celsius,
            # showing how the code is not DRY.
            fahrenheit_str = input("Enter temperature in Fahrenheit: ")
            try:
                celsius = fahrenheit_to_celsius(fahrenheit_str)
                print(f"{float(fahrenheit_str):.2f}°F is {celsius:.2f}°C.")
            except ValueError as e:
                print(e)

        elif choice == 3:
            # YAGNI Violation: No Need for option. "Future Capability"
            print("The Celsius to Kelvin feature is not yet implemented.")

        elif choice == 4:
            print("Exiting the Temperature Converter.")
            break

        else:
            # KISS Violation: Check for invalid input here,
            # but also in multiple other places, complicating the logic.
            print("Invalid number. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
