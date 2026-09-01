'''for i in range(1,10):
    if i == 15:
        break
    print(i)
else:
    print("end of the loop")'''

'''pin = 1234
epin = int(input("enter the number"))
for _in range(5):
    if pin == epin:
    print("unlock phone")
    break
    else:
    print("Invalid pin")
else:
print("try again after 30 sec")'''

'''n = int(input("enter the number"))
print("factors", end=' ')
for i in range(1,n + 1):
    if n % i ==0:
        print(i,end=' ')'''

'''n = int(input("enter the number"))
c = 0
for i in range(1,n + 1):
    if n % i ==0:
        c+=1
if c ==2:
      print("prime number")
else:
     print("not prime number")'''

'''n = int(input("enter the number"))
for i in range(2,n//2 +1):
      if n % i==0:
        print("not a prime number")
        break
else:
    print("prime number")'''

'''i = 1
while i<=10:
    print(i)
    i +=1'''

'''i =10
while i > 0:
    print(i)
    i-=1'''

'''i = 2
while i<=100:
    print(i)
    i += 2
        '''

'''s = "codegnan"
i = len(s) -1
while i >=0:
    print(s[i],i)
    i-=1'''

'''l =[1,0,7,0,9,8,0,0]
while 0 in l:
    l.remove(0)
print(l)
'''
'''data = {}
total_bill = 0
while True:
    product = input("enter the product (for exit):")
    if product=='exit':
        break
    price = int(input("enter the price"))
    total_bill=price
    data[product]=price
print(data)
print("Total bill",total_bill) '''

'''i =0
while i <= 10:
    i += 1
    if i ==15:
        break
    print(i)
else:
    print("end of the loop")'''
