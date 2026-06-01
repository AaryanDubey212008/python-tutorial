# solution

#

### Problem 9: Salary Hike and Tax Check

### Problem 9: Salary Hike and Tax Check

# Ask the user to enter their current salary (float) and performance rating (out of 5).   old salary, new salary, and taxability status.
# If rating is greater than or equal to 4 and salary is less than 80000, increase salary by 15%; otherwise increase by 5%.
# Then check using comparison and logical operators whether the new salary is taxable (greater than 50000). Print

# salary=float(input('enter the salary:'))
# rating=int(input('enter the rating:'))

# hike=0
# totalSalary=0

# if(salary<80000 and rating>=4):
#     hike=15/100*salary
#     totalSalary=salary+hike
#     if(totalSalary>50000):
#         print('Taxable,salary,totalSalary')
#     else:
#         print('Non Taxable',salary,totalSalary)

# else:
#     newHike=5/100*salary
#     totalSalary=salary+newHike
   


# ### Problem 10: Voting Booth Validator

# # Take age and city name as input. Convert age to integer. Using logical operators, verify that the person is at least 18 and does not live in a restricted city named "TestCity". Print whether they can vote in the local booth. Also print how many years are left if they are underage (use arithmetic operator).

# #43 and jaipur test=delhi>>-does not vote
# #23 and delhi vote
# age=int(input(enter the age))
# city=float(input(enter the city))
# testcity= 'delhi'

 


# ### Problem 12: Mobile Data Usage Bill

# # Ask the user to input total data used in GB (float). CoIf usage is greater than 10 GB and less than or equal to 25 GB, give 8% discount; if greater than 25 GB, give 12% discount. Also add 18% tax if final amount is greater than 1000 using logical operators. Print usage and final bill.
 
# data=float(input('enter the data usage'))
### Problem 11: Triangle Type Finder

# Take three sides of a triangle as input (convert to floats). First check if a valid triangle can be formed using comparison and logical operators (sum of any two sides greater than third). If valid, determine whether it is equilateral, isosceles, or scalene. Also print the perimeter using arithmetic operators.
#side1=side2 or side2=side3 0r side3=side1

# side1=float(input('Enter side 1:'))
# side2=float(input('Enter side 2:'))
# side3=float(input('Enter side 3:'))

# if(((side1+side2>side3)or(side2+side3>side1)or(side3+side2>side1))and(side1!=0 and side2!=0 and side3!=0)):
#     print('Valid triangle')
#     if(side3==side2 and side1==side3):
#         print('Equilateral')
#     elif(side1==side2 or side2==side3 or side1==side3):
#         print('scalene')
# else:
#     print('Not a valid triangle')



# ### Problem 12: Mobile Data Usage Bill

# Ask the user to input total data used in GB (float). Convert if required. Calculate the base bill at 50 per GB. If usage is greater than 10 GB and less than or equal to 25 GB, give 8% discount; if greater than 25 GB, give 12% discount. Also add 18% tax if final amount is greater than 1000 using logical operators. Print usage and final bill.

# data=float(input('Enter the data'))
# totalBill=0
# discount=0
# if(data>10 and data<=25):
#     totalBill=data*50
#     discount=8/100*totalBill
#     finalBill=totalBill-discount
#     if(totalBill>1000):
#         gst=18/100*totalBill
#         gstBill=finalBill+gst
#         print('bill:',gstBill)
#     else:
#         print('bill':,finalBill)
# elif(data>25):
#     totalBill=data*50
#     discount=12/100*totalBill
#     finalBill=totalBill-discount
#     gst=18/100*totalBill
#     gstBill=finalBill+gst
#     print('bill',gstBill)
# else:
#     totalBill=data*50
#     print('bill:',totalBill)

# Problem 13: Temperature Converter and Weather Check

# Take temperature input in Celsius as a string, convert it to float,and convert it to Fahrenheit using AO
# Using comparision and logical operators,print whether the weather is cold(<=15),pleasant(16-30),or hot(>30).
# Also print both celsius and Fahrenheit values.

# solution

# temperature=float(input('Enter the temperature in celsius'))
# temperature=float(input('Enter the temperature in Fahrenheit'))
# temperature=0
# temperature in Fahrenheit=(Celsius*9/5)+32
# if('temperature <=15'):
#     print('cold')
# elif('temperature 16-30 it is plesant'):
#     print('pleasant')
# else('temperture >30 it is hot'):
#     print(hot)



    
    


# ### Problem 14: Password Strength Checker

# Ask the user to input password length (integer) and whether it contains special characters ("yes"/"no"). Using logical and comparison operators, determine if password is Strong (length ≥ 8 and has special characters), Medium (length ≥ 6 or has special characters), or Weak otherwise. Print the strength category.

# solution

# Password=int(input("yes"/"no"))
# if(lenght>=8 and "yes"/"no")
#    print('strong')
# else(lenght>=6 or"yes"/"no")
#    print(weak)

   
# ### Problem 15: Profit or Loss with Percentage

# Ask the user to input cost price and selling price (floats). Calculate profit or loss amount and percentage using arithmetic operators. Using comparison operators, print whether it is profit, loss, or no profit-no loss. Also check logically if profit percentage is more than 20% and print a message "High Profit" if true.

costprice=float('Enter costprice')
sellingprice=float('Enter sellingprice')

                


# ### Problem 16: Attendance Eligibility for Exam

# Take total classes and attended classes as integers. Calculate attendance percentage. Using comparison and logical operators, check if attendance is at least 75% and the student does not have any medical leave flag set to "no" or "yes". If attendance < 75 but medical leave is "yes", still allow. Print eligibility and attendance percentage

# totalclasses=int('Enter totalclasses')
# attendedclasses=int('Enter attendedclasses')
# attendance percentage=totalclasses/100*attendedclasses
#     print('attendance percentage')
# if:('attendance=75% and student not have any medical leave flag'):
#     print("no" or "yes")
# elif:('printattendance<75 but medical leave'):
#     print("yes")
