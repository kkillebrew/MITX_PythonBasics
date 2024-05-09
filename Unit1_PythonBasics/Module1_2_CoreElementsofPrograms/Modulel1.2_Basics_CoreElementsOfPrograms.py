# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:48:50 2023

@author: kkill
"""

## Bindings
# Excercise 1 problems
#1
"a" + "bc"

#2
3 * "bc"

#3
"3" * "bc"

#4
"abcd"[2]

#5
"abcd"[0:2]

#6
"abcd"[:2]

#7
"abcd"[2:]

# String slicing examples
s = 'Python is fun'
s[1:5] # 'ytho' - goes i:j-1
s[:5]  # 'Pytho'
s[1:]  # 'ython is fun'
s[:]   # 'Python is fun'
s[1:12:2] # 'yhni u' - in matlab lingo would be i:k:j-1
s[1:12:3] # 'yoiF'
s[::2]    # 'Pto sfn'

# In and not in operators
'P' in s      # True
'P' not in s  # False


## Strings
# Excercise 2 part 1 problems
# Assume we have:
str1 = 'hello'
str2 = ','
str3 = 'world'

#1
str1

#2
str1[0]

#3
str1[1]

#4
str1[-1]

#5
len(str1)

# Excercise 2 part 2 problems
#1
str1[len(str1)]

#2
str1 + str2 + str3

#3
str1 + str2 + ' ' + str3

#4
str3 * 3

#5
'hello' == str1

# Excercise 2 part 3 problems
#1
'HELLO' == str1

#2
'a' in str3

#3
str4 = str1 + str3
'low' in str4

#4
str3[1:3]

#5
str3[:3]


# Excercise 2 part 4 problems
str1 = 'hello'
str2 = ','
str3 = 'world'
str4 = str1 + str3

#1
str3[:-1]

#2
str1[1:]

#3
str4[1:9]

#4
str4[1:9:2]

#5
str4[::-1]

## Input/Output
# Excercise 3
# Notes



# Problems
# 1
if 6>7:
    print("Yep")
    
#2 
if 6>7:
    print("Yep")
else:
    print("Nope")
    
# 3
var = 'panda'
if var == 'Panda':
    print("Cute!")
elif var == "Panda":
    print("Regal!")
else:
    print("Ugly...")
    
# 4
temp = 120
if temp > 85:
    print("Hot")
elif temp > 100:
    print("REALLY HOT!")
elif temp > 60:
    print("Comfortable")
else:
    print("Cold")
    
# 4
temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")

## IDEs
# Notes
# Integrated development environment
# Using spyder

# Excersie: hello world
# Write a peice of code that prints hello world
print('hello world')


## Control Flow
# Notes
# a += b is equivalent to a = a + b
# a -= b is equivalent to a = a - b
# a *= b is equivalent to a = a * b
# a /= b is equivalent to a = a / b

# Exercise: happy
happy = 3
if happy > 2:
    print('hello world')
    
# Excercise 4:
# Problems:
# 1:
num = 0
while num <= 5:
    print(num)
    num += 1
    
print('Outside of loop')
print(num)

# 2: 
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

# 3:
num = 10
while num > 3:
    num -= 1
    print(num) 

# 4:
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

# 5:
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 


# Exercise: while
# Problems:
# 1: Convert the following into code that uses a while loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

iI = 2
while iI <= 10:
    print(iI)
    iI += 2
print('Goodbye!')

# 2:Convert the following into code that uses a while loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print('Hello!')
iI = 10
while iI >= 2:
    print(iI)
    iI -= 2

# 3:
# Write a while loop that sums the values 1 through end, inclusive. end is a 
# variable that we define for you. So, for example, if we define end to be 6, 
# your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

end = 6
iI = 1
total = 0
while iI <= end:
    total = iI + total 
    iI += 1
print(total)


# Exercise: For 
# Notes:
# For loop syntax
# Matlab:
# for iI = 1:length(x)
# Python:
# for iI in range(x)  # range will run 0:4
# could also use range(2, 10, 2), which goes from 2:10 by 2's (2, 4, 6, 8), 
# not 10 as it stops at 1- the last value

# Problems:
# 1: Convert the following into code that uses a while loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!
for iI in range(2,12,2):
    print(iI)
print('Goodbye')

# 2:Convert the following into code that uses a while loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
print('Hello!')
for iI in range(10,0,-2):
    print(iI)

# 3:
# Write a while loop that sums the values 1 through end, inclusive. end is a 
# variable that we define for you. So, for example, if we define end to be 6, 
# your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.
end = 6
total = 0
for iI in range(1,end+1,1):
    total = total+iI
print(total)


## Iteration
# Exercise 5:
# 1
num = 10
for num in range(5):
    print(num)
print(num)
# Will print 1, 2, 3, 4, 4

# 2
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
# Will print 0, 1, 2, 3, 4

# 3
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
# Will print 0, Foo!, 4, 8, 12, 16, Foo!

# 4
for letter in 'hola':
    print(letter)  
# Will print h, o, l, a

# 5
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
# Will print Letter # 0 is S, 1


# Exercise 6:
# Problems:
# 1
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')
# Will print 6, ., 0, 0, x, done
# 6 will print 1x
# . will print 1x
# 0 will print 2x
# x will print 1x
# done will print 1x

# 2
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
# Will print H, e, e, l, l, l, o, !, !, done 
# H will print 1x
# e will print 2x
# l will print 3x
# o will print 1x
# ! will print 2x
# dont will print 1x

# 3
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
# Will print M, numVowels is: 12, numCons is: 24
# o will print 1x
# M will print 2x
# numVowels will print 11
# numCons will print 25

