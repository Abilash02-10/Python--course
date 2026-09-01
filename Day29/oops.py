'''class Flipkart:
    products = {'shirts':1000,'Tshirt':700,'pants':1000}
    discount = 20
    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello { self.name}, welcome to the flipkart")

dheeraj = Flipkart( )
dheeraj.userinfo('dheeraj',9392824939,'Hyd')
karthik = Flipkart()
karthik.userinfo('karthik',345678,'hyd')
Abhilash = Flipkart()
Abhilash.userinfo('Abhilash',2345678,'hyd')'''



''''class Flipkart:
    products = {'shirts':1000,'Tshirt':700,'pants':1000}
    discount = 20

    @classmethod
    def display(cls):
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello { self.name}, welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount} discount is going on,grab the products")

dheeraj = Flipkart( )
dheeraj.userinfo('dheeraj',9392824939,'Hyd')
dheeraj.displaydiscount()
karthik = Flipkart()
karthik.userinfo('karthik',345678,'hyd')
karthik.displaydiscount()
Abhilash = Flipkart()
Abhilash.userinfo('Abhilash',2345678,'hyd')
Abhilash.displaydiscount()
'''
# using object we can access class method,instance method, static method, classattribute, instance attribute
# using class we can access class method, static method,class attribute
'''class Flipkart:
    products = {'shirts':1000,'Tshirt':700,'pants':1000}
    discount = 20

    @classmethod
    def display(cls):
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello { self.name}, welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount} discount is going on,grab the products")

dheeraj = Flipkart( )
dheeraj.userinfo('dheeraj',9392824939,'Hyd')
dheeraj.displaydiscount()
karthik = Flipkart()
karthik.userinfo('karthik',345678,'hyd')
karthik.displaydiscount()
Abhilash = Flipkart()
Abhilash.userinfo('Abhilash',2345678,'hyd')
Abhilash.displaydiscount()
dheeraj = Flipkart( )
dheeraj.userinfo('dheeraj',345678,'Hyd')
dheeraj.displaydiscount()
dheeraj.display()
print(dheeraj.products())
print(dheeraj.name)

Flipkart.displaydiscount()
Flipkart.display()
Flipkart.products
'''


