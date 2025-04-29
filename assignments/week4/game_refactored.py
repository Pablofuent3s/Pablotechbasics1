# This is the game of life!
## I always think about having a healthy lifestyle. This game can be a good reminder!

import time

# Constants
MAX_AGE = 120
MIN_AGE = 0
MAX_SCREEN_TIME = 24

def pause(seconds=1.5):
    time.sleep(seconds)

def get_valid_age() -> int:
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

def get_place() -> str:
    place = input("Enter your place of living (by continent): ").lower()
    if place == "europe":
        print("The average life expectancy in Europe is 74 years for men and 81 for women!")
    elif place == "oceania":
        print("The average life expectancy in Oceania is 77 years for men and 83 for women!")
    else:
        print("I recommend you retire in Europe, Asia or Oceania, where life expectancy is higher.")
    return place

def get_lifestyle() -> str:
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

def get_screen_time() -> float:
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

def scene_summary(age, place, lifestyle, screentime):
    print(f"You are {age} years old, live in {place}, have a {lifestyle} lifestyle, and spend {screentime} hours on your phone daily.")
    pause(2)
    print("Thank you for playing! By having less time on your phone and a more active lifestyle, you can live your life to the fullest!")

def main():
    print("Welcome to the Game of Life! Let's see how you're living...")
    pause()

    age = get_valid_age()
    pause()

    place = get_place()
    pause()

    lifestyle = get_lifestyle()
    pause()

    screentime = get_screen_time()
    pause()

    scene_summary(age, place, lifestyle, screentime)

main()