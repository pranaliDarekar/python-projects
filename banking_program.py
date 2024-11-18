# Banking Program

def show_balance(balance):
    print(f"Your Balance :${balance:.2f}")

def deposit():
    
    amount = float(input("Enter the amount to be deposited: "))

    if amount < 0:
        print("Enter a amount greater than zero")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount < balance:
        print("******************************")
        print("Insufficient Funds!")
        print("******************************")
        return 0
    
    elif amount < 0:
        print("******************************")
        print("Enter a amount greater than 0")
        print("******************************")
        return 0
    
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("Banking Program")
        print("************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("************************")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("************************")
            print("Invalid choice")
            print("************************")

    print("*******************************")
    print("Thank you!, Have a nice day!!")
    print("*******************************")
    
main()       