#-------------------------------------------------------
# Author : Robert Sanborn
# File : eTipMaster
# Description : CSCI 141 WWU, Pr. Jagodzinski
# Date : 11/21/16
#-------------------------------------------------------


# Function : roundTotalTip
# Inputs : unroundedTip
# InputType : float
def roundTotalTip(unroundedTip):

    # The variable unroundedTip is converted from a float to a string and saved
    str_unroundedTip = str(unroundedTip)

    # The index of the "." (decimal) character in the string str_unroundedTip
    # is found and saved to memory as decPlace
    decPlace = (str_unroundedTip).index(".")

    # The value of the expression decPlace + 3, is calculated then saved to memory
    # This number is used to round the number to the nearest hundreth
    thousandthPlace = decPlace + 3

    # If the number with the index thousandthPlace is 5, 6, 7, 8, or 9, the 
    # hundreth place is incremented and thus unroundedTip is updated
    if str_unroundedTip[thousandthPlace] in "56789" :
        unroundedTip = unroundedTip + 0.01
        
    # The float variable unroundedTip is again converted into a string
    str_unroundedTip = str(unroundedTip)

    # The slice of str_unroundedTip going from the first index up to the index
    # of the thousandth place of the floating number is generated.
    # This string of at least 4 characters is then converted back into a float
    # and saved to memory to the variable ruffTip, which the function then returns.
    ruffTip = float(str_unroundedTip[:thousandthPlace])

    return ruffTip


# Function : calculateHeadCountTip
# Inputs : numCustomers
# InputType : integer
def calculateHeadCountTip(numCustomers):

    # If the value of variable numCustomers is greater than 1,
    # the value (numCustomers ^ 1.04) is returned
    if numCustomers > 1:
        return (numCustomers ** 1.04)

    # Otherwise the value of expression (2^1.04 - 1) is returned
    else:
        return ((2 ** 1.04) - 1)


# Function : calculateCocktailDiscount
# Inputs : numCustomers, numCocktails, costOfMeal
# InputType : integer, integer, float
def calculateCocktailDiscount(numCustomers, numCocktails, costOfMeal):

    # If the value of variable numCocktails is less than the
    # value of variable numCustomers, the integer 0 is returned
    if (numCocktails < numCustomers):
        return 0
    
    # Otherwise 9 percent of the value of variable costOfMeal, a float, is returned
    else:
        return ((costOfMeal) * 0.09)

    
# Function : calculateFloorTip
# Inputs : floorLevel, numCustomers
# InputType : integer, integer
def calculateFloorTip(floorLevel, numCustomers):

    # If the value of variable numCustomers is greater than 2,
    # the value of the following expression is returned
    if (numCustomers > 2) :
        return (0.1 * ((numCustomers) ** (floorLevel)))
    
    # Otherwise the value of product of the two variables, both of type integer,
    # floorLevel and numCustomers, is returned
    else:
        return ((floorLevel)*(numCustomers))


# Function : calculateTotalTip
# Inputs : headTip, drinksDiscount, floorTip
# InputType : float, float, float
def calculateTotalTip(headTip, drinksDiscount, floorTip):
    
    # The absolute value of the expression: headTip - drinksDiscount + floorTip,
    # is returned as a float; all three variables in the expression are of type float
    totalTip = abs(headTip - drinksDiscount + floorTip)
    return totalTip


# Function : main
# Inputs : none
def main():

    # Txt file, "dailySpreadSheet.txt" is opened for writing purposes
    fileInput = open("dailySpreadSheet.txt", "w")

    # List of information is sent to file, each entry in the list gives the name
    # of the data point that corresponds to the same index of the list it is found in
    fileInput.write("numGuests | numCocktails | numFloor | costOfMeal | headTax | floorTax | cocktailDiscount | totalTip | roundedTip" + "\n")

    # While loop is initiated and will continuously iterate until the isThereMore
    # Boolean variable is updated to false
    isThereMore = True
    while isThereMore :

        print("========================================================")
        print()
        
        # Worker at the Restraunt using this program to calculate tips for
        # the dinner party will first be prompted with the question of whether or
        # not there is another party.
        workerInput = input("Is there another party that needs to pay there tip? ")
        print()

        # If the worker responds "no" the worker must then enter the password: Shut%Down123
        # Once they do the while loop will stop, the file will close, and the program will end.
        if (workerInput == "no") :
            print("Once the correct password is entered, program will shutdown.")
            workerPass = input("What is the password? ")
            if (workerPass == "Shut%Down123") :
                print("Thank you for using eTipMaster.")
                fileInput.close()
                isThereMore = False

        # If the worker responds "yes" then an empty list, nthLine, is created
        # and the following data objects are converted to strings then
        # appended to the list
        elif (workerInput == "yes"):
            
            nthLine = []

            # Worker is prompted to record how many guests are in the party,
            # this data point is saved first as an integer, then appended as a string
            # to the list
            numGuests = int(input("How many guests are there in the party? "))
            nthLine.append(str(numGuests))

            # Worker is prompted to record how many cocktails that the party ordered,
            # this data point is saved first as an integer
            numCocktails = int(input("How many cocktails were ordered? "))
            nthLine.append(str(numCocktails))

            # Worker is prompted to record what was the number of the floor
            # that the party dined on, data point is saved as an integer
            numFloor = int(input("What was the number of the floor that the party dined on? "))
            nthLine.append(str(numFloor))

            # Worker is prompted to record what was the cost of the meal of the 
            # diner party without the tip, the data point is saved as a float
            costOfMeal = float(input("What was the cost of the meal without the tip? "))
            nthLine.append(str(costOfMeal))

            # Function calculateHeadCountTip is invoked, returns a float which is
            # saved, then appended to the list as a string like all other data points
            headTax = calculateHeadCountTip(numGuests)
            nthLine.append(str(headTax))

            # Function calculateFloorTip is invoked, returns a float which is saved
            floorTax = calculateFloorTip(numFloor, numGuests)
            nthLine.append(str(floorTax))

            # Function calculateCocktailDiscount is invoked, returns a float which is saved
            cocktailDiscount = calculateCocktailDiscount(numGuests, numCocktails, costOfMeal)
            nthLine.append(str(cocktailDiscount))

            # Function calculateTotalTip is invoked, returns a float which is saved 
            totalRaw = calculateTotalTip(headTax, cocktailDiscount, floorTax)
            nthLine.append(str(totalRaw))

            # Function roundTotalTip is invoked, returns a string
            roundedTip = roundTotalTip(totalRaw)
            nthLine.append(str(roundedTip))

            # After all nine data points have been appended to the list nthLine
            # as strings, a print statement is shown to screen detailing what
            # is the cost of the party's tip is.
            print("Your tip to be paid is $" + str(roundedTip))
            
            # Then the list, nthLine is converted to a string with the " | " 
            # character acting as the delimiter of the entries
            nthLine = (" | ").join(nthLine) + "\n"

            # The Text file "dailySpreadSheet.txt" is closed and
            # the changes to it are saved
            fileInput.write(nthLine)

# Main function is invoked
main()
