# Python OOP concepts 
class Accounts:
    def __init__(self, account_no, account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass

acc1 = Accounts("123", "abab")
print(acc1.account_no, acc1.__account_pass)
