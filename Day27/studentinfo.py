'''import json
with open("data.json",'r') as file:
    data = json.load(file)
data["name"]= "abilash"'''



'''try:
    a = int(input())
except:
    print("enter the correct data type")
else:
    print(a)
finally:
    print("end of the program")
'''

'''try:
    a = int(input(""))
    k =[1:22,4:24]
    print(1[10])
    print(10/10)
except ValueError:
    print("enter the correct data type")
except KeyError:
    print("key is not there")
except IndexError:
    print("index out of range")
except ZeroDivisionError:
    print("cant divide with zero")
except Nameerror:
    print("define the vairable")
else :
    print(a)
finally:
    print('end of the program')'''


import json

student = {
    "name": "sajid",
    "age": 22,
    "course": 'python'

}
json_data = json.dumps(student)
print(json_data)
student = json.loads(json_data)
print(student)
print(type(student))


''try :
    # a = int(input())
    k = { 11:12,12:13}
    #print(k[14])
    l =[232,54]
    #print(l[10])
    #print(10/0)
    #print('1' + 1)
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("error occured:",e)
else:
    print("error free program")
finally :
    print("end of the program")'''

'''try :
    # a = int(input())
    k = { 11:12,12:13}
    #print(k[14])
    l =[232,54]
    #print(l[10])
    #print(10/0)
    #print('1' + 1)
except Exception as e:
    print("error occured:",e)
else:
    print("error free program")
finally :
    print("end of the program")
'''

try:
    amount = int(input('enter the amount'))
    balance = 5000
    if balance < 0:
        raise Exception("amount needs to be positive")
except Exception as e:
    print("error occured", e)
else:
    print("error free program")
finally:
    print("end of the program")
