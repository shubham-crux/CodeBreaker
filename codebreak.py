#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
code =[]

def user_code():
    guess = input("Hey User! Whats your guess for my code:").strip()
    return guess

def system_code():
    while len(code) <4:
        j = random.randint(0,9)
        if j not in code :
            code.append(j)
            if code[0] == 0:
                code.pop
    return code

def user_code_valid(usercode):
    if len(usercode)!=4 or usercode.isdigit() == False:
        return bool(0)
    else:
        return bool(1)
    
def check_actualcode(syscode,usercode):
    result = []
    for i in range(len(syscode)):
        if syscode[i] == int(usercode[i]):
            result.insert(i,'X')
        elif int(usercode[i]) in syscode:
            result.insert(i,'0')
        else:
            result.insert(i,'-')
    return result
    
usercode = user_code()
syscode = system_code()
attempt = 1
while True:
    if user_code_valid(usercode) == True:
        print('Welcome, let us check your guess')
        if(int(usercode)== syscode):
            print('Wow perfect! You are such a code breaker, congratss!!')
            break;
        else:
            hint = check_actualcode(syscode,usercode)
            if hint == ['X', 'X', 'X', 'X']:
                print('Wow perfect! You are such a code breaker, congratss!!')
                break;
            else:
                print('Oh no! Crap! attempt {} failed!, but dont worry see below hints'.format(attempt))
                attempt = attempt + 1
                print(hint)
                print('Give it a one more try buddy!')
                usercode = user_code()

    else:
        print('Please enter valid code!')
        usercode = user_code()


# In[ ]:




