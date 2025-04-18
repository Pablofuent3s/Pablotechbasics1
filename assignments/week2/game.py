import time

print("Welcome to the game of life!")
time.sleep(1.5)

print("Let's see how old you are...")
time.sleep(1.5)

number = int(input("Enter your age: "))
time.sleep(1)

if number <= 0:
    print("You are not alive yet!")
elif number <= 2:
    print("You are a baby! How can you manage Python?")
elif number <= 10:
    print("Hello little friend! Do you like computers?")
elif number <= 20:
    print("Hey dude! So you like programming? You can be a good coder if you start young.")
elif number <= 50:
    print("Wow! You are in your prime!")
elif number <= 99:
    print("An elder wise coder! Do you know Tim Berners-Lee?")
elif number == 100:
    print("Wow! A centenary user! Happy 100th birthday!")
elif number <= 120:
    print("You need to contact the Guinness World Records! You're SO OLD! I respect that.")
else:
    print("That's not a human age number!")
time.sleep (1)

print ("where do you want to retire?")
place = input("Enter your retirement place (by continent): ")
if place == Europe:
    print (" The average life expectance in Europe is 74 years for men and 81 for women!")
elif place == Oceania:
    print ("The average life expectance in Europe is 77 years for men and 83 for women!")
else:
    print ("I reccomend you to retire in Europe or Oceania! they have better life expectancy")

time.sleep (1.5)
