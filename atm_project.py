username="Honey"
PIN="1234"

print("~~~~~ Welcome ~~~~~")
print("    ")


user_name=input("Enter your Name:")
user_pin=input("Enter your PIN:")

if user_name==username and user_pin==PIN:
    print('''
        1.Deposit Amount
        2.Withdrawl Amount
        3.Mini Statement
        4.Exit
        ''')
    
    amount=20000
while True:
    option=int(input("Enter your option:"))
    if option==1:
        dep=int(input("Enter your amount:"))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount:"))
        amount-=withd
        print("Total amount:",amount)
    elif option==3:
        print("Username:",username)
        print("Total amount:",amount)
    elif option==4:
        print("~~~~ Thanks for visiting ~~~~")
        exit()
        
        
else:
    print("Please enter correct details")
