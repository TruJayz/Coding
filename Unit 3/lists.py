# Lists - a collection for storing and oragnizing multiple pices of data.


# lists Syntax (how its written)
# when we want to create a list, we first create a varable, and then assign it to the square brackets []

# [] - square brackets means lists

shoppingList = ['apples','oranges','water',1,2,3,True,['bread','milk']]

# if we want to acess an item from a list, we use the index system. We write the list variable name, and then use the brackets and pass in the number position.

print(shoppingList[4])

trunkparty = ['fan','mini-fridge','laptop','tv','air fryer']

def addItemForCollage(list):
newitem = input("please add a new item")
list.append(newitem)
addItemForCollage(trunkparty)

def removeitemformtrunkparty(list):
    item = ('please type the item you want to remove')
    list.remove(item)
    print(list)



    numberList = [100, 23, 450, 63, 1, 6, 19, 1000]

    def addAndSort(newNumber):
        numberList.append(newNumber)
        numberList.sort()
        print(numberList)

        addAndSort(60)