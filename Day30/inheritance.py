
#1. A -> B single heritance
class whatsupversion1:
    
    def __init__(self,name):
        self.name = name
        print(f"welcome to the whatsapp - v1 { self.name}!")

    def messaging(self):
        print("you can send messages")

class Whatsupversion2(whatsupversion1):
    def __init__(self, name):
        self.name = name
        print(f"welcome to the whatsupapp - v2 { self.name}!")


    def calls(self):
        print("you can make audio and video calls")

abilash =whatsupversion1('abilash')
abilash.messaging()

harish = Whatsupversion2('harish')
harish.messaging( )
harish.calls()

        
