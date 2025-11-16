
# 1)print number from 10 to 40
# for i in range(10,41,1) :
#     print(i);
    
# 2)print number from -10 to 20
# for i in range(-10,21,1):
#     print(i)

# 3)print number from 34 to 5
# for i in range(34,4,-1):
#     print(i);

# table print any number
# table=int(input("Enter the an number:"));
# for i in range(table,table*10+1,table):
#     print(i);

# string print one by one charactor
# s="Hello how are you";
# for i in s:
#     print(i);

# s="Hello how are you";
# for i in range(0,len(s),1):
#     print(s[i]);

# a="Nature";
# for i in range(len(a)):
#     print(a[i]);


# Loop Practice Set 
# Ques 1) Print "Hello world" n times use a loop to repeat a print statement ("Hello world") based on user input count n
# n=int(input("Enter the number"));
# for i in range(n):
#     print("Hello world"); 


# Ques 2) Print Number from 1 to n Display numbers in increasing order from 1 up to a given number n
# n=int(input("Enter the last number:"));
# for i in range(1,n+1):
#     print(i);

# Ques 3) Print Number from n to 1 
# Display numbers in decreasing order from n down  to  1
# n=int(input("Enter the last number:"))
# for i in range(n,0,-1):
#     print(i)

# Question 4)
# x=int(input("Enter the number"));

# sum=0;
# for i in range(1,x+1):
#     sum=sum+i;
# print("total n number sum is :-",sum)

# Question 5)
# n=int(input("Enter the number:"));
# mult=1;
# for i in range(1,n+1):
#     mult=mult*i;
# print(f"Fatorial is:{mult}"); 

# Qustion 6
# num=int(input("Enter the number"));
# even_sum=0;
# odd_sum=0
# for i in range(num+1):
#       if i%2==0:
#           even_sum+=i;
#       else:
#           odd_sum+=i;
# print(f"Hello your even sum is {even_sum} and odd sum is{odd_sum}");


# Question 7
# num=int(input("Enter the number:"));
# for i in range(1,num+1):
#     if num%i==0:
#         print(f"factor = {i}")
    
# Question 8
# num=int(input("Enter the number:"));
# sum=0;
# for i in range(1,num+1):
#     if num%i==0:
#         sum+=i
# print(f"factor = {sum}")


# Question 9
# a=int(input("Entner the base"));
# b=int(input("Enter the exponent number"));
# ans=1;
# for i in range(1,b+1):
#     ans=ans*a;
# print(f"a^b={ans}");

# Question 10 prime number

# n=int(input("Enter the number:"));
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1;
# if count==1:
#     print("your number is a unity number:");
# elif count==2:
#     print("your numbe is prime");
# else:
#     print("your number is composite")


# or


# n=int(input("Enter the number:"));
# for i in range(2,n):
#     if n%i==0:
#         print("sorry your number is composit")
#         break;
# else:
#     print("Your number is prime")
        


# Practice Question 
# Question 1) Calculate the sum of digits

# n=input("Enter the number:");
# sum=0
# for i in n:
#     sum=sum+int(i);
# print(f"All digit sum= {sum}")

# n=input("Enter the number:");
# sum=0;
# for i in range(len(n)):
#     sum=sum+int(n[i]);
# print(sum);

# Question 3) Count upercase and lowercase latter
# latter=input("Enter the charactor");
# u=0;
# l=0;
# for i in latter:
#     if i.isupper():
#         u=u+1;
#     elif i.islower():
#         l=l+1;
# print("Upper Values is",u);
# print("Lower values is",l);

# Quetion 4) Count event and odd digits
# num=input("Enter the number:");
# odd=0;
# even=0;
# for i in num:
#     if int(i)%2==0:
#         even=even+1;
#     elif int(i)%2!=0:
#         odd=odd+1;
# print("Even is",even);
# print("Odd is:",odd);

# Question 5) Print pelindrome number
# startN=int(input("Enter the start number"));
# endN=int(input("Enter the end number"));
# for i in range(startN,endN+1):
#     if str(i)==str(i)[: : -1]:
#         print("Pelimdrome number",str(i));