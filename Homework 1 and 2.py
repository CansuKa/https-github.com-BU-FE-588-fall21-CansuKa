#!/usr/bin/env python
# coding: utf-8

# # Homework 1 and 2 due November 23$^{th}$, 2021
# 
# The aim of this homework is to practive the concepts of basic data structures, control flows and loops in Python. You are expected to use GitHub Classroom and present your work as an html file (i.e. web page) on your progress journals. You can use this jupyter notebook as template to provide your answers.

# ## Task 1
# Implement a Python program to input two numbers and perform all arithmetic operations. You are expected to find the sum, difference, product, quotient and remainder of two given numbers. 
# 
# 
# What is the first number? 4
# What is the second number? 2.5
# The sum is 6.5
# The difference is 1.5
# The product is 8.0
# The integer quotient is 2
# The floating-point quotient is 1.6

# In[ ]:


x = int(input("What is the first number? "))
y = int(input("What is the second number? "))

print("The sum is: ", x+y)
print("The difference is: ", x-y)
print("The product is: ", x*y)
print("The integer quotient is: ", x/y)
print("The floating-point quotient is: ", x/y)


# ## Task 2
# Implement a Python program to input length and width of a rectangle and find area of the given rectangle. 

# In[ ]:


while len(factors)>0:

    l = factors[0]
    w = factors[-1]

    print("The eight possibilites for the lenghth of", l, "and the width of", w, "are: ")
    print()

    first = (x + w,y + l)

    print ("The First Rectangle is the one which is constructed between the point", original_coordinate, "and", first)
    print ("")


# ## Task 3
# Implement a Python program to input any decimal number from user and convert it to binary number system (i.e. base-2 number system)

# In[ ]:


dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# ## Task 4
# Implement a Python program to input a number and check whether number is even or odd using if/else statements.
# 
# Example:
# Input <br>
# Input num: 25 <br>
# Output <br>
# 25 is odd.

# In[ ]:


num=int(input("Enter a number for check odd or even: "))
def find_Evenodd(num):
    
    if(num%2==0):
        print(num," Is an even")
    else:
        print(num," is an odd")
find_Evenodd(num);//function call


# ## Task 5
# Implement a Python program to check if input year is a leap year using if/else statements.

# In[ ]:


Year = 2024
if (Year % 4) == 0:
   if (Year % 100) == 0:
       if (Year % 400) == 0:
           print("{0} is a leap year".format(Year))
       else:
           print("{0} is not a leap year".format(Year))
   else:
       print("{0} is a leap year".format(Year))
else:
   print("{0} is not a leap year".format(Year))


# ## Task 6
# Implement a Python program to print all natural numbers from 1 to n using loop.
# 
# Input number:8
# 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# In[ ]:


def natural_num(n):
    try:
        n=int(n)
        for x in range(1,n+1):
            print(x)
    except Exception as e:
        print(e)
        print("Is {} number?".format(num1))
n=input("Input Number: ")
natural_num(n)


# ## Task 7
# Implement a Python program to input a number from user and swap first and last digit of the given number. This task is easy to perform when input is transformed to a string. However, the aim here is to make use of mathematical operations to perform the swapping operation. One way to perform this task is to divide the input number by 10 until you are left with the first digit. The remainder from the first division is the last digit. Note that there are alternative approaches to perform the same task.
# 
# I used swaping the first and last element using tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with first and last element in that list. Now, the First and last values in that list are swapped. (Output is [24, 35, 9, 56, 12])

# In[ ]:


# Python3 program to swap first
# and last element of a list
 
# Swap function
def swapList(list):
     
    # Storing the first and last element
    # as a pair in a tuple variable get
    get = list[-1], list[0]
     
    # unpacking those elements
    list[0], list[-1] = get
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


# ## Task 8
# Implement a Python program to input any number from user and find cube of the given number using function. 

# In[ ]:


# Python Program to Calculate Cube of a Number

#To take input from user
number = float(input("Enter any numeric Value: "))

cube = number * number * number

print("The Cube of a Given Number {0}  = {1}".format(number, cube))


# ## Task 9
# Write a function to find prime numbers between two integers (i.e. lower and upper bound). Note that you need to control if provided bounds are positive (at least upper bound should be some positive number) and upper bound is larger than provided lower bound.

# In[ ]:


lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 


# ## Task 10
# Implement a Python program that takes a list with numerical elements and find the sum of list elements.

# In[ ]:


l1 = [1, 2, 3, 'A']

sum(filter(lambda i: isinstance(i, int), l1))

# prints 6


# ## Task 11
# Implement a Python program that takes an integer list and find frequency of each element in list. There are built-in functions to perform this task in Python however you are expected perform this task using loops. Example:
# 
# 
# Input
# Input array elements: 4, 9, 9, 5, 100, 1, 2, 1, 2
# 
# Output <br>
# Frequency of 4 = 1  <br>
# Frequency of 9 = 2  <br>
# Frequency of 5 = 1  <br>
# Frequency of 100 = 1  <br>
# Frequency of 1 = 2  <br>
# Frequency of 2 = 2  <br>

# In[ ]:


def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("Frequency of% d =% d"%(key, value))
 
# Driver function
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)


# ## Task 12
# Implement a Python program that reads the side (side sizes between 1 and 5 ) of a square and prints square using hash (#) character.
# 
# Input: 5
# Sample Output: <br>
# Input the size of the square:  <br>
#  $ # # # # # $ <br>
#  $ # # # # # $ <br>
#  $ # # # # # $ <br>
#  $ # # # # # $ <br>
#  $ # # # # # $ <br>

# In[ ]:


#Side sizes between 1 and 5

def square_size(n):
    if n>=1 and n<=5:
        printing="#"*n
        for i in range(n):
            print(printing)
            
size=input("Input the size of the square: ")
square_size(int(size))

