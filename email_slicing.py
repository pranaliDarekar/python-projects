# Email slicing program using index method

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index +1:]

print(f"Your username is {username} and domian name is {domain}")