import sys

class bank:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.balance=0

    def sign_up(self):
        self.name=input("ENTER YOUR NAME : ")
        self.age=int(input("ENTER YOUR AGE : "))
        self.gender=input("ENTER YOUR GENDER : ")
        print("successfully signed up")

    def show_details(self):
        print("personal details : ")
        print("name ", self.name)
        print("age ", self.age)
        print("gender ", self.gender)
        print("your balance is : ",self.balance)


    def deposite(self,amount):
         self.balance=self.balance+amount
         print("the money is added successfully your balance now is : ",self.balance)

    def wihdraw(self,amount):
         if amount>self.balance:
             print("insufficient fund your available balance is: ",self.balance)
         else:
             self.balance -= amount
             print("account balance has been updated your current balance is:",self.balance)
    def view_balance(self):
        print("your current balance is: ",self.balance)

class user:
    def added_amount(self):
        print("enter the amount you want to add : ")
        self.amount=int(input())
        return self.amount

    def withdraw_amount(self):
        print("enter the amount you want to withdraw : ")
        self.amount=int(input())
        return self.amount

def main():
    user1=user()
    bank1=bank("bassant",20,"female")
    done = True
    while done == True:
        print(""" ======BANK MANAGEMENT SYSTEM======
                          1. sign up
                          2. deposite money
                          3. withdraw
                          4. view balance
                          5. view user details
                          6. exit
                          """)
        choice=int(input("enter your choice: "))
        if choice ==1:
            bank1.sign_up()
        elif choice==2:
         bank1.deposite(user1.added_amount())
        elif choice==3:
         bank1.wihdraw(user1.withdraw_amount())
        elif choice==4:
         bank1.view_balance()
        elif choice==5:
            bank1.show_details()
        elif choice==6:
            sys.exit()
main()
