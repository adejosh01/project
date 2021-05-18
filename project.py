class Bank:
    def __init__(self, Account_name, Account_number, Amount):
        self.AN = Account_name
        self.ANU = Account_number
        self.A = Amount


    def deposit(self):
        print("Good deposit")

    def withdraw(self):
        print("Good withdraw")
    
    def loan(self):
        print("Comfirm")

class First_Bank(Bank):
    def __init__(self, Account_name, Account_number, Amount):
        super().__init__(Account_name, Account_number, Amount)
    
    def loan(self):
        print("Still manageable")

    def ATM(self):
        return True

class Microfinance(Bank):
    def __init__(self, Account_name, Account_number, Amount):
        super().__init__(Account_name, Account_number, Amount)

    def loan1(self):
        print("perfect place")

    def saving(self):
        return False

class Big_bank(First_Bank, Microfinance):
    def __init__(self, Account_name, Account_number, Amount):
        super().__init__(Account_name, Account_number, Amount)

user1 = First_Bank('Adeloba Joshua', '12345678', '#20000')  
print("ACCOUNT NAME: " + user1.AN, "ACCOUNT NUMBER: " + user1.ANU, "AMOUNT: " + user1.A)
print("DEPOSIT: ")
print(user1.deposit())
print("LOAN: ")
print(user1.loan())
print("WITHDRAW: ")
print(user1.withdraw())
print("ATM: ")
print(user1.ATM())

user2 = Microfinance("Adeloba Grace", "12346623", "#123000" )
print("ACCOUNT NAME: " + user2.AN, "ACCOUNT NUMBER: " + user2.ANU, "AMOUNT: " + user2.A)
print("DEPOSIT: ")
print(user2.deposit())
print("LOAN1: ")
print(user2.loan1())
print("WITHDRAW: ")
print(user2.withdraw())
print("SAVING: ")
print(user2.saving())

user3 = Big_bank('Oyinlola caleb', "1234567890987", "#30000 ")
print("ACCOUNT NAME: " + user3.AN, "ACCOUNT NUMBER: " + user3.ANU, "AMOUNT: " + user3.A)
print("DEPOSIT: ")
print(user3.deposit())
print("LOAN: ")
user3.loan1()
print("WITHDRAW: ")
print(user3.withdraw())
print("ATM: ")
print(user3.ATM())
print("Saving: ")
print(user3.saving())
