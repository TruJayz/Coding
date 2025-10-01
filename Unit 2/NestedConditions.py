# Nested conditions = A conditional statement thats has other conditional
# Statements within in. Conditions inside of conditions.

def sandwichStore():
    pritnt("Weelcome to the store")
    selection = input("Please select your food. What do u like?")
    print("1. meatball sandwich")
    print("Turkey sandwich")
    print("3. Honey turkey sandwich")
    print("4. buffallo chicken ")
    selection = ("please pick a side")
    if selection == 1:
    print("You choose the meatball sandwich")
    print("whats sides do you want?")
    print("1. fries")
    print("2. saled")
    print("3. chips")
    side =int(input)())
    if side == 1:
        print("Great meatball sandwich and fries")
    elif side == 2:
        print("healthy meatball sandwich and fries")
    elif side == 3:
        Print("meatball sandwich and chips")
    else:
        print("sorry, dont understand your side.")
        if selection == 2:
            print("sorry we are out of terkey sandwichs")
        sandwichStore()

        sandwichStore()

        def atm():
            balence = 2000
            pin = 1234

            userpin = input("Please type in your pin")
            if userpin == pin:
                print("Welcome, what would you like to do?")
                print("1. withdraw money")
                print("2. deposit money")
                print("3. check your balence")
                selection = input()
if selection == 1:
    amount = int(input("how much do you want to take out"))
    if amount> balence:
        pritn(" sorry you dont have that much in your account")
    else:
        newbalence = balence- amount
        print('your new balence is :' + str(newbalence))
    else:
print("sorry incorrect.")
atm()

def atm(): 

