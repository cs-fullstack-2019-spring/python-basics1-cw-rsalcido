# Problem 1:
#
# Create a function with two variables. One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.

def main():
#     problem1()
#      problem2()
#       problem3()
        problem4()
# def problem1():
#     x = str("My name is ")
#     y = str("Ricardo Salcido")
#     print(x +y )
#
#
#
#
# if __name__ == '__main__':
#     main()

# Problem 2:
#
# Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.

# def problem2():

#     x = int(input("Please enter the extra credit you have earned. "))
#     if (x<5):
#         print("That's not enough extra credit.")
#     elif (x>5):
#         print("That's too much extra credit")
#
#
#
# main()

# Problem 3:
#
# Create a function to ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
#

# def problem3():
#     x = input("Enter your password")
#     y = input("For your safety, please re-enter your password")
#     if (x==y):
#         print("Correct")
#
#
# main ()


# Problem 4:
#
# Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”
#

def problem4():

    x= int(input("Pick your first card."))
    y= int(input("Pick your second card"))
    if (x+y >21):
        print("BUST")
    elif(x+y == 21):
        print(str("BlackJACK!"))
    elif (x+y <21):
        print(str("The total is")) + int(input(x+y))

main ()