# If statement 

# syntax
# if (condition):
#    indented_code block

weather = "rainy"

assertion = (weather == "sunny")
print(assertion)

print("="*50)

if weather == "sunny": # if statements are always looking for a true condition/assertion
    print("let's have a picnic!")

torch_lit = True 

if torch_lit:
    print("My path is clear!") 

if True:
    print("This statement will always be true") # I placed a boolean value of True for this statement so it will always run


# example of "if" statement that is dynamic and gives user options say a if they were playing a text game

# user_input = input("Would you like to explore the cave or explore the spooky path? ")
# if user_input == 'cave':
#     print ("Oooooh you just entered a dark cave !! ")
# elif user_input == 'spooky path':
#     print("This path is spooky but you bravely charge forward")
# elif user_input == 'lake':
#     print("The lake sounds like a nice place to relax")
print("="*50)

# If statements check for a True condition/assertion, if it's True they execute the indented code block.
# COMPUND CONDITIONAL STATEMENTS USING "and" AND "or" logical operator 

#--- and : requires both conditions to be True in orer to execute the indented code block

gold_coins = 10
silver_coins = 50

if (gold_coins > 5) and (silver_coins > 30):
    print("You have enough coins to buy a magical item!") # both conditions have to be true in order for this statement to run


#--- or : requires at least one of the conditions to be True in order to execute the indented code block

if (gold_coins > 5) or (silver_coins > 55):
    print("You have enough coins to buy a magical item!") # either one or the other conditions has to be true in order for this statement to run
print("="*50)

# using "and" and "or" together 

caffinated = True
prepared_lvl = 11
confidence = 70

# How ready am I to teach class?

#True
if (caffinated and prepared_lvl > 6) or (confidence > 60):
    print("I am ready to teach class!") #True
else:
    print("I am not ready to teach class yet.") #False

#False
if (caffinated and prepared_lvl > 12 ) or (confidence > 80):
    print("I am ready to teach class!") #True
else:
    print("I am not ready to teach class yet.") #False

print("="*50)
# "not" operator

# By incorporating the "not" operator, we can check for false condition

busy = False
if not busy:
    print("Nice time to relax") # not busy is its on condition 

# if False:
#     run code ( basically what the code block is doing)

print("="*50)
# 









