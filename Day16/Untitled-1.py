a = eval(input("check the linl active"))
b = eval(input("check the permission"))

if a:
    if b:
        print("file open sucessfully")
    else:
        print("file not open")
else:
    print("link is active")