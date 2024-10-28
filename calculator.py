# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter Principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero!!")

while rate <= 0:
    rate = float(input("Enter Interest Rate: "))
    if rate <= 0:
        print("Interest Rate can't be less than or equal to zero!!")

while time <= 0:
    time = int(input("Enter Time in year/s: "))
    if time <= 0:
        print("Time can't be less than or equal to zero!!")

total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} year/s: ${total:.1f}")