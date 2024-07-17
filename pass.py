# Pass statement is a placeholder keyword, or a temporary standin for a codeblock.

feeling ="fantastic"

if feeling == "sick":
    pass # placeholder - nothing happens until we decide what we want to go in here
elif feeling == "decent":
    pass
elif feeling == "good":
    pass
else:
    print("Wow, I'm feeling greeat, let's go running")


print("="*50)

user_input = input("Where doyou wanna go next?")

if user_input == "cave":
    pass # expand on optiions for cave exploration
elif user_input == "left fork":
    pass # options for what happends if you choose left fork
elif user_input == "lake":
    pass # options for what happens if you choose the lake
else:
    print("chose a valid path")

