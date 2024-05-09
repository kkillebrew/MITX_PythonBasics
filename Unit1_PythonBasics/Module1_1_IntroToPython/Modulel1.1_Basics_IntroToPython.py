# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:48:14 2023

@author: kkill
"""

# Example problems
6+4*10

(6+4)*10

23**5

# "Positive root of the following equation: 34*x^2 + 68*x - 510 = 0
# Recall: given a*x^2 + b*x + c = 0, 
# then x = (-b +sqrt(b*b - 4*a*c))/(2*a)"
import math
solution1 = (-68 + math.sqrt(68*68 - 4*34*(-510))) / (2*34)
solution2 = (-68-((68**2)-4*34*(-510))**0.5) / (2*34)

import math
math.cos(3.4)**2 + math.sin(3.4)**2

print('hello world')



# Finding types of variables
type(3.5)
type(5)

# 'Casing' one variable type to another
int(4.5)
float(5)

# Basic operators on floats or ints
2+3  #sum
2-3  #difference
2*3  #product
2/3  #division
2//3 #int division; quotient w/out the remainder
2%3  #remainder
2**3 #power

#Excercise 6 problems
#1
6+12-3

#2
2*3.0

#3
- - 4

#4
10/3

#5
10.0/3.0

#6
(2 + 3) * 4

#7
2 + 3 * 4

#8
2**3 + 1

#9
2.1 ** 2.0

#10
2.2  * 3.0

# Excercise 7 problems
#1
a = 3
a + 2.0

#2
a = a + 1.0
a

#3
a = 3
b

# Excercise 8 problems
# 1
3 > 4

#2 
4.0 > 3.999

#3 
4>4

#4 
4 > + 4

#5 
2 + 2 == 4

#6 
True or False

#7
False or False

#8 
not False

#9
3.0 - 1.0 != 5.0 - 3.0

#10
3 > 4 or (2 < 3 and 9 > 10)

#11
4 > 5 or 3 < 4 and 9 > 8

#12
not(4 > 3 and 100 > 6)


# Excercise 9 problems
#1
a = 3
a == 5.0
a

#2
b = 10
c = b > 9
c


# Excercise 10 problems
#1
3 + 5.0

#2
5/2

#3
5/2 == 5/2.0

#4
5/2.0

#5
round(2.6)

#6
int(2.6)

#7
2.0 + 5.0

#8
5*2 == 5.0 * 2.0
















