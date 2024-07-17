# nested if statements

# We can have nested if statements inside other if statements. This can make the code more readable and maintainable

# activity of the day

weather = "sunny"
friends = 5

if weather == "sunny": # outer condition
    #inner staement
    if friends >= 6:
        print("Let's play vollyball!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think I'll play golf...all by my lonesome")
        elif friends < 5:
            print("the", friends, "of s hould play golf")
else:
    print("Lets's go to the movies")


print("="*50)

weather = "sunny"
friends = 3 # friends under 6, 5, but more then 1, 0, or negative

if weather == "sunny": # outer condition
    #inner staement
    if friends >= 6:
        print("Let's play vollyball!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think I'll play golf...all by my lonesome")
        elif friends < 5:
            print("the", friends, "of s hould play golf")
else:
    print("Lets's go to the movies")

print("="*50)

weather = "sunny"
friends = 0 # no frineds 

if weather == "sunny": # outer condition
    #inner staement
    if friends >= 6:
        print("Let's play vollyball!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think I'll play golf...all by my lonesome")
        elif friends < 5:
            print("the", friends, "of s hould play golf")
else:
    print("Lets's go to the movies")

print("="*50)

weather = "sunnny" #sunny misspelled in the example
friends = 5

if weather == "sunny": # outer condition
    #inner staement
    if friends >= 6:
        print("Let's play vollyball!")
    elif friends == 5:
        print("Let's play frisbee!")
    else:
        if friends == 1:
            print("I think I'll play golf...all by my lonesome")
        elif friends < 5:
            print("the", friends, "of s hould play golf")
else:
    print("Lets's go to the movies")

