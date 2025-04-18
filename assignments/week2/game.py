import time

print("Welcome to the game of life! You will get to know how are you living.")
time.sleep(1.5)

print("Let's see how old you are...")
time.sleep(1.5)

while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        if 0 <= age <= 120:
            break
        else:
            print("Please enter an age between 0 and 120.")
    else:
        print("That's not a valid number.")

print("Where do you live?")
place = input("Enter your place of living (by continent): ").lower()
if place == "europe":
    print("The average life expectancy in Europe is 74 years for men and 81 for women!")
elif place == "oceania":
    print("The average life expectancy in Oceania is 77 years for men and 83 for women!")
else:
    print("I recommend you retire in Europe, Asia or Oceania, where life expectancy is higher.")
time.sleep(1.5)

print("What's your lifestyle: more sedentary or more active?")
lifestyle = input("Enter your type of lifestyle: ").lower()

if lifestyle == "more sedentary":
    print("Why?")
    time.sleep(1)
    reason = input("Tell me the reason: ")
    if reason == "work":
        print("You should work out! Even riding a bike to work or taking the stairs in your routine will raise your life expectancy!")
    else:
        print("You should work out! Even riding a bike to work or taking the stairs in your routine will raise your life expectancy!")
elif lifestyle == "more active":
    print("Great! Working out can raise your life expectancy by 10 years with a good diet based on quality food.")
else:
    print("Hmm, I didn't understand that. Try typing 'more sedentary' or 'more active'.")
time.sleep(1.5)

print("How much time do you spend on your phone daily?")
while True:
    screentime_input = input("Enter your screentime in hours (e.g., 3.5): ")
    try:
        screentime = float(screentime_input)
        if 0 <= screentime <= 24:
            break
        else:
            print("Please enter a number between 0 and 24.")
    except ValueError:
        print("That's not a valid number.")

if screentime <= 2:
    print("You are living life to the fullest!")
else:
    print("You should have less screentime! You're wasting time of your life.")
time.sleep (2)
print("You are", age, "years old and live in", place, "and you are", lifestyle, "and you spend", screentime, "hours on your phone daily.")
time.sleep (2)
print ("Thank you for playing! By having less time on your phone and a more active lifestyle, you can live your life to the fullest!.")