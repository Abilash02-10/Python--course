'''def display(n):
    n = n+10
    print("Inside:", n)

n = 10
display(n)
print('outside', n)'''

'''def display():
    print("inside", n)
n = 20
display()
print("outside", n)'''

'''def display():
    n = 10
    print("inside :",n)

display()
print("outside",)'''

'''def display():
    global n
    n = n + 10
    print("inside", n)

n = 10
display()
print('outside:', n)
'''

'''def display():
    global n
    n = 'PFS'
    print("updated course", n)

n = "JFS"
display()
print("Final Course", n)'''

#nested d
def display():
    n = "JFS"
    def update():
        nonlocal n
        n = "PFS"
        print("updated course", n)
    update()
    print("final course", n)
display()