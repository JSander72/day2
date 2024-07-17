
# Inline if statements (ternary operator) are simply away to write if steatements in a single line of code


# syntax
# <True return> if <condition> else <False return>

candy_jar = "empty"

print("It's candy time!" if candy_jar == "full" else "time to hit up Mr. Wonka") 

print("="*50)

# ternary operator with "and" 

candy_jar = "empty"
sweet_tooth = True

print("It's candy time!" if candy_jar == "full" and sweet_tooth else "Who needs candy anyway?") 

# ternary operator with "or"

candy_jar = "empty"
sweet_tooth = False

print("It's candy time!" if candy_jar == "full" or sweet_tooth else "Who needs candy anyway?")

print("="*50)

day = "tuesday"
print("It's the weekend!") if (day == "saturday") or (day == "sunday") else print("Boooooo it's not the weekend!")

print("="*50)


