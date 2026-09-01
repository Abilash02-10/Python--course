
#acessing inside class and outside class in encapsulation
'''class Instagram :
    def __init__(self,username,password):
        self.username = username #public
        self.__password = password #private
        self._posts                #protected
    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._posts

    def display(self):
        print(self.username,self.__password,self._posts)

abilash = Instagram('abilash','abilash@123')
abilash.display()
print(abilash.username)
print(abilash.getpassword())
print(abilash.accesspost)
'''


# updating password and posts and username
'''class Instagram :
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts
    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword



    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        return self._post.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)

abilash = Instagram('abilash','abilash@123')
abilash.display()
print(abilash.username)
print(abilash.getpassword())
print(abilash.accesspost)
abilash.username = "xcvbn"
abilash.setpassword("dfghj@123")
abilash.accesspost = "sdfgh.png"
abilash.accesspost = "sdfg.png"
abilash.accesspost = "sfg.png"

print(abilash.username)
print(abilash.getpassword())
print(abilash.accesspost)
'''

class user_registration:
    def __init__(self,name,email,phone,password):
        self.name = name
        self.email =email
        self.phone = phone
        self.password=password

    def registration(self):
        if self.name ==" ":
            print("registration Failed: nameis required")
        elif self.email ==" ":
            print("registration Failed: email is required")
        elif self.phone ==" ":
            print("registration failed: mobile number is required")
        elif self.password == " ":
            print("registration Failed: password is required")

user1 = user_registration('abilash','abilash@gmail.com','939283929','1234')
user1.registration( )

user2 = user_registration('abilash', '4356789','','')
user2.registration()



