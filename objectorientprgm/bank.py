from datetime import*
class bank:
    bank_name="sib"

    def create_account(self,accno,c_name,phno,bal):
        self.accno=accno
        self.c_name=c_name
        self.phno=phno
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print(bank.bank_name,"a/c noxxx",self.accno,"credited with",amount,"on",datetime.today(),"your availble bal",self.bal)

    def withdraw(self,amount):
        if amount>self.bal:
          print("transcation is falied with error")
        else:
            self.bal-=amount
            print("a/c noxxx",self.accno,"debited with",amount,"your availble bal",self.bal)
    def bal_enq(self):
        print("available bal",self.bal)

obj=bank()
obj.create_account(1234,"neethu",9812345678,2000)
obj.withdraw(500)