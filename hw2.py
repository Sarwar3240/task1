
#1. Write a program in Python to perform the following operation:
"""
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string."""
x= int(input("enter number: "))

if x % 3 == 0 and x % 5 == 0:
    print("Consultadd - python Training")

elif x % 3 == 0:
    print("Consultadd")

elif x % 5 == 0:
    print("python Training")

#2. Write a program in Python to perform the following operator based task:
"""Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action."""

print("choose your option:\n1 - Addition\n2 - Subtraction\n3 - Dividion\n4 - Multiplication\n5 - Average ")
x= eval(input("select the option from 1 to 5: "))
if x == 1:
    num1= int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    add = num1 + num2
    print(add)
    if add < 0:
         print("NEGATIVE")
elif x== 2:
   num1= int(input("enter a number: "))
   num2 = int(input("enter a number: "))
   subtraction = num1 - num2
   print(subtraction)
   if sub < 0:
        print("NEGATIVE")
elif x == 3:
   num1= int(input("enter a number: "))
   num2 = int(input("enter a number: "))
   division = num1 /num2
   print(division)
   if div < 0:
       print("NEGATIVE")
elif x == 4:
   num1= int(input("enter a number: "))
   num2 = int(input("enter a number: "))
   multiply = num1 * num2
   print(multiply)
   if multiply < 0:
       print("NEGATIVE")
elif x== 5:
   num1= int(input("enter a number: "))
   num2 = int(input("enter a number: "))
   average = (num1+num2)  /2
   print(average)
   if average < 0:
      print("NEGATIVE")
        
else: 
  print("please select the valid option.")


#3. Write a program in Python to implement the given flowchart:

a, b, c = 10, 20, 30
avg = (a+b+c)/3
print("average = ", avg)
if (avg > a and avg > b and avg > c):
    print("average is Higher than a,b,c")
if (avg > a and avg > b):
    print("average is Higher than a and b")
if (avg > a and avg > c):
    print("average is Higher than a and c")
if (avg > b and avg > c):
    print("average is Higher than b and c")
if (avg > a):
    print("average is Higher than a")
if (avg > b):
    print("average is Higher than b")
if (avg > c):
    print("average is Higher than c")

# 4. Write a program in Python to break and continue if the following cases occurs
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”
x= int(input("enter a number: "))
a=0
while a < x:
  if x < 0:
        print("it's Over.")
        break
   elif x > 0 :
        print("Good Going.")
        continue

#5.. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.

for x in range (2000,3201):
    if x % 7 == 0 and  x % 5 !=0:
        print(x)

#6. What is the output of the following code examples?
x=123 
for i in x: 
    print(i)
# answer: error int object not iterable

i = 0
while i < 5: 
    print(i) 
    i += 1 
    if i == 3: 
        break
    else: 
        print('error')
# answer:0
"""
error
1
error
2
"""
count = 0
while True: 
    print(count) 
    count += 1 
    if count >= 5: 
        break
# answer : 0,1,2,3,4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i)

#8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters. 
# Sample input: consul72 
# Expected output: Letters 6 Digits 2

sentence=input("please enter anything: ")
def letterAndNumbers(Sentence):
    lettercount=Numcount=0

    for i in sentence:
        if i.isdigit():
            Numcount+=1
        elif i.isalpha():
            lettercount+=1
    return lettercount, Numcount

letters, Number= letterAndNumbers(sentence)

print("number of letters: ", letters)
print("number of Numbers: ", Number)

# 9. Read the two parts of the question below: 
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two
#variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct
#number)
import random

number = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
#such as
#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
#correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”

import random
i = 1
while i <=5:
    guess = random.randint(1,10)
    print("the lucky number is: ", answer)
    number= int(input("Guess the lucky number from 1 to 10: "))
    if number == guess:
        print("good guess")
    else:
        print("try again")
    if i == 5:
        print("game over")
    i +=1

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”

import random
i = 1
while i <=5:
    guess = random.randint(1,10)
    print("the lucky number is: ", answer)
    number= int(input("Guess the lucky number from 1 to 10: "))
    if number == guess:
        print("Good guess!")
        break
    else:
        print("Sorry but that was not very successful.")
    if i == 5:
        print("game over")
    i +=1
