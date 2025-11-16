import random;
num=random.randint(1,100);
tries=0; 
while True:
    guess=int(input("Enter the number:"));
    tries+=1;
    if guess==num:
        print(f"Conguratution your guessing number is found: {tries}");
        break;
    elif guess>num:
        print("your guessing number is greter");
    else:
        print("you guessing number is smaller")