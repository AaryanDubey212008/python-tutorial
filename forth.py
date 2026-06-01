# # print numbers from 1 to 10 using while loop 1,2,3
# i=1
# while(1<10):
#   print(i)
#   i=i+1

# # print all even numbers between 1 to 20
#   i=2
# while(1<20):
#   print(i)
#   i=i+2

# # print all odd numbers between 1 to 20
#   i=1
# while(1<20):
#   print(i)
# i=i+1

# print 2,3,4 ( 1to 10)
# i=2
# while(i<22):
#   print(i)
#   i=i+2

# i=3
# while(i<33):
#   print(i)
#   i=i+3

# i=4
# while(i<44):
#   print(i)
#   i=i+4

# upgrade user jo bhi number dale usk table run krde hmara pg

# num=int(input())
# i=1
# while(i<=10):
#   print(f'{num}*{i}={num*i}')
#   i=i+1

# count number of digits
#5678
#76543
# hint->//10
5678//10==567
567//10==56
56//10==5
5//10==0

# n=5678
# cnt=0
# while(n>0):
#   cnt=cnt+1
#   n=n//10

# print(cnt)



# n=76543
# cnt=0
# while(n>0):
#   cnt=cnt+1
#   n=n//10

# print(cnt)

#problems

# sum of digits
#8762->8+7+6+2-23

# hint->//10
8762//10==876
876//10==87
87//10==8
8//10==0

# n=8762
# sum=0
# while(n>0):
#    rem=n%10
#    sum=sum+rem
#    n=n//10

# print(sum)


# reverse digit
# 123->321

ip=123
op=321

n=123
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10



# check if digits are palindrome
#naman  121->yes it is palindrome  123->not

#1234567->no it is not palindrome
# sumo=16 sume=12->no it is not palindrome