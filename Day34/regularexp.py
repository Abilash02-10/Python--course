#match
'''import re
pattern = r'[0-9]'
text = 'codegnan'
res = re.match(pattern,text)
print(res.group() if res else 'pattern not found')
'''
# search operation
'''import re
pattern = r'[0-9]'
text = 'codegnan2026'
res = re.search(pattern,text)
print(res.group() if res else 'pattern not found')

#findall gives all the occurences of the patternin the text
'''
'''import re
pattern = r'[0-9]'
text = 'codegnan2026'
res = re.findall(pattern,text)
print(res)'''

'''import re
pattern = r'[a-z]'
text = 'codegnan2026'
res = re.findall(pattern,text)
print(res)

'''
#find iter gives with the index of the occurence
'''import re
pattern = r'[a-z]'
text = 'codegnan2026'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
    '''
# validation full match
'''import re
pattern = r'[0-9]{10}'
text = '1234567890'
res = re.fullmatch(pattern,text)
print(res.group() if res else 'pattern not found')
'''
# spliting the string based on the pattern

'''import re
pattern = r'[,(#)]'
text = 'java,python(html#css'
res = re.split(pattern,text)
print(res)
'''
#replacing using sub
'''import re
pattern = r'[a-z]'
text = 'python version 3.14,batch-63'
res = re.sub(pattern,'*',text)
print(res)'''

'''import re
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Edfghj'
res = re.findall(pattern,text)
print(res)
'''

'''import re
pattern = r'^(91)'
text = '91-9876543210'
res = re.findall(pattern,text)
print(res)

'''

'''import re
pattern = r'(0$)'
text = '91-9876543210'
res = re.findall(pattern,text)
print(res)
'''
'''import re
pattern = r'to*'
text = 'to tdfghj too toooo toooooo'
res = re.findall(pattern,text)
print(res)'''

'''import re
pattern = r'to+'
text = 'to tdfghj too toooo toooooo'
res = re.findall(pattern,text)
print(res)'''

'''import re
pattern = r'ab+'
text = 'ab abbb a abbbbbb abbbbbbb'
res = re.findall(pattern,text)
print(res)
'''

'''import re
pattern = r'91|0'
text = '05678'
res = re.findall(pattern,text)
print(res)'''

'''import re
pattern = r'[4567sdtryugio]'
text = '05678'
res = re.findall(pattern,text)
print(res)
'''


