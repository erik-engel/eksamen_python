class Bank:
    def __init__(self):
        self.__accounts = []
    
    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, account):
        if type(account) == list:
            for i in account:
                self.__has_account(i)
                self.__accounts.append(i)
        else:
            self.__has_account(account)
            self.__accounts.append(account)
        
    def __has_account(self, acc):
        for i in self.__accounts:
            if acc.cust.name == i.cust.name:
                raise ValueError('Customer already has an account')
        return False



class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust
    
    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, no):
        self.__no = no

    @property
    def cust(self):
        return self.__cust

    @cust.setter
    def cust(self, cust):
        self.__cust = cust

    def __repr__(self):
        return str(self.__dict__)

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("customer must be at least 18 years old")
        else:
            self.__age = age

    def __repr__(self):
        return str(self.__dict__)