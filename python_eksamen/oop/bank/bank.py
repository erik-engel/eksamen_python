class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust


