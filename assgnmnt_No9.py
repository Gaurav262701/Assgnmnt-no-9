#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer no 1
#program to check if the given number is a disarium number
def cal_length(n):
    length = 0
    while(n!=0):
        length = length + 1
        n = n//10
    return length

num = 175
rem = sum =0
len = cal_length(num)
n = num 

while(num > 0):
    rem = num%10
    sum = sum + int(rem**len)
    len = len -1
    
if(sum == n):
    print(str(n)+"is a disarium number")
    
else:
    print(str(n)+"is not a disarium number")
        


# In[1]:


#Answer no 2 
#program to find disarium number between 1 to 100
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    


# In[3]:


#Answer no 3
#program to check if the given number is happy number
def isHappyNumber(num):
    rem = sum = 0
    
    while(num >0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10
        
    return sum
num =82
result = num 

while(result !=1 and result!=4):
    result = isHappyNumber(result)
    
if(result == 1):
    print(str(num)+"is a happy number")
    
elif(rsult == 4):
    print(str(num)+"is not happy number")


# In[6]:


#Answer no 4
#program to print all happy numbers between 1 to 100
def check_happy_num(my_num):
    remaining = sum_val = 0
    while(my_num > 0):
        remaining = my_num%10
        sum_val = sum_val + (remaining*remaining)
        my_num = my_num//10
    return sum_val
print("The list of happy number between 1 to 100 :")
for i in range(1,101):
    my_result = i 
    while(my_result != 1 and my_result != 4):
        my_result = check_happy_num(my_result)
    if(my_result == 1):
        print(i)


# In[7]:


#Answer no 5
#Python Program to Check a Number is a Harshad Number
number = int(input("Enter the number"))
sum =0
rem =0

temp = number
while temp > 0:
    rem = temp%10
    sum = sum + rem
    temp = temp//10
    
print("the sum of digits = %d"%sum)

if number % sum == 0:
    print("\n%d is a Harshad number."%number)
else:
    print("%d is not a Harshad number")


# In[8]:


#Answer no 6
#Program to print all Pronic numbers between 1 to 100
def isPronicNumber(num):
    flag = False
    
    for j in range(1,num+1):
        if((j*(j+1))==num):
            flag = True
            break
    return flag

print("pronic number between 1 to 100:")
for i in range(1,101):
    if(isPronicNumber(i)):
        print(i)
        print(" ")

