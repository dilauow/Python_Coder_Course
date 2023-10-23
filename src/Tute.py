"""Write a Python program that %takes a number% as input and print the all the
    even numbers from 0 to that number."""

# This question requires the student to:

# Understand the concept of Python data types, specifically numbers.
# Use a loop to iterate from 1 to the input number.
# Use a conditional statement to check if each number is even.
# Use a variable to store the sum of the even numbers.
# Use a function to define the logic for calculating the sum of the even numbers.


#take a input


#user is giving us 10


def returnEvenNumbers(num):

    for i in range(1,num + 1):
        if i % 2 == 0:
            print(i)





runTheProgram  = True
while runTheProgram==True:
    userInput = int(input("Enter a number: "))
    returnEvenNumbers(userInput)
    shouldRuntheProgram = input("Do you want this pogram to continue running.If so type Y. If not type anything: ")
    if(shouldRuntheProgram=="Y"):
        print("Still Running")
    else:
        runTheProgram= False





















# def printEvenNumbers(num):
#     for i in range(1, num + 1):
#         if i % 2 == 0:
#             print(i)
#         else:
#             pass
#
#
#
#
# runtheLoop = True
# while runtheLoop==True:
#     answer = int(input("Enter the number: "))
#     printEvenNumbers(answer)
#     endTheLoop = input("Should we end the loop. If we should end, type F, if not type anything")
#     if(endTheLoop == "F"):
#         runtheLoop= False
