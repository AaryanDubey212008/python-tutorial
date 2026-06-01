# print((x+y)>)
# logical operators
# #or operators whwen all condkition are fslse then result will be false if any result will be true then result will be true
# #and operators when all conditionm are true then result will be true if any result will be fale then result will be false

# name=input('enter your name')
# if(name=aryan):
#      print('trainer as madrid')
# else:
#      print ('student as madrid')
     

#      age=int(input('enter yourt age'))
#       if(age>=18):
#          print ('yes you can  vote')
#       else (age<18)
#           print('you cannot vote')
               
#                # Problem 1: Age Eligibility and Type Conversion

# Ask the user to enter their birth year as a string. Convert it to an integer and calculate their age (assume the current year is 2026). Using comparison and logical operators, check if the person is both:

# * 18 years or older
# * Age less than or equal to 60
#   Print the age and whether the person is in the “working age group”.

# #birth year= String 
# convert string to integer
# assume current year=2026
# print (the user is eligible to work or not)

# # Problem 2: Shopping Bill with Discount

# Take the price and quantity of an item as input from the user. Convert them to appropriate numeric types and calculate the total amount. If the total amount is greater than 1000 *and* quantity is more than 5, apply a 10% discount. Otherwise, print the normal total. Display final payable amount.
# #problem 2 Shopping bills and discounts
# # Take the price and quantity of an item.
# # convert them to appropriate numeric types and calculate the total amount.
# # if the total amount is greater than 1000 and quantity is more than 5, apply 10% diascount
# # otherwise print the normal total.Display the final amount.

# #price=int(input('enter the price'))

# ## Problem 3: Student Percentage and Pass/Fail Decision

# Take marks of three subjects as input (in string form). Convert them into integers, calculate total and percentage using arithmetic operators. Using comparison and logical operators, print whether the student has:

# * Passed (percentage ≥ 40 *and* each subject mark ≥ 33)
# * Failed otherwise
#   Also print the percentage.

# #problem 3 student percentage and pass/fail decision
# #take marks of three subject as input in string form.
# #passed percentag>=40 and each subject marks >= 33.
# #failed otherwise

# #solution
# # 1. take marks of three subjects as input in (string form)
# sub1_str = input("enter marks for subject 1:'')
# sub2_str = input("enter marks for subject 2:")
# sub3_str = input("enter marks for subject 3:")

# # 2. convert them into integers
# m1 = int(sub1_str)
# m2 = int(sub3_str)
# m3 = int(sub3_str)

# # 3. calculate the total and percentage using arithmetic operators
# total = m1+m2+m3
# percentage = (total/300)*100

# # 4. using comparision and logical operators to determine pass/fail
# # condition: percentage >=40 AND each subject mark>= 33
# if percentage >= 40 and m1 >= 33 and m2 >=33 and m3 >=33:
#     result = "passed"

# else:
#      result ="failed"
     
# # 5. print results
# print(f'\ntotal marks: {total}")
# print(f" percentage: {percentage:.2f}%")
# print(f" result: {result}")


#5. BMI Category Checker

# ask user for weight and height
weight = float(input("enter weight in kg "))
height = float(input("enter height in meters"))


bmi= weight/(height**2)

if (bmi < 18.5):
    print('underwieght')
elif (bmi<=18.5 and bmi <= 24.9):
    print("normal")
else:
    print("overweight")



# 9: salary hike and tax check


# current_salary = float(input("enter your current salary:"))
# performance_rating = float("enter your performance rating(out of 5):"))

# 
# if performance_rating >= 4 and current_salary < 80000:
#     increase_percentage = 0.15 # 15% increase


# else:
#     increase_percentage = 0.05 #5% increase
# 
# new_salary = current_salary *(1+ increase_percengtage)

 






# #4. number comparision with arithmetic result

# # ask the user for two numbers
# # perform the arithmetic operations(addition and multiplication.)
# # determine the sum is greater than the product or both numbers are equal.
# # print the result 

# #21 a,b program-> 5,7--->7 is maximum

# a=int(input())
# b=int(input())

# #5

  # Problem 7: Calculator with Condition Check

# Take two numbers as floats and an operator (+, -, *, /) as input. Perform the corresponding arithmetic operation. Before division, check using comparison operators that the second number is not zero. Use logical operators where needed and print the result.

num1=float(input('enter first number'))
num2=float(input('enter second number'))
op=input()

if(op=='+'):
    print(num1+num2)
elif(op=='-'):
     print(num1-num2)
elif(op=='*'):
    print(num1*num2)
else:
    if(num2!=0):
      print(num1/num2)
    else:
      print('division not possible')



## Problem 8: Electricity Bill Calculator

# Ask the user to enter the number of units consumed as a string and convert it into an integer. Calculate total bill:

# * First 100 units → 5 per unit
# * Next 100 units → 7 per unit
# * Remaining units → 10 per unit
#   After calculating the bill, if the total bill is more than 1500 *or* units are more than 250, add a surcharge of 5%.
#   Print total units  bill amount, and final amount after surcharge if applicable
   
    units=float(input('Enter the units'))
    totalBill=0

    if(units<=100):
        totalBill=units*5
        if(totalBill>1500):
         surCharge=5/100*totalBill
         grandtotal=totalBill+surCharge
         print('Your bill is:',grandtotal)
        else:
           print('Your bill is:',totalBill)
    elif(units>100 and units<=200):
       afterHundred=units-100
       totalBill=5*100+afterHundred*7
       if(totalBill>1500):
          surCharge=5/100*totalBill
          grandtotal=totalBill+surCharge
          print('Your bill is:',grandtotal)
    else:
          print('Your bill is:',totalBill)
    # else:
 
    #    totalBill=5*100+7*100+afterTwoHundred*10
    #    if(totalBill>1500 or units>250):
        #   surCharge=5/100*totalBill
        #   grandTotal=totalBill+surCharge
        #   print('Your bill is:',grandTotal)
        # else:
        #   print('Your Bill is',totalBill)
        
          
          

