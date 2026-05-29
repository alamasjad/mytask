import random 
class Bank:
    Bank_Name="Asjad's Bank"
    accounts={}
    def __init__(self,name:str,phone_no:int):
        self.name=str(name)
        self.phone_no=int(phone_no)
        self.account_number=random.choice(["A","B","C","D"])+str(random.randint(100001,999999))
        if self.account_number in self.accounts:
            self.account_number=random.choice(["Z","E","L","K"])+str(random.randint(100001,999999))
        self.balance=0
        self.accounts[self.account_number]=self


    @classmethod
    def display_names(cls):
        print(f"Account Holders in {cls.Bank_Name} are:")
        for key in cls.accounts:
            c_obj=cls.accounts[key]
            print(f"{c_obj.name}:{key}")
        print()

    def deposit(self,amnt):
        print(self.name+"'s","Account:")
        if amnt<0:
            print('Invalid Amount to deposit')

        else:
            self.balance+=amnt
            print("Amount Deposited")
        print()


    def withdraw(self,amnt):
        print(self.name+"'s","Account:")
        if amnt>self.balance:
            print("Insufficient Balance")
        elif amnt<0:
            print("Invalid Amount to withdraw")
        else:
            self.balance-=amnt
            print("Amount Withdrawed")
        print()


    def show_balance(self):
        print(f"{self.name} Total Balance is {self.balance}")
        print()


c1=Bank('Peter',8409475707)
c2=Bank('Banner',9840198411)
Bank.display_names()
c1.deposit(20000)
c1.show_balance()
c1.withdraw(10000)
c1.show_balance()
c1.withdraw(12000)
c1.deposit(-20000)























"""
def open_account(x):
    while x:
        name=input("Enter Your Name:")
        phone_no=input("Enter Your Number:")
        customer=Bank(name,phone_no)
        print(f"Account Created For {name} ,Your Account Number is:{customer.account_number}")
        x=int(input("Continue-Press '1' Else Press 0:"))
        if x==0:
            print("ThankYou")
            return customer
        if x!=1 and x!=0:
            print("Wrong input")
            return customer
        
open_account(1)
"""
