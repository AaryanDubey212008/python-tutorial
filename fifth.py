#loop ->repition 
# while

# i=0
# while(i<5):
#     print('aryan')
#     i=i+1

## print numbers from 1 to 10 using while loop 1,2,3
# i=1
# while(1<10):
#     print(i)
#     i=i+1

## print all even numbers between 1 to 20 
# i=2
# while(2<20):
#     print(i)
#     i=i+2

## print all odd numberes between 1 t0 20
# i=1
# while(1<20):
#     print(i)
#     i=i+1

## print 2,3,4 (1to 10)
# i=2
# while(2<22):
#     print(i)
#     i=i+2

# i=3
# while(3<33):
#     print(i)
#     i=i+3

# i=4
# while(4<44):
#     print(i)
#     i=i+4

## count number of digits other than zero




#         cnt=cnt+1
#     n=n//10
# print(cnt)n=60908070568
# cnt=0
# while(n>0):
#     rem=n%10
#     if(rem!=0):

# ## sum of digit
# n=97635
# sum=0
# while(n>0):
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# print(sum)

# ## sum of even and odd
# n=87654321
# sumofeven=0
# sumofodd=0
# while(n>0):
#     rem=n%10
#     if(rem%2==0):
#         sumofeven=sumofeven+rem
#     else:
#         sumofodd=sumofodd+rem
#     n=n//10

# print(sumofeven) 
# print(sumofodd)  

# ## nested loop
# #loop ke andr loop
# ## pattern based questions
# #  * * * * *
# #  * * * * *
# #  * * * * *
# #  * * * * *
# #  * * * * *

# i=0
# while i<5:
#     print('* * * * *')
#     i=i+1

# # m-2
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')

# # m-3
# #nested loop
# #matrix method rows and cols
   
# #  1 2 3 4 5
# #  * * * * * row=1
# #  * * * * * row=2
# #  * * * * * row=3
# #  * * * * * row=4
# #  * * * * * row=5

# #notes
# # upar wali while will print the rows
# # niche wali while will print the cols

# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#         print('*',end='')
#         j=j+1
#     i=i+1

# i=2
# while(i<=2):
#      j=1
#      while(j<=1):
#          print('*',end='')
#          j=j+1
#      print()
#      i=i+1

# * * * * * 
# * * * *
# * * *
# * *
# *

# max no. of rows=5
# max no. of cols=5

# i=1 j=(* * * * *) 
# i=2 j=(* * * *)   
# i=3 j=(* * *)
# i=4 j=(* * )
# i=5 j=(* )

# Problem 1
# Print the following pattern:
# *
# **
# ***
# ****
# *****

# max no. of rows=5
# max no. of cols=5


# i=1 j=1
# i=2 j=1,2
# i=3 j=1,2,3
# i=4 j=1.2,3,4
# i=5 j=1,2,3,4,5

# i=1
# while(i<=5):
#      j=1
#      while(j<=5):
#           if(j<=i):
#              print('*',end='')
    
#      j=j+1
    
#      print()
# i=i+1

# Problem 2
# Print the following pattern:
# *****
# ****
# ***
# **
# *

# max no. of rows=5
# max no. of cols=3

# i=1 j=3
# i=2 j=2
# i=3 j=1
# i=4 j=2
# i=5 j=1

# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#         if(j<=6-i):
#             print('*',end='')
#         j=j+1
#     print()
#     i=i+1


# Problem 3
# Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345

# max no. of rows=5
# max no. of cols=5


#     i=i+1i=1
# while(1<=5):
#     j=1
#     while(j<=5):
#         if(j<=1):
#            print(j,end='')
#         j=j+1
#     print()
    
    


# i=1 j=1
# i=2 j=2
# i=3 j=3
# i=4 j=4
# i=5 j=5

# Problem 4
# Print the following pattern:
# 5
# 54
# 543
# 5432
# 54321

# max no. of rows=5
# max no. of cols=5

# i=1 j=1
# i=2 j=2
# i=3 j=3
# i=4 j=4
# i=5 j=5

# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#         if(j<=i):
#          print(6-j,end='')
#         j=j+1
#     print()
#     i=i+1

# factor of 6

# i=1
# n=6
# while(i<=n):
#    if(n%i==0):
#       print('HCF', i)
#       i=i+1

# HCF of 24 and 36

# i=1
# x=24
# n=36
# hcf=0
# while(i<=x and n):  
#    if(n%i==0 and n%i==0):
#        print('hcf',i)
#        i=i+1

# i=1
# m=8
# n=12
# lcm=0
# while(i<=n):
#    if (i%n==0 and i%m==0):
#       lcm=i
#       break
#       i=i+1
   
# print('lcm is',lcm)

# lcm of 16 and 20

# i=1
# m=16
# n=20
# lcm=0
# while(i<n):
#    if(i%n==0 and i%m==0):
#       lcm=i
#       break
#    i=i+1

# print('lcm is',lcm)

# lcm of 17 and 21

# i=1
# m=17
# n=21
# lcm=0
# while(i<n):
#    if(i%n==0 and i%m==0):
#       lcm=i
#       break
#    i=i+1

# print('lcm is ,lcm')

# lcm of 25 and 30

i=1
m=25
n=30
lcm=0
while(i<n):
   if(i%n==0 and i%m==0):
      lcm=i
      break
   i=i+1 

print('lcm is ,lcm')
     
   

   





    
 





