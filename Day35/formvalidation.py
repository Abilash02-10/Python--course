'''import re
fullname = input("enter the full name")
pattern = r'[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=re.fullmatch(pattern,fullname)
print("valid ful name" if res else "invalid full name")
'''

'''import re
email = input("enter the email")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res = re.fullmatch(pattern,email)
print("valid email" if res else "invalid email")
'''

'''import re
phonenumber = input("enter the phone number")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern,phonenumber)
print("valid phone number" if res else "Invalid phone number")'''

'''import re
password= input("enter the password")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])(A-Za-z\d@$!%*?&]{8,25}$'
res = re.fullmatch(pattern,password)
print("valid password" if res else "Invalid password")'''

'''import re
username = input("enter the username")
pattern = r'^[A-Za-z_0-9]{2,}'
res = re.fullmatch(pattern,username)
print("valid username" if res else "Invalid username")'''

'''import re
adhar= input("enter the adhar number" )
pattern = r'^[0-9.-]{2,12}'
res = re.fullmatch(pattern,adhar)
print("valid adhar" if res else "invalid adhar")
'''

import re
pan = input("enter the pan ")
pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}'
res =