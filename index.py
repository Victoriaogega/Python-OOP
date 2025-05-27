from datetime import datetime, timedelta
from statistics import mean

class Account:
    def __init__(self,name,balance = 0.0,limit= 50000):
        self.name = name
        self.deposit = []
        self.withdrawals = []
        self.balance = balance
        self.loan_intrest_rate = 0.05
        self.loans = loans
        self.transfers = transfers
       

    def deposits(self,amount):
        if amount > 0:
            self.transactions.append(amount)
            self.balance += amount
            return f"You have deposited {amount} to your account successfully and your balance is {self.show_balance()}"
            

    def show_balance(self):
        return f"Your balance is {self.balance} shillings."
 

    def transfer(self,amount):
        if amount > self.balance:
            print("Insufficient balance. Your current balance is {self.balance} KSH.")
        else:
            self.transactions.append(amount) 
            self.balance -= amount 
            return f"You have successfully transfered {amount} shillings and your balance is {self.balance} KSH"               

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance.Your current balance is {self.balance}KSH.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")  
        else:
            self.transactions.append(amount)
            self.balance -= amount
            return f"You have successfully withdrawed {amount} shillings from your account and your balance is {self.balance} KSH."
                
def get_loan(self, amount):
        if amount > 0:
            pass
        else:
            return "You can't take a negative loan."
        if amount > self.limit:
            return "Please try a smaller amount."  
        else:
            self.loans.append(amount)

                  

    def repay_loan(self, amount):
        if amount <=0:
            return "Loan repayment failed, amount has to be positive."
        total_outstanding_debt = sum(loans["amount"]-loans["repaid_amount"]for loans in self.loans if not loan.get ("Fully re-paid", false))
        if total_outstanding_debt == 0:
            return "No outstanding loans to repay"   
        if amount >  total_outstanding_debt:
                return f"Repayment amount {amount} esxceeds total outstanding loan debt of {total_outstanding_debt}"
                amount_to_repay = total_outstanding_debt
        else: amount_to_repay = amount

        if self.balance < amount_to_repay:
                 print(f"Loan repayment failed: Insufficient funds in account to repay ${amount_to_repay}. Current balance: ${self.balance}")
            return


                 

    def get_statement(self):
        statement = f"Account statement for {self.name} Deposit: {self.depositt}withdrawals: {self.withdrawals}transfers: {self.transfers} Balance: {self.get_balance()}"
        return statement

    def get_loan_statement(self):
        statement = f"Loan statement for {self.name} Loans taken: {self.loans} Loan repayments: {self.loan_repaying}Unpaid loan: {sum(self.loans) - sum(self.loan_repaying)}"
        return statement

def freeze_account(self):
        self.freeze=true
        return "Account frozen"

def unfreeze_account(self):
        self.freeze=false
        return "Account unfrozen"
def view_account_details(self):
    return (f"{self.name}", your account balance is {self.balance()})        


def change_owner(self,new_owner):
        self.new_owner=new_owner
        return f"New account holder is {new_owner}"