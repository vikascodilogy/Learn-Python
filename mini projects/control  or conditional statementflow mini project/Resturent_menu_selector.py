print(".................................Welcom to Foodology...................................\n");
print("...............Resturent menu List............");
print("1) Breakfat");
print("2) Lunch");
print("3) Dinner\n");
print("-----------------------------------------------\n")
print("Which option would you like to choose\n 1 or 2 or 3\n");
option=int(input("Enter the your option:\n\n"));

# 1)Breakfast
if option==1:
    print("*******Welcom to the Breakfast menu*******");
    print("1) 🇮🇳 Indian Breakfast Menu ")
    print("2) 🇮🇳 English/Continental Breakfast Menu ")
    print("3) 🍽️ Healthy Breakfast \n");
    print("-----------------------------------------------\n")
    print("Pease choose option 1 or 2 or 3 \n");
    BreakfastMenu=int(input("Enter the option of Breakfast menu"));
    
    # Indian Breakfast
    if BreakfastMenu==1:
        print("*******Welcom to 🇮🇳 Indian Breakfast Menu*******");
        print("1)  Aloo Paratha with curd")
        print("2) 🧈 Poha")
        print("3) 🥔 Masala Dosa with chutney & sambar")
        print("4) 🍞 Bread Butter / Jam")
        print("5) 🍳 Omelette or Boiled Eggs")
        print("6) ☕ Chai (Tea)")
        print("7)  Coffee")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 or 3 or 4 or 5 or 6 or 7 \n")
        indian_breakfast=int(input("Enter your Choice:"));
        
        if indian_breakfast==1:
            print("~~~~~Aalu paratha with curd~~~~~")
            print("Price : 120 Rs");
            Quantity=int(input("Enter the Aalu paratha Quantity"));
            total=120*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  Aalu paratha with curd    |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==2:
            print("~~~~~🧈 Poha~~~~~")
            print("Price : 99 Rs");
            Quantity=int(input("Enter the 🧈 Poha Quantity"));
            total=99*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  Poha                      |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==3:
            print("~~~~~🥔 Masala Dosa with chutney & sambar~~~~~")
            print("Price : 49 Rs");
            Quantity=int(input("Enter the 🥔 Masala Dosa with chutney & sambar Quantity"));
            total=49*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🥔 Masala Dosa with \n chutney & sambar    |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==4:
            print("~~~~~🍞 Bread Butter / Jam~~~~~")
            print("Price : 40 Rs");
            Quantity=int(input("Enter the 🍞 Bread Butter / Jam Quantity"));
            total=40*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🍞 Bread Butter / Jam     |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==5:
            print("~~~~~🍳 Omelette or Boiled Eggs~~~~~")
            print("Price : 15 Rs");
            Quantity=int(input("Enter the 🍳 Omelette or Boiled Eggs Quantity"));
            total=15*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🍳 Omelette or Boiled Eggs|  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==6:
            print("~~~~~☕ Chai (Tea)~~~~~")
            print("Price : 10 Rs");
            Quantity=int(input("Enter the☕ Chai (Tea) Quantity"));
            total=10*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  ☕ Chai (Tea)             |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif indian_breakfast==7:
            print("~~~~~☕ Coffee~~~~~")
            print("Price : 15 Rs");
            Quantity=int(input("Enter the Coffee Quantity"));
            total=15*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  Coffee                    |  Rs {total}               |");
            print("------------------------------------------------------")


    # English/Continental Breakfast
    elif BreakfastMenu==2:
        print("*******Welcom to 🇮🇳 English/Continental Breakfast Menu*******");
        print("1) 🍳 Fried Eggs / Scrambled Eggs")
        print("2) 🥓 Toast & Butter")
        print("3) 🧇 Pancakes with honey or syrup")
        print("4) 🥐 Croissant with jam")
        print("5) 🥣 Cereal or Oats")
        print("6)  Coffee")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 or 3 or 4 or 5 or 6  \n")
        English_breakfast=int(input("Enter your Choice:"));
        if English_breakfast==1:
            print("~~~~~🍳 Fried Eggs / Scrambled Eggs~~~~~")
            print("Price : 20 Rs");
            Quantity=int(input("Enter the 🍳 Fried Eggs / Scrambled Eggs Quantity"));
            total=20*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🍳 Fried Eggs / \n Scrambled Eggs    |  Rs {total}               |");
            print("------------------------------------------------------")
               
        elif English_breakfast==2:
            print("~~~~~🥓 Toast & Butter~~~~~")
            print("Price : 100 Rs");
            Quantity=int(input("Enter the 🥓 Toast & Butter Quantity"));
            total=100*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🥓 Toast & Butter         |  Rs {total}               |");
            print("------------------------------------------------------")
             
        elif English_breakfast==3:
            print("~~~~~🧇 Pancakes with honey or syrup~~~~~")
            print("Price : 199 Rs");
            Quantity=int(input("Enter the 🧇 Pancakes with honey or syrup Quantity"));
            total=199*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🧇 Pancakes with honey or syrup  |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif English_breakfast==4:
            print("~~~~~🥐 Croissant with jam~~~~~")
            print("Price : 109 Rs");
            Quantity=int(input("Enter the 🥐 Croissant with jam Quantity"));
            total=109*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🥐 Croissant with jam            |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif English_breakfast==5:
            print("~~~~~🥣 Cereal or Oats~~~~~")
            print("Price : 80 Rs");
            Quantity=int(input("Enter the 🥣 Cereal or Oats Quantity"));
            total=80*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🥣 Cereal or Oats                |  Rs {total}               |");
            print("------------------------------------------------------")
                
        elif English_breakfast==6:
            print("~~~~~Coffee~~~~~")
            print("Price : 30 Rs");
            Quantity=int(input("Enter the Coffee Quantity"));
            total=30*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  Coffee                           |  Rs {total}               |");
            print("------------------------------------------------------")
            
      
        
    # 🍽️ Healthy Breakfast 
    elif BreakfastMenu==3:
        print("*******Welcom to 🍽️  Healthy Breakfast*******");
        print("1) 🥗 Oats with fruits")
        print("2) 🍌 Banana smoothie")
        print("3) 🍎 Fruit salad")
        print("4) 🥚 Boiled egg whites")
        print("5) 🥤 Green tea")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 or 3 or 4 or 5 or 6  \n")
        Healthy_Breakfast=int(input("Enter your Choice:"));
        if Healthy_Breakfast==1:
            print("~~~~~ 🥗 Oats with fruits~~~~~")
            print("Price : 20 Rs");
            Quantity=int(input("Enter the  🥗 Oats with fruits Quantity"));
            total=20*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|   🥗 Oats with fruits      |  Rs {total}               |");
            print("------------------------------------------------------")
               
        elif Healthy_Breakfast==2:
            print("~~~~~🍌 Banana smoothie~~~~~")
            print("Price : 100 Rs");
            Quantity=int(input("Enter the 🍌 Banana smoothie Quantity"));
            total=100*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  🍌 Banana smoothie         |  Rs {total}               |");
            print("------------------------------------------------------")
             
        elif Healthy_Breakfast==3:
            print("~~~~~🍎 Fruit salad~~~~~")
            print("Price : 199 Rs");
            Quantity=int(input("Enter the 🍎 Fruit salad Quantity"));
            total=199*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🍎 Fruit salad                   |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif Healthy_Breakfast==4:
            print("~~~~~🥚 Boiled egg whites~~~~~")
            print("Price : 109 Rs");
            Quantity=int(input("Enter the 🥚 Boiled egg whites"));
            total=109*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🥚 Boiled egg whites             |  Rs {total}               |");
            print("------------------------------------------------------")
            
        elif Healthy_Breakfast==5:
            print("~~~~~🥣 Cereal or Oats~~~~~")
            print("Price : 80 Rs");
            Quantity=int(input("Enter the 🥣 Cereal or Oats Quantity"));
            total=80*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                             |  Price Rs.            |");
            print(f"|  🥣 Cereal or Oats                |  Rs {total}               |");
            print("------------------------------------------------------")
            
        else:
            print("Invalid brakfast menu option");
    
    
# 2) Lunch      
elif option==2:
    print("*******Welcom to the  Lunch menu*******");
    print("1) Veg Menu ")
    print("2) 🍗 Non-Veg ")
    print("-----------------------------------------------\n")
    print("Pease choose option 1 or 2 \n");
    luncMenu=int(input("Enter the option of Lunch menu"));
    if luncMenu==1:
        print("*******Welcom to Veg Menu*******");
        print("1)  Paneer Butter Masala")
        print("2)  Dal Tadka + Jeera Rice")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 \n")
        vegMenu=int(input("Enter your Choice:"));
        if vegMenu==1:
            print("~~~~~Paneer Butter Masala~~~~~")
            print("Price : 120 Rs");
            Quantity=int(input("Enter the Paneer Butter Masala Quantity"));
            total=120*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  Paneer Butter Masala      |  Rs {total}               |");
            print("------------------------------------------------------")
        elif vegMenu==2:
            print("~~~~~Dal Tadka + Jeera Rice~~~~~")
            print("Price : 100 Rs");
            Quantity=int(input("Enter the Dal Tadka + Jeera Rice Quantity"));
            total=100*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                        |  Price Rs.            |");
            print(f"|  Dal Tadka + Jeera Rice      |  Rs {total}               |");
            print("------------------------------------------------------")
            
    elif luncMenu==2:
        print("*******Welcom to 🍗 Non-Veg *******");
        print("1)  Chicken Curry + Rice")
        print("2)  Egg Curry + Roti")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 \n")
        non_veg_Menu=int(input("Enter your Choice:"));
        if non_veg_Menu==1:
            print("~~~~~Chicken Curry + Rice~~~~~")
            print("Price : 150 Rs");
            Quantity=int(input("Enter the Chicken Curry + Rice Quantity"));
            total=150*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                      |  Price Rs.            |");
            print(f"|  Chicken Curry + Rice      |  Rs {total}               |");
            print("------------------------------------------------------")
        elif non_veg_Menu==2:
            print("~~~~~Egg Curry + Roti~~~~~")
            print("Price : 125 Rs");
            Quantity=int(input("Enter the Egg Curry + Roti Quantity"));
            total=125*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                        |  Price Rs.            |");
            print(f"|  Egg Curry + Roti            |  Rs {total}               |");
            print("------------------------------------------------------")
            
    else:
        print("Invalid option")
            
            
        
    
    
    
# 🌙 Denner menu
elif option==3:
    print("Welcom to the 🌙 Denner menu ");
    print("1) 🟢 Veg Dinner Menu ")
    print("2) 🔴 Non-Veg Dinner Menu ")
    print("-----------------------------------------------\n")
    print("Pease choose option 1 or 2 \n");
    luncMenu=int(input("Enter the option of 🌙 Denner menu"));
    if luncMenu==1:
        print("*******Welcom to 🟢 Veg Dinner Menu*******");
        print("1)  Shahi Paneer + Butter Naan")
        print("2)  Veg Pulao + Raita")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 \n")
        vegMenu=int(input("Enter your Choice:"));
        if vegMenu==1:
            print("~~~~~Shahi Paneer + Butter Naan~~~~~")
            print("Price : 130 Rs");
            Quantity=int(input("Enter the Shahi Paneer + Butter Naan Quantity"));
            total=130*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                       |  Price Rs.            |");
            print(f"|  Shahi Paneer + Butter Naan |  Rs {total}               |");
            print("------------------------------------------------------")
        elif vegMenu==2:
            print("~~~~~ Veg Pulao + Raita~~~~~")
            print("Price : 100 Rs");
            Quantity=int(input("Enter the  Veg Pulao + Raita Quantity"));
            total=100*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                        |  Price Rs.            |");
            print(f"|   Veg Pulao + Raita          |  Rs {total}               |");
            print("------------------------------------------------------")
            
    elif luncMenu==2:
        print("*******Welcom to 🔴 Non-Veg Dinner *******");
        print("1)  Butter Chicken + Garlic Naan")
        print("2)  Fish Curry + Steamed Rice")
        print("-----------------------------------------------\n")
        print("Please choose option press 1 or 2 \n")
        non_veg_Menu=int(input("Enter your Choice:"));
        if non_veg_Menu==1:
            print("~~~~~Butter Chicken + Garlic Naan~~~~~")
            print("Price : 180 Rs");
            Quantity=int(input("Enter the Butter Chicken + Garlic Naan Quantity"));
            total=180*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                              |  Price Rs.            |");
            print(f"|  Butter Chicken + Garlic Naan      |  Rs {total}               |");
            print("------------------------------------------------------")
        elif non_veg_Menu==2:
            print("~~~~~Fish Curry + Steamed Rice~~~~~")
            print("Price : 150 Rs");
            Quantity=int(input("Enter the Fish Curry + Steamed Rice Quantity"));
            total=150*Quantity;
            print("------------------------------------------------------")
            print("|   **********Pyament bill**********                 |")
            print( "|  Item                        |  Price Rs.            |");
            print(f"|  Fish Curry + Steamed Rice   |  Rs {total}               |");
            print("------------------------------------------------------")
            
    else:
        print("Invalid option")
            
else:
    print("Invalid option please enter the valide option and try again")
print();
print();
print();

