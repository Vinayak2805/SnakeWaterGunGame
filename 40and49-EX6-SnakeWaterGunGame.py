import random
print("Play snake, water, gun game with computer")

yourScore = 0
chances = 10

while (chances>0):
    choices = ("s, w, g")
    c = random.choice(choices)
    inp = input("Enter s for snake\nEnter w for water\nEnter g for gun\n") 
    chances = chances-1
    if inp == "s":
        if c == "w":
            print("You win! Computer's choice was water")
            print("Chances left", chances)
            yourScore = yourScore+1
            continue
        elif c == "g":
            print("You lose! Computer's choice was gun")
            print("Chances left", chances)
            continue
        elif c == "s":
            print("Match tied! Computer's choice was also snake")
            print("Chances left", chances)
            continue

    elif inp == "w":
        if c == "g":
            print("You win! Computer's choice was gun")
            print("Chances left", chances)
            yourScore = yourScore+1
            continue
        elif c == "s":
            print("You lose! Computer's choice was snake")
            print("Chances left", chances)
            continue
        elif c == "w":
            print("Match tied! Computer's choice was also water")
            print("Chances left", chances)
            continue

    elif inp == "g":
        if c == "s":
            print("You win! Computer's choice was snake")
            print("Chances left", chances)
            yourScore = yourScore+1
            continue
        elif c == "w":
            print("You lose! Computer's choice was water")
            print("Chances left", chances)
            continue
        elif c == "g":
            print("Match tied! Computer's choice was also gun")
            print("Chances left", chances)
            continue
            
    else:
        print("Please enter a valid input")
        continue

print("Game Over")
print("Your score:", yourScore)
print("Thanks for playing")