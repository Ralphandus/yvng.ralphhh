value = float(input("Enter a value: "))
temp = input("Enter the temperature unit C/F")

if temp == 'C' or temp == 'c':
    converted = (value * 9/5) + 32
    print(f"{value}°C is {converted}°F")
elif temp == 'F' or temp == 'f':
    converted = (value - 32) * 5/9
    print(f"{value}°F is {converted}°C")
else:
    print("Invalid temperature input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")