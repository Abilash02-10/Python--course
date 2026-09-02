
#single inheritance
'''class whatsapp1:
    def messaging(self):
        print("you can message")
class whatsapp2(whatsapp1):
    def calls(self):
        print("you can make calls")
a = whatsapp1()
a.messaging()
b = whatsapp2()
b.calls()
b.messaging()'''

#multi level inheritance
'''class whatsapp1:
    def messaging(self):
        print("you can message")
class whatsapp2(whatsapp1):
    def calls(self):
        print("you can make calls")

class whatsapp3(whatsapp2):
    def status(self):
        print("you can add the status for 24 hours")
a = whatsapp1()
a.messaging()
b = whatsapp2()
b.calls()
b.messaging()
c = whatsapp3( )
c.status( )
c.calls()
c.messaging( )

#Multipleinheritance

class whatsapp1:
    def messaging(self):
        print("you can message")
class whatsapp2():
    def calls(self):
        print("you can make calls")

class whatsapp3(whatsapp1,whatsapp2): #multiple inheritance
    def status(self):
        print("you can add the status for 24 hours")
a = whatsapp1()
a.messaging()
b = whatsapp2()
b.calls()
c = whatsapp3()
c.status()
c.calls()
c.messaging( )
'''

#Hierarical Inheritance multiple childs

'''class whatsapp1:
    def messaging(self):
        print("you can message")
class whatsapp2(whatsapp1):
    def calls(self):
        print("you can make calls")

class whatsapp3(whatsapp1): #multiple inheritance
    def status(self):
        print("you can add the status for 24 hours")
a = whatsapp1()
a.messaging()
b = whatsapp2()
b.calls()
b.messaging()
c = whatsapp3()
c.status()
c.messaging( )

'''

# Hybrid inheritance

'''class whatsapp1:
    def messaging(self):
        print("you can message")
class whatsapp2():
    def calls(self):
        print("you can make calls")

class whatsapp3(whatsapp1,whatsapp2): #multiple inheritance
    def status(self):
        print("you can add the status for 24 hours")

class whatsapp4(whatsapp3):     # multilevel inheritance
    def extramessages(self):
        print("here wecansend emojis ")
a = whatsapp1()
a.messaging()
b = whatsapp2()
b.calls()
c = whatsapp3()
c.status()
c.messaging( )
c.calls( )
d = whatsapp4( )
d.extramessages()
d.status( )
d.calls( )
d.messaging()
'''

# using super method when we have the same methods names
'''class whatsv1:
    def status(self):
         print("you can add images and videos")
class whatsv2(whatsv1):
    def status(self):
        super().status()
        print("you can add music and stickers")
class whatsv3(whatsv2):
    def status(self):
        super().status( )
        print("you can like and react")
a = whatsv1()
a.status()
b = whatsv2()
b.status( )
b.status( )
c =whatsv3( )
c.status( )
'''

class whatsv1:
    def status(self):
         print("you can add images and videos")
class whatsv2:
    def status(self):

        print("you can add music and stickers")
class whatsv3(whatsv1,whatsv2):
    def status(self):
        whatsv1().status(self)
        whatsv2( ).status(self)
        print("you can like and react")
a =whatsv1( )
a.status()
    

        
    


