age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote")
    else:
        print("You are must be a citizen to vote")
else:
    print("You are not eligible to vote yet")