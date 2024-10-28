# Python weight converter

weight = float(input("What is your weight? : "))
unit = input("Kilogram or Pound? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight,1)} {unit}")

elif unit == "L":
    weight = weight/2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print(f"Inavlid {unit}")

