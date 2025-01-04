def check_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("Unvalid amount (amount vlaue has to be greater than 0)")
        return 0
    else:
        print ("Amount is deposited successfully")
        return amount

def withdraw(balance):

    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("You don't have sufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        print("Amount is withdrawn successfully")
        return amount
    
def thx_msg():
    print("=====================")
    print("Thank you for using our services!")
    print("=====================")

def continue_prompt():
    decision = input("Do you want to continue ? \nEnter Y if you want to contuine, otherwise enter N: ").upper()
    if decision=='Y':
        return True
    elif decision=='N':
        thx_msg()
        return False
    else:
        print("Invalid input")
    
  
#MAIN
balance = 0
is_running = True

while is_running:
    print("=====================")
    print("   Banking System   ")
    print("=====================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. check Balance")
    print("4. Exit")
    print("=====================")
    choice = input("Enter your choice, please: ").strip()


    if choice == '1':
        balance += deposit()
        is_running = continue_prompt()
        
    elif choice == '2':
        balance -= withdraw(balance)
        is_running = continue_prompt()
        
    elif choice == '3':
        check_balance(balance)
        is_running = continue_prompt()
        
    elif choice == '4':
        thx_msg()
        is_running = False
    else:
        print("Unvalid choice, please enter a value between 1 and 4") 
    




