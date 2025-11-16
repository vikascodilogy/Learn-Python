# Question 1) Print each Digit (Reverse order)
#     Break a number into individual digits and them starting from the last digit.

# a=123;
# b=str(a)
# print(b[0]);
# print(b[1]);
# print(b[2]);

# or

# a=int(input("Enter the number"));
# while a>0:
#     print(a%10);
#     a=a//10;

# Question 2) sum of digits
# Ad all the digits of a number (e.g 123->1+2+3=6)
# n=int(input("Enter the number"));
# sum=0
# while n>0:
#     sum=sum+n%10;
#     n=n//10;
# print(f"digit sum is {sum} ")
    
    
    
# Question 3) Reverse a number
    # input a number and reverse its digits (e.g 123 -> 321)
# n=int(input("Enter the number"));
# rev=0;
# while n> 0:
#     rev=rev*10 +n%10;
#     n=n//10;
# print(rev);


# Question 4) Palinfrome number check 
    # check if a number reads the same forword(e.g. 121,1331)
# a=int(input("Enter the number:"));
# copy=a;
# rev=0;
# while a>0:
#     rev=rev*10 +a%10;
#     a=a//10;
# if rev==copy:
#     print("Your number is pelindrom number");
# else:
#     print("Your number is not pelindrom")


# Question 5) Automorphic number
# a=int(input("Enter the nubmer:"))
# dup=a
# count=0;
# square=a**2;
# while a>0:
#     count=count+1;
#     a=a//10;
# extract=square %(10**count);
# if extract==dup:
#     print("your nmber is automorphic");
# else:
#     print("Your number is not automorphic");






# ****************************practice Question of While loop******************************

# 1) Continuouse number input & sum
# sum=0;
# while True:
#     n= int(input("Enter the number"));
#     sum=sum+n
#     if n==0:
#         break;
# print(sum)


# 2) Palindrome number check 
# n=int(input("Enter the number:"));
# copy=n;
# rev=0;
# while n>0:
#     rev=rev*10+n%10;
#     n=n//10;
# if rev==copy:
#     print("This is a pelindrome number:");
# else:
#     print("This is not a pelimdrome number:")



# 3) product of Digit
# n=int(input("Enter the number:"));
# mult=1;
# while n>0:
#     fact=n%10;
#     n=n//10;
#     mult=mult*fact
# print(mult);

# 4) Harshad number check 
# n=int(input("Enter the number:"));
# copy=n
# sum=0
# while n>0:
#     sum=sum+n%10;
#     n=n//10;
# if copy%sum==0:
#     print("Harshad number:")
# else:
#     print("Not a harshad number")



# 5) Average until negative input

# sum=0;
# count=0;
# while True:
#     n=int(input("Enter the number"));
#     sum=sum+n;
#     count=count+1;
#     if n<0:
#         break;
# avg=sum/count;
# print(avg);

# Question 6) strong number check 
# n=int(input("Enter the number"));
# while n>0:
#     fact=n%10;
#     n=n//10;
#     print(fact)


