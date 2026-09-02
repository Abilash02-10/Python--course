from abc import ABC,abstractmethod
class Phonepay(ABC):
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("you can enter amount")

    def pin(self):
        print("enter your pin")

    @abstractmethod    
    def transactions(self):
        pass
class SBI(Phonepay):
    def transactions(self):
        print("payment using SBI")
class HDFC(Phonepay):
    def transactions(self):
        print("payment using HDFC")
class UNION(Phonepay):
    def transactions(self):
        print("payment using union bank")
abilash = SBI()
abilash.senderinfo()
abilash.amount()
abilash.pin()
abilash.transactions()
jagadeeh = HDFC()
jagadeeh.senderinfo()
jagadeeh.amount()
jagadeeh.pin()
jagadeeh.transactions()
xyz = UNION()
xyz.senderinfo()
xyz.amount()
xyz.pin()
xyz.transactions()


        