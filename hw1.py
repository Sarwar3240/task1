Number and Varibales
"""
# Q1.Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
 num, v_bol, name = 10, false, "sarwar"

# # 2. Create a variable of type complex and swap it with another variable of type integer.
x = 1 + 2j
x=int(x)

#3.Swap two numbers using a third variable and do the same task without using any third variable.
x, y = 1, 2
z = x+y
# without the 3rd var
x=x+y
y=x-y
x=x-y

# #4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
#python_2x 
x=raw_input("please enter anything you would like: ")
print(x)

# python3.x
x = input("please enter anything you would like: ")
print(x)

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

num_1= int(input("enter a number in between 1-10: "))
num_2= int(input("enter another number in between 1-10: "))
z = num_1+num_2
result = z + 30
print(result)

#6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
a, x, y, z = 2, 2.5, "hello", true
print(type(a), type(x), type(y), type(Z))


# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# (Refer: https://capitalizemytitle.com/camel-case/)

UpCam = "upper camel case variable"
lowCam = "lower camel case variable"
s_case = 'snake case varibale'

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?
#it does change the value because python will recognize the most recent value asiigned to the variable.
