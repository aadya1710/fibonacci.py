#taking 1st three numbers of fibonacci series

a=0 
b=1
c=1
n= int(input("Enter n : "))
for i in range(2,n):
    a=b
    b=c
    c=a+b 
print(c)
