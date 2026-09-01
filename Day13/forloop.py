'''s = "python programming"
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])'''

'''l = [12,23,45,34,50,52,53,68,75,10]
sum = 0
for i in range(len(l)):
    if l[i]%2==0:
        sum = sum+ i
        print(i,l[i])
print(sum)'''

'''n = int(input("enter the number:"))
fact = 1
for i in range(1,n + 1):
    fact *= i
    print(f"factorial of {n} is {fact}")'''

'''data = {}
n =int(input("enterthe no of students"))
max_marks = 0
for i in range(n):
    name = input("enter the names: ")
    marks = int(input("Enter the marks"))
    if marks > max_marks:
        max_marks = marks
    data[name] = marks
print(data)
print("maximum marks", max_marks)'''

'''data = {}
a = int(input("no of the products"))
sum= 0
for i in range(a):
    name = input("enter the name of product")
    price= int(input("price of items"))
    quantity=int(input("enter the quantity"))
    total = price*quantity
    data[name]= total
    sum = total
print(data)
print("total amount", sum)'''


'''n = int(input("enter no of products"))
total_bill =0
products = { }
for i in range(n):
    product = input("enter name of products")
    price= int(input("enter the price"))
    quantity = int(input("enter the quantity"))
    final_price = price*quantity
    total_bill = final_price
    products[product]=f"{price}*{quantity} = {final_price}"
print(products)
print("total_bill", total_bill)'''


#practice problems
'''n = int(input("enter the number"))
for i in range(n):
    print(i)'''


'''n = int(input("enter the number"))
for i in range(2,n+1,2):
        print("even",i)'''

'''n = int(input("enter the number"))
sum = 0
for i in range(1,n +1):
    sum = sum +i
    print("sum =", sum)'''

'''n = int(input("enter the numbers"))
sum = 0
for i in range(1,n +2,2):
    sum = sum + i
    print(sum)'''

'''n = int(input("enter the number"))
fact = 1
for i in range(1,n +1):
    fact = fact * i
    print(fact)'''

'''n = int(input("enter the number"))
for i in range(1,11):
    print(f'{n}*{i} = {n*i}')'''

'''n = int(input("enter the number"))
count = 0
for i in range(n):
    if i % 2 ==0:
        count +=1
if count == 2:
      print("prime")
else :
     print("not prime")'''

'''n = int(input("enter the number"))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum  + digit
    n = n // 10
print("sum of digits=", sum) '''
                   
'''sum1 = 0
sum2 = 1
fib = 0
n = int(input("enter the number"))
while fib < n:
    print(sum1,end=" ")
    fib = sum1 + sum2
    sum1 = sum2
    sum2 = fib
    fib = fib + 1'''


'''n = int(input("enter the number"))
count = 0
for i in range(1,n + 1):
    if i% 3 ==0:
        print("divisible",i)
        count = count + 1
    else:
        print("no divisible",i)'''

'''n = int(input("enter the number"))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
    if original==reverse:
        print("palindrome")
    else:
        print("not palindrome")'''

'''n = int(input("enter the number"))
print("multiples of 5 up to", n,"are")
for i in range(5,n+1,5):
    print(i)'''

'''a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
numbers =[a,b,c]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print("maximum number is:",max)'''

'''n = int(input("enter the number"))
reverse = 0
temp = n
while temp > 0 :
    digit = temp % 10
    reverse = reverse * 10+ digit
    temp = temp // 10
print("Reverse of the number is :",reverse)'''

'''n = int(input("enter the number"))
sum = 0
for i in range(n,0,-1):
    sum = sum + i
    print(sum)
    '''
'''n = int(input("enter the number"))
while n >= 1:
    print(n)
    n = n -1'''

'''n = int(input("enter the number"))
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10
    print(product)'''


'''n = int(input("enter the number"))
for i in range(1,n+1):
    if i % 3 ==0 and i % 5 ==0 :
        print(i)'''


'''n = int(input("enter the number"))
for i in range(7,n +1):
    if n % i == 0:
        print(i)'''

'''n = int(input("enter the number"))
while n >=0:
    if n % 2 ==0:
        print(n, end=" ")
    n -=1 '''

'''n =int(input("enter the odd numbers"))
sum = 0
for i in range(1,n +1,2):
    sum = sum + i
    print(sum)'''

'''n = int(input("enter the number"))
for i in range(1,n +1):
    print(i*i)
'''




