"""
Fahrenheit - Celsius Temperature Converter made with good practices

A simple temperature converter following:
KISS (Keep It Simple, Stupid): Straightforward and easy to read
DRY (Don't Repeat Yourself): Conversion logic is encapsulated for reusable functions
YAGNI: (You Aren't Going to Need It): Only necessary functionality

Program include three main functions:
celsius_to_fahrenheit: Converts Celsius to Fahrenheit
fahrenheit_to_celsius: Converts Fahrenheit to Celsius
main: Manages user interaction and displays resluts
"""

def celsius_to_fahrenheit(celsius):
    """
    Concerts Celsius to Fahrenheit.

    :param: celsius (float): Temp in Celsius.
    :return: float: Temp in Fahrenheit.
    """

    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Concerts Fahrenheit to Celsius.

    :param: fahrenheit (float): Temp in Fahrenheit.
    :return: Temperature in Celsius.
    """
    return(fahrenheit - 32) * 5/9

def main():
    """
    Main function to run the temperature converter.
    Prompts the user for input and displays results.
    """
    while True:
        print("Welcome to the Fahrenheit/Celsius Temperature Converter.")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, 3): "))
        except ValueError:
            print("Invalid input. Please enter the number 1, 2, or 3.")
            return

        if choice == 1:
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 2:
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 3:
            print("Exiting the Temperature Converter.")
            break

        else:
            print("Invalid Number. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
