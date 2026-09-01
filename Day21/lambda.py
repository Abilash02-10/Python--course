'''greater = lambda a,b,c : a if a >b else b
print(greater(10,20,30))


wish = lambda name: f"welcome to the course {name}"
print(wish("sajid"))
print(wish('abilash'))

iseven = lambda n : "even" if n%2 == 0 else "odd"
print(iseven(40))
print(iseven(57))

avg = lambda a,b,c : (a+b+c)/3
print(avg(10,20,30))

domain = lambda mail : (mail.split('@')[-1].split('.')[0])
print(domain('sowmya@codegnan.com'))
print(domain('abilash@codegnan.com'))

gst = lambda price :price + price*0.18
print(gst(1000))
print(gst(2000))

prices = [234,567,789,435,456]
res = list(map(lambda price : price + price*0.18,prices))
print(res)


names=['sajid','abful','abilash']
res= list(map(lambda name:name.title(),names))
print(res)

prices = [1234,4567,5678,6789,7890]
res=list(map(lambda price:price-price*0.3,prices))
print(res)


prices =[ 1234,5678,9876,6789,2345,567889]
res=list(filter(lambda prices:prices > 5000,prices))
print(res)

names = {"sajud", 'abdul','asdfgh','asdf'}
res=list(filter(lambda name:len(names) > 5,names))
print(res)'''


'''from functools import reduce

l = [234,4567,6789,34]
res=reduce(lambda sum,i:sum+i,l)
print(res)'''

'''products = {'sugar':50,
            'salt':34,
            'rice':56

}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),reverse=True,key=lambda i:i[1])))'''

a = int(input("enter the units: "))
senior_citizen = eval(input()) == True
bill=0
if 0 <= a <= 100:
    bill = a*1.5
elif 101 <=a<= 200:
    bill = a*2.5
elif 201 <= a <= 300:
    bill = a *4
elif 500 <= a <= 5000:
    bill = a *6
if senior_citizen:
    bill =bill-(bill * 10/100)
if a>=800:
    bill=bill + (bill*0.05)
print(int(bill))
                        

