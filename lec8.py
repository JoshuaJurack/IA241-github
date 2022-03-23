'''
lec8
'''

def my_function(a,b):
    result = a+b
    return result
print(my_function(1,2))

def my_function(a,b=0):
    result = a+b
    #a and b are parameters 
    #the default value of b is 0
    print('a is ', a)
    print('b is ', b)
    
    return result
    
print(my_function(1))
print(my_function(b=2,a=1))

def my_function(a,b=0):
    result = a+b
    #a and b are parameters 
    #the default value of b is 0
    print('a is ', a)
    print('b is ', b)
    
print(my_function(1))

def calculate_abs(a):
    if type(a) is str:
        return('wrong data type')
    elif a>=0:
        return a
    else:
        return -a
        
def cal_sigma(m,n):
    result = 0
    for i in range(n,m+1):
        result = result + i
    return result 
print(cal_sigma(5,3))
        
def cal_pi(m,n):
    result = 1
    for i in range(n,m+1):
        result = result *i
    return result 
print(cal_pi(5,3))
        
def cal_f(m):
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
print(cal_f(0))
print(cal_f(3))
    
def cal_p(m,n):
    return cal_f(m)/cal_f(m-1)
    
print(cal_p(5,3))
        
        
        
        
        
        
        
        
        
        
        
        
        