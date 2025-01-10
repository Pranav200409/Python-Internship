''' Create a Python program that converts temperatures between Celsius and Fahrenheit.
Prompt the user to enter a temperature value and the unit of measurement, and then display the
converted temperature.'''


def fahrenheit_to_celcius(temp):
    return ( temp - 32 )* 5/9

def celcius_to_fahrenheit(temp):
    return (temp *9/5) + 32
print("\t\t\t Temperature Conversion Program")

while True :
    print("Enter C for celsius or F for Fahrenheit.")

    temp = float(input("Enter a temperature to be converted :"))
    unit = input("Enter the unit for measurement (C\F):").strip().upper()

    if unit == 'F':
        converted_temp = fahrenheit_to_celcius(temp)
        print(f"{temp}F is equal to {converted_temp}")

    elif unit == 'C':
        converted_temp = celcius_to_fahrenheit(temp)
        print(f"{temp}C is equal to {converted_temp}")
    
    else:
        print("Enter a valid unit ")

    continue_choice = input("Want to convert another temperature ? (yes to CONTINUE or no to EXIT):").strip().lower()
    if continue_choice != 'yes':
        print("Exiting ....... thaqnk you ")
        break