import stdio
import sys

answer = ""
print("You woke up in an unfamiliar place, no longer in your bed. You're surrounded by a vicious green substance as it seems like a portal or dimension closing behind you.")
print("The substance seemingly dries instantly off of you. The air around you seems heavier than usual, even has a different noticeable smell to it not unpleasant, just noticeably different.")
print("You wander around thinking this is some kind of elaborate prank being played on you. Unfortunately, it starts to rain, but in no normal way at all. It's a maroon almost crimson color.")

name = input('Enter your name: ')
print(f'Greetings {name}! Dont get lost in the fog 🙃')

directions = ["forward", "backward", "left", "right"]

answer = input("Do you want to play? (y/n)? 👾 ")

if answer.lower().strip() == "y" or answer.lower().strip() == "yes":
   stdio.write("Playing...\n")
elif answer.lower().strip() == "n" or answer.lower().strip() == "no":
   stdio.write("Not playing...awww try again next time.\n")
   quit()

answer = input("You've reached a crossroad, would you like to turn left or right?").strip().lower()

if answer == "left":
    answer = input("Turning left..., after walking for a while you encountered a monster at what appears to be a gas station. Would you like to attack or run??!").strip().lower()
    if answer in ["attack", "attacking", "attacking monster"]:
        stdio.write("Attacking...\n")
        stdio.write("That wasn't the smartest idea...., you lost! ☠️\n")
    else:
        stdio.write("Running...\n")
        stdio.write("Good choice, look who gets to live another day! 😇\n")
        
        answer = input("You approach two vehicles in a field of grass with a purplish color, one resembling a car and another resembling a bike of some sort. Which would you like to take? (car/bike)").strip().lower()

        if answer == "bike":
            stdio.write("Unfortunately, You don't know how to ride a bike.....Game over!\n")
        elif answer == "car":
            stdio.write("You were able to make the car run, you leave this land. You won!\n")

elif answer == "right":
    stdio.write("You begin walking aimlessly to the right and fall into an endless abyss of fog...it seems you cannot continue in this direction.\n")
    answer = input("You find yourself lost in the fields of fog. Would you like to continue? (Y/N)").strip().lower()
    
    if answer == "y" or answer == "yes":
        stdio.write("Continuing...\n")
    elif answer == "n" or answer == "no":
        stdio.write("Not playing...awww try again next time.\n")
        quit()
    
    while answer not in directions:
        print("------------------------------")
        answer = input("Which direction would you like to go? (forward/left/right/backward)").strip().lower()

        if answer == "forward":
            print("Moving forward...⬆️")
            answer = input("You find another portal made of the same substance you came to this place in. You walk through and find yourself waking up in your bed like nothing ever happened. You made it back home safely, congrats. You won!")
        elif answer == "left":
            print("Moving left...⬅️")
            answer = input("Turning left..., after walking for a while you encountered a monster at what appears to be a gas station. Would you like to attack or run??!").strip().lower()
            if answer in ["attack", "attacking", "attacking monster"]:
                stdio.write("Attacking...\n")
                stdio.write("That wasn't the smartest idea...., you lost! ☠️\n")
            else:
                stdio.write("Running...\n")
                stdio.write("Good choice, look who gets to live another day! 😇\n")
                
                answer = input("You approach two vehicles in a field of grass with a purplish color, one resembling a car and another resembling a bike of some sort. Which would you like to take? (car/bike)").strip().lower()
                
                if answer == "bike":
                    stdio.write("Unfortunately, You don't know how to ride a bike.....Game over!\n")
                elif answer == "car":
                    stdio.write("You were able to make the car run, you leave this land. You won!\n")
        elif answer == "right":
            print("Moving right...➡️ You find yourself deeper into the abyss of fog. However, the fog seems thinner somehow... Wait, you see something glimmering in the distance??!")
            answer = input("Would you like to interact with the object? (Y/N)").strip().lower()
            if answer == "y" or answer == "yes":
                stdio.write("Continuing...\n")
            elif answer == "n" or answer == "no":
                stdio.write("Not playing...awww try again next time.\n")
                quit()
        elif answer == "backward":
            print("Moving backward...⬇️ You traverse through the abyss of fog... you find an empty saloon and it seems to be safe with no creatures in sight. It seems safe enough to camp here for the night.")
        else:
            print("Invalid Response: Please enter either forward, left, right, or backward. ↕️ ↔️")

        if answer == "y" or answer == "yes":
            stdio.write("Continuing...\n")
        elif answer == "n" or answer == "no":
            stdio.write("Not playing...awww try again next time.\n")
            quit()

else:
    stdio.write("Invalid answer, you lost!\n")
