'''import sys
#print(sys.path)
#print(sys.version)
print('start')
sys.exit()
print('end')'''

'''import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''

'''import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))
print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.floor(12.0001))
print(math.floor(12.3))
print(math.floor(12.6))
print(math.abs(-10))
'''

'''import math
print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,3))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
'''

'''import random
print(random.randint(1,10))
print(random.randint(1000000,9999999))
print(random.random())
print(random.uniform(1,6))


I = ['s','A','I']
print(random.choice(I))
print(random.choices(I,k=2))
random.shuffle(I)
print(I)'''

'''from collections import Counter
s ='python programming'
m = 'this is that that is this is is '
l = [1,1,1,1,1,2,2,2,2,2,45,67,89]
print(Counter(s))
print(Counter(m))
print(Counter(l))
'''
'''from collections import defaultdict
s = 'python programming'
m = "this is that is is fgh this"
l = [1,1,1,1,1,1,22,2,2,2,45678,7]
d = defaultdict(int)
for i in s :
    d[i]+=1
print(i)'''

'''from collections import deque
l = deque([])
l.append(10)
l.append(10)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()

print(l)'''

from itertools import combinations,permutations
res1 =list(combinations('abc',2))
res2 = list(permutations('abc',2))
print(''.join(i) for i in res1)
print(''.join(i) for i in res2)