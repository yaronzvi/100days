
# weight = 80
# height = 1.75

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26

#print (f'{weight} + ({height} x {height}) = '+ str(int(weight)/(float(height)*float(height))))
# print ("{:10.0f}".format(float(weight)//(float(height)*float(height))))
#########################################################################################################
# age = input("What is your current age?")

# You have 12410 days, 1768 weeks, and 408 months left.
# max_years = 90
# days = (max_years-int(age))*365
# weeks = ((max_years*52)-(int(age)*52))
# months = ((max_years*12)-(int(age)*12))

# print ("You have {:10.0f} days, {:10.0f} weeks, and {:10.0f} months left".format(days,weeks,months))

#################################################################################################
# number = int(input("Which number do you want to check? "))

# This is an odd number.
# This is an even number.
# result = number % 2

# if result == 0 :
#     print ('This is an even number.')
# else:
#     print ('This is an odd number.')

#########################################################################################

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."  

# underweight, normal weight,slightly overweight, obese, clinically obese
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = weight / height**2

# underweight_str = 'you are \033[1munderweight\033[0m' 
# normal_str = 'you have a \033[1mnormal weight\033[0m'
# overweight_str = 'you are \033[1mslightly overweight\033[0m'
# obese_str = 'you are \033[1mobese\033[0m'
# clinically_obese = 'you are \033[1mclinically obese\033[0m'

# if bmi < 18.5:
#     res =  underweight_str
# elif bmi >= 18.5 and bmi <25:
#     res = normal_str
# elif bmi >=25 and bmi <30:
#     res =  overweight_str
# elif bmi >=30 and bmi <=35:
#     res =  obese_str
# elif bmi >= 35:         
#     res = clinically_obese

# print (f'Your BMI is {:3.0f},{}'.format(bmi,res))

####################################################################
# on every year that is evenly divisible by 4 

# **except** every year that is evenly divisible by 100 

# **unless** the year is also evenly divisible by 400

# year = int(input("Which year do you want to check? "))

# divisible_by_4 = year % 4

# divisible_by_100 = year % 100

# divisible_by_400 = year % 400

# if (divisible_by_4 == 0 and divisible_by_100 != 0) or (divisible_by_4 == 0 and divisible_by_100 == 0 and divisible_by_400 ==0):
#     print ("Leap year.")
# else:
#     print("Not leap year.")

######################################################################################################

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill= 0

# if size == 'S': 
#     bill = bill + 15
# elif size == 'M':
#     bill = bill + 20
# elif size == 'L': 
#     bill = bill + 25

# if size == 'S' and add_pepperoni == 'Y':
#     bill = bill + 2

# if (size == 'M' or size == 'L') and add_pepperoni == 'Y':
#     bill = bill + 3

# if extra_cheese == 'Y':
#     bill = bill + 1

# print('Your final bill is: ${}.'.format(bill))     

#################################################################


# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."



# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_name = name1.strip() + name2.strip()
# combined_name = combined_name.upper()
# combined_len = len(str(combined_name))

# true_str =  'TRUE'
# love_str = 'LOVE'

# total_true = 0
# total_love = 0

# print(combined_name)
# print(combined_len)


# for y in range(4):
#     if str(combined_name).count(true_str[y]) > 0:
#         total_true = total_true + str(combined_name).count(true_str[y]) 

# for y in range(4):
#     if str(combined_name).count(love_str[y]) > 0:
#        total_love = total_love + str(combined_name).count(love_str[y]) 
           

# total = total_true*10+total_love
# # print(total_true*10+total_love)

# if total < 10 or total > 90:
#     print(f"Your score is {total}, you go together like coke and mentos.")
# elif  total >= 40  and total <= 50:
#     print(f'"Your score is {total}, you are alright together."') 
# else:
#     print(f"Your score is {total}.") 
#################################################

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def plusMinus(arr):
#     # Write your code here
#     #print (1,2,3)
#     #length = len(arr)
#     #print (length)
#     pos_num = 0
#     neg_num = 0
#     zero_num = 0
#     for i in arr:
#         if i == 0:
#             zero_num += 1
#         elif i > 0:
#             pos_num += 1
#         else:
#             neg_num += 1        
#     print('{:10.6f}'.format(pos_num/n))
#     print('{:10.6f}'.format(neg_num/n))
#     print('{:10.6f}'.format(zero_num/n))

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)

#############################################################

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def miniMaxSum(arr):
#     # Write your code here
#     min_val = min(arr)
#     max_val = max(arr)
#     sum_val = sum(arr)
#     print('{} {}'.format(sum_val-max_val,sum_val-min_val))



# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

#mondy_tempretue = [9.1,77,87,5.5]

# def foo(x, array):
#     if x in array:
#         return True
#     else:
#         return False
 
# print(foo(1, [1, 2, 3]))
# print(foo(1, [2, 3]))
# print(foo(1, ['1', 2, 3]))

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

# for values in phone_numbers.values():
#     alt_val = values.replace('+','00')
#     print (alt_val)
###########################################
# def foo(chr1,filepath1):
#     with open(filepath1) as file:
#         contant = file.read()
#         num_of_cur = contant.count(chr1)
#     print (num_of_cur)

# foo('a','text1.txt')    

# with open('file.txt','w') as file:
#     file.write('snail')
##############################################
# bear_bear_contant = ''
# with open('bear.txt') as file:
#     bear_contant = file.read()

# with open('first.txt','w') as file2:
#     file2.write(bear_contant[:90])


import time
import os
import pandas

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temps_today.csv')
        print(data.mean()["st1"])
    else:
        print('file does not exist.')        
    time.sleep(10)

# git remote add origin https://github.com/yaronzvi/100days.git
# git branch -M master
# git push -u origin main

#123
    