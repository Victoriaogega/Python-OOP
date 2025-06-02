import datetime

class Transaction:
    def __init__(self,date,narration,transaction_type,amount):
        self.date= date
        self.narration = narration
        self.transaction_type = transaction_type
        self.amount = amount

    def get_details (self):
        return {
            'date':self.date,
            'narration':self.narration,
            'transaction_type':self.transaction_type,
            'amount':self.amount
        }   

class Account:
    def __init__(self,name,account_no):
        self.name = name
        self._account_no = account_no
        self.transaction = []
        self._balance = 0
        self.loan_balance = 0
        self.loan = 0
        self.new_loan_amount=0

    def deposit(self,amount,narration ='deposit'):
        if self.is_frozen:
            print("Account is frozen,you cannot deposit") 
        if amount < 0:
            print ("Input a positive number")
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,narration,'deposit',amount)
            self.transaction.append(new_transaction)
            self._balance += amount
            print(f"Deposited {amount} to {self.name} at {new_transaction.date} account and your balance is {self.balance}")                  

    def withdraw(self,amount,narration='withdraw'):
        if self.is_frozen:
            print("Account is frozen,you cannot withdraw") 
        if amount < 0:
            print("Input a positive number")
        if amount > self.balance:
            print ("Insufficient balance")
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,amount,narration,'withdraw')
            self.transaction.append(new_transaction)  
            self._balance -=amount
            print(f"Dear {self.name} you have withdrawed {amount} and your balance is {self.balance} at {new_transaction.date}")    

    def transfering(self,amount,recepient,narration = 'narration'):
        if self.is_frozen:
            print("Account is frozen, you cantinue with your transaction.") 
        if amount < 0: 
            print("Please input a positive value")
        if amount > self._balance:
            print("Insufficient funds") 
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,amount,narration,'transfering')
            self.transaction.append(new_transaction)
            self._balance -=amount
            print(f"you have transfered {amount} to {recepient} and your balance is {self.balance}")    


    def  get_balance(self):
        remaining balance = sum(transaction.get_details()['amount']for transaction in self.transaction )
        balance = sum(transaction.get_details()['amount']) for transaction in self.transaction
        self._balance = balance
        return self.get_balance
      
   

    def get_total_deposits(self):
        total_amount = sum(
            transaction.get_details()['amount']
            for transaction in self.transaction
            if transaction.get_details()['transaction_type'] in ['deposit','Initial deposit']
            and transaction.get_details()['amount']
        )
        return total_amount                          


    def get_loan(self,amount,narration = 'loan'): 
            if self.is_frozen:
                print("Account is frozen") 
            if amount <0 :
                print("Enter a positive value")
            if self.loan_balance >0:
                return "You have an outstanding debt." 
            if amount > self.get_total_deposits():
                print("The amount is past your loan limit,please try a lower amount")    
            else:
                current_date = datetime.datetime.now()
                new_transaction = Transaction(current_date,amount,narration,'loan')
                self.loan_balance += amount
                self.balance +=amount
                self.transaction.append(new_transaction)
                self.loan = amount
                return f"You have received a loan of {amount} at {new_transaction.date} and your new balance is {self.balance}. Your loan balance is {self.loan}"       

    def interest_rate(self,rate,time_in_years):
        loan_amount = self.loan *rate*time_in_years
        self.new_loan_amount += self.loan_balance + loan_amount
        return self.new_loan_amount
       
             
    def repay_loan(self,amount,narration = 'repay_loan'):
        if amount <0 :
            print("Enter a positive value")
        if amount <= self.loan_balance:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,amount,narration,'repay_loan')
            self.loan_balance = self.new_loan_amount -amount
            return f"You have repayed your loan of {self.loan} with {amount} at {new_transaction.date} and your balance is {self.loan_balance}"   
        else:
            current_date = datetime.datetime.now()
            new_transaction = Transaction(current_date,amount,narration,'repay_loan')
            extra_amount = amount - self.loan_balance
            self._balance += extra_amount
            return f"You have repayed your loan of {self.loan} with {amount} at {new_transaction.date} and your balance is {self.loan_balance}"  

    def freeze_account(self): 
        self_.is_frozen = true
        return "Account has been frozen"  

    def unfreeze_account(self): 
        self_.is_frozen = false
        return "Account has been unfrozen" 

    def close_account(self,account):
        deposits = [
            transaction for transaction in self.transaction
            if transaction.get_details()['transaction_type']
        ]
        if not deposits:
            last_deposit = max(transaction.get_details()['date'] for transaction in deposits )
            if last_deposit < datetime.now() - timedelta(days = 90):
                account.close_account()
                return "Account closed"

    def account_statement(self):
        if not self.transactions:
            return "No transactions found."
            statement = f"Account Statement for {self.name}"
        for transaction in self.transactions:
            statement += f"Date: {transaction.date}, Narration: {transaction.narration}, Type: {transaction.transaction_type}, Amount: {transaction.amount}"
            return statement            






                            

                        