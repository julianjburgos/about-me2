Chicken = 5.25
Beef = 6.25
Tofu = 5.75
Small = 1.00
Medium = 1.75
Large = 2.25
fsmall = 1.00
fmed = 1.50
flarge = 2.00
sandwich = None
beverage = None
fries = None
price = float(0)
ketchup = .25
order = []
ordernumber = 0

print("Welcome to Sandwich Place! We have: ")
print("Chicken - $5.25")
print("Beef - $6.25")
print("Tofu - $5.75")
orderchoice = input("Would you like to order?(yes/no) ").lower()
if orderchoice == "yes":
    while orderchoice == "yes":
        ordernumber = ordernumber + 1
        order.append("Order #" + str(ordernumber))
        aska = input("Would you like a sandwich?(yes/no) ").lower()
        
        if aska == 'yes':
            choice = 1
            ask = input("What Sandwich would you like? ").lower()
            while choice == 1:
                if(ask == "chicken"):
                    choice = 2
                    price += Chicken
                    sandwich = ask + " sandwich"
                    order.append("chicken")
                elif(ask == "beef"):
                    price += Beef
                    choice = 2
                    sandwich = ask + " sandwich"
                    order.append("beef")
                elif(ask == "tofu"):
                    price += Tofu
                    choice = 2
                    sandwich = ask + " sandwich"
                    order.append("tofu")
                else:
                    ask = input("What Sandwich would you like? ").lower()
                    choice = 1
        else:
            print("You did not want a sandwich")
            sandwich = "No Sandwich"
                
        ask2 = input("Would you like a beverage?(yes/no) ").lower()
        if(ask2 == "yes"):
            choice = 1
            ask3 = input("What size Beverage would you like? ").lower()
            while choice == 1:
                beverage = ask3 + " beverage"
                if(ask3 == "small"):
                    choice = 2
                    price += Small
                    beverage = ask3 + " beverage"
                    order.append("small beverage")
                elif(ask3 == "medium"):
                    choice = 2
                    price += Medium
                    beverage = ask3 + " beverage"
                    order.append("medium beverage")
                elif(ask3 == "large"):
                    choice = 2
                    price += Large
                    beverage = ask3 + " beverage"
                    order.append("large beverage")
                else:
                    ask3 = input("What size Beverage would you like? ").lower()
                    choice = 1
                    
        else:
            print(ask2)
            order.append("No beverages")
           
        ask4 = input("Would you like fries?(yes/no) ").lower()
        if(ask4 == "yes"):
            choice = 1
            ask5 =input("What size fry would you like? ")
            while choice == 1:
                if(ask5 == "small"):
                    choice = 3
                    x = input("Would you like to mega-size your fries? ").lower()
                    while choice == 3:
                        if(x == "yes"):
                            choice = 2
                            price += flarge
                            print("Mega-sized fry")
                            fries = "Mega-sized fry"
                            order.append("Mega-sized Fry")
                        elif x == "no":
                            choice = 2
                            price += fsmall
                            print("Small Fry")
                            fries = ask5 + " fry"
                            order.append("Small Fry")
                        else:
                            x = input("Would you like to mega-size your fries?(yes/no) ").lower()
                            choice = 3
                elif(ask5 == "medium"):
                    choice = 2
                    price += fmed
                    fries = ask5 + " fry"
                    order.append("Medium Fry")
                elif(ask5 == "large"):
                    chioce = 2
                    price += flarge
                    fries = ask5 + " fry"
                    order.append("Large Fry")
                else:
                    ask5 =input("What size fry would you like? ")
                    choice = 1
        else:
            print(ask4)
            order.append("No Fries")
                    
              
                
        ask6 = abs(int(input("How many ketchup packets would you like? ")))
        price += ketchup * ask6
        order.append(str(ask6) + " ketchup packets")
        if(ask2 and ask4 and aska == "yes"):
            price = price -1
            print("Since you ordered a whole meal, $1 has been deducted from your cost.\n")
            
        print(*order, sep="\n") #the star and sep = "/n" allows the list to separate by line
        orderchoice = input("Would you like to order again?(yes/no) ").lower()
        print("\n")
    else:
        print("Your total price is: $" + str(price))

elif orderchoice == "no":
    print("Ok then leave my restaurant!")
    
        


