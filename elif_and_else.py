# If statments is our original condition, we can use it to control the flow of our program
# elif allows us to chain additinal conditions/assertions, with their own corrresponding code blocks

# the flow of the if/elif chain reads frin tio down, and as soon as a condition staemen evaluates to True, the code block and the rest of the condition are skipped

money = 15
# chained together with the initial "if" statement
if money >= 50:
    print("We can have a steak dinner!")
elif money >= 20:
    print("Italian sounds like a good choice")
elif money >= 10:
    print("Let's grab some Chipotle!")

print("="*50)

money = 15
# is not chained together (the space between each is ran seperatedly)
if money >= 50:
    print("We can have a steak dinner!")

elif money >= 20:
    print("Italian sounds like a good choice")

elif money >= 10:
    print("Let's grab some Chipotle!")

print("="*50)

# the order in whichyouconstruct matters as well - following code after True statement will not be executed
money = 75

if money >= 50:
    print("We can have a steak dinner!")
elif money >= 20:
    print("Italian sounds like a good choice")
elif money >= 10:
    print("Let's grab some Chipotle!")

print("="*50)

money = 75
# is not chained together (the space between each is ran seperatedly)
if money >= 50:
    print("We can have a steak dinner!")

elif money >= 20:
    print("Italian sounds like a good choice")

elif money >= 10:
    print("Let's grab some Chipotle!")

print("="*50)

# Else statements are essentially a default condition
# They dont have a specific condition attached to them, they are used when none of the preceding conditions are met

money = 8

if money >= 50:
    print("We can have a steak dinner!")
elif money >= 20:
    print("Italian sounds like a good choice")
elif money >= 10:
    print("Let's grab some Chipotle!")
else:
    print("Maybe I should just cook at home...") # else statement is basically used a catch all ( if none of the other conditions are true nothing would print which makes for a base user experiance) 

