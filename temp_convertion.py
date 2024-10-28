# Temperature Convertion

unit = input("Is this temperature in Celsius or Fahrenheit? (C or F):  ")
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "°F"
    print(f"The temperature in Fahrenheit is: {temp} {unit}")
elif unit == "F":
    temp = (temp-32) * 5/9
    unit = "°C"
    print(f"The temperature in Celsius is: {round(temp,1)} {unit}")
else:
    print(f"Invalid {unit}")