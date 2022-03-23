'''
lec7 while loop
'''

i = 5
while i >=0:
    i = i -1
    print(i)
    
i = 5
while i >=0:
    
    print(i)
    i = i-1
    
i = 5

while i >=0:
    
    i = i -1
    
    if i ==3:
        break
    print(i)
    
i = 5

while i >=0:
    
    i = i -1
    
    if i ==3:
        continue
    print(i)
    
i = 5

while i >=0:
    
    i = i -1
    
    if i ==3:
        pass
    print(i)
    
try:
    print(1/0)
    
except ZeroDivisionError:
    print('division by zero')
    
i = 5
while i >=0:
    
    try:
        print(1/(i-3))
    except:
        break
    
    i = i-1
    
i = 5
while i >=0:
    
    try:
        print(1/(i-3))
    except:
        pass
    
    i = i-1
    
i = 5
while i >=0:
    
    try:
        print(1/(i-3))
    except:
        continue
    
    i = i-1