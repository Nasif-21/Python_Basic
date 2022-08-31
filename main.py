class Parents:
    def __init__(self,papa,mamma):
        self.firstname=papa
        self.middlename=mamma

    def printname(self):
            print(self.firstname, self.middlename)
class Child(Parents):
    def __init__(self,papa,mamma,baby):
        super().__init__(papa,mamma)
        self.lastname=baby
    def Welcome(self):
        print("Welcome Dear", self.firstname,self.middlename,self.lastname)

a=Child(input("Enter First name"),input("Enter Middle name"),input("Enter Last Name"))
a.Welcome()

