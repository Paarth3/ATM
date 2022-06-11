class ATM:
    def __init__(self):
        self.cardNumber = int(input("Please Enter Your Card Number: "))
        self.pinNumber = int(input("Please Enter Your Pin Number: "))
    def BalanceEnquiry(self):
        print("---Your card Number is",self.cardNumber)
        print("---Your Account Balance is ₹50000")
    def CashWithdrawl(self):
        cashToBeRemoved = int(input("Enter the amount to be withdrawed: "))
        if(cashToBeRemoved>50000):
            print("---Ohh! Amount greater than bank Balance :(")
        else:
            newBalance = 50000 - cashToBeRemoved
            print("---Cash Withdrawed")
            print("---Available Balance:", newBalance)

Atm = ATM()
Atm.BalanceEnquiry()
Atm.CashWithdrawl()