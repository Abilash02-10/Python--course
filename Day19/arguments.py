# positional arguments
'''def display(name,email,password):
    print(f'name: {name}')
    print(f'email:{email}')
    print(f'password:{password}')

display('xyz','xyz@gmail.com','xyz@123')
display('acd@gmail.com','xgdhv','ohdgfyf')'''

#key word arguments

cd def display(name,email,password):
    print(f'name: {name}')
    print(f'email:{email}')
    print(f'password:{password}')

display(name = 'xyz',email='xyz@gmail.com',password='xyz@123')
display(password= 'acd@gmail.com',email='xgdhv',name ='ohdgfyf')

#default arguments

'''def display(name,email='gmail.com',password=' '):
    print(f'name: {name}')
    print(f'email:{email}')
    print(f'password:{password}')

display('xyz','xyz@gmail.com',)
display('acd@gmail.com','xgdhv',)
display('xyz') '''


# vairable arguments
'''def display(*name):
    print(name)

display('sajid')
display('sajid','abdul')
display('sajid','abdul','dheeraj')'''

#
def display(**products):
    print(products)

display(bag = 5000)
display(bag = 5000, book = 30)
display(bag = 5000, book = 40,bottle = 200)
