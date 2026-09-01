# functions
'''def display(name,email,password):
    print(f'Hello {name},')
    print(f'your email : {email}')
    print(f' your password:{password}')

display('abilash','abilashreddy@gmail.com','abilash123')
display('jagadesh','jagadeesh@gmail.com','jagadeesg123')'''


'''def isleapyear(year):
    if year %400 == 0 or(year%4==0 and year % 100 != 0):
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')
for year in range(2001,2027):
    isleapyear(year)'''

'''def sumofdigits(n):
    sum = 0
    while n >0:
        sum += n%10
        n = n//10
    return sum
n = int(input("enter the number :"))
print(f'sum of {n} digits is {sumofdigits(n)}')'''

'''def productofdigits(n):
    product = 1
    while n > 0:
        product *= n%10
        n = n // 10
    return product
n = int(input("enter the number"))
print(f' product of {n} digits is {productofdigits(n)}') '''

'''def checkpassword(password):
    if len(password) > 8 :
        check = set( )
        for i in password:
            if i .isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check) == 4:
            return "strong password"
    return "weak password"
password = input('')
print(checkpassword(password)) '''

'''def table(n):
    print(f'-----------Table - {n}---------')
    for i in range(1,13):
        print(f'{n} * {i}= {n*i}')

for i in range(1,24):
    table(i)'''