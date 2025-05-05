# This is the game of life!
## I always think about having a healthy lifestyle. This game can be a good reminder!
## ChatGPT assisted me in understanding global variables and debugging various syntax mistakes (e.g: function structures)
import time

# Constants
MAX_AGE = 120
MIN_AGE = 0
MAX_SCREEN_TIME = 24

# Creation of functions and time delays
def pause(seconds=1.5):
    time.sleep(seconds)
# age indexing with the restraints kept in mind
def valid_age() -> int:
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            age = int(age_input)
            if MIN_AGE <= age <= MAX_AGE:
                return age
            else:
                print(f"Please enter an age between {MIN_AGE} and {MAX_AGE}.")
        else:
            print("That's not a valid number.")
# Knowing where does the user live to choose between locations
def location() -> str:
    place = input("Enter your place of living (by continent): ").lower()
    if place == "europe":
        print("The average life expectancy in Europe is 74 years for men and 81 for women!")
    elif place == "oceania":
        print("The average life expectancy in Oceania is 77 years for men and 83 for women!")
    else:
        print("I recommend you retire in Europe, Asia or Oceania, where life expectancy is higher.")
    return place

# You enter your lifestyle by thinking how active you are (how often you go make exercise)
def lifestyle() -> str:
    lifestyle = input("Enter your type of lifestyle (rather sedentary or rather active): ").lower()
    if lifestyle == "rather sedentary":
        print("Why?")
        pause(1)
        reason = input("Tell me the reason: ")
        print("You should work out! Even riding a bike to work or taking the stairs in your routine will raise your life expectancy!")
    elif lifestyle == "rather active":
        print("Great! Working out can raise your life expectancy by 10 years with a good diet based on quality food.")
    else:
        print("Hmm, I didn't understand that. Try typing 'rather sedentary' or 'rather active'.")
    return lifestyle
# I try to use the phone as little as I can. My goal is to go under 2 hours a day at least once every week.
def screen_time() -> float:
    while True:
        screentime_input = input("Enter your screentime in hours (e.g., 3.5): ")
        try:
            screentime = float(screentime_input)
            if 0 <= screentime <= MAX_SCREEN_TIME:
                if screentime <= 2:
                    print("You are living life to the fullest!")
                else:
                    print("You should have less screentime! You're wasting time of your life.")
                return screentime
            else:
                print(f"Please enter a number between 0 and {MAX_SCREEN_TIME}.")
        except ValueError:
            print("That's not a valid number.")
# summary of the past functions
def summary(age, place, lifestyle, screentime):
    print(f"You are {age} years old, live in {place}, have a {lifestyle} lifestyle, and spend {screentime} hours on your phone daily.")
    pause(2)
    print("Thank you for playing! By having less time on your phone and a more active lifestyle, you can live your life to the fullest!")
# running the main function
def main():
    print("Welcome to the Game of Life! Let's see how you're living...")
    pause()

    age_var = valid_age()
    pause()

    place_var = location()
    pause()

    lifestyle_var = lifestyle()
    pause()

    screentime_var = screen_time()
    pause()

    summary(age_var, place_var, lifestyle_var, screentime_var)

main()