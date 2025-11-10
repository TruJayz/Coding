# Question 1
# Build a program that determines if a student has submitted their class work 
# and homework assignment. The program should use an operator that allows 
# for evaluating 2 conditions and determining if the conditions are true 
# or false , then answer the following questions: 

# Question 2
# Create a function that will take in a string as an argument and output 
# that string in reverse order.

# hint: look into string reverse in w3schools

# Question 3
# Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 
# Your program should also give the user information on if their guess 
# is close to the correct number. If the guess is above the correct number 
# it should tell the user it is too high and try again. 
# If the guess is below the number, it should tell the user it is too low, 
# it should tell them it is too low and to guess again. Once the user gets 
# it correct the program should congratulate them, stop, and tell them how 
# many attempts they made.



def CheckAssignmentSub():

 
   'ClassWorkSubmitted' = input("Has the class work been submitted? (yes/no): ").lower()
  'homeworkSubmitted' = input("Has the homework been submitted? (yes/no): ").lower()

 
  ClassWorkSubmitted =  ClassWorkSubmitted == 'yes'
  homeworkSubmitted = homeworkSubmitted == 'yes'

  
  if ClassWorkSubmitted and homeworkSubmitted:
    print("The student has submitted both the class work and the homework.")
  else:
    print("The student has not submitted all assignments.")

CheckAssignmentSub()



2#



txt = "Honkai Star Rail is the greatest game ever"[::-1]
print(txt)





3#

       def randomNumber():
          correctNumber = 7
          userGuess = input('plese guess a number')
          while userGuess != correctNumber:
             userGuess = int(input('please guess a number: '))
             if userGuess > correctNumber
             print('your guess is to higth')

          else:
             print('your guess is to low')
             userGuess = int(input("please guess a number: "))

          else:
          print("congrats, you got the correct number! ")


            randomNumber()
