import random
import time
# inputs
width = int(input("how many width blocks do you want? "))
height = int(input(" how many height blocks do you want? "))
symbol = input("which symbol do you want to use? (pick from: *, #, +, @) ")
name = input("Write your name (it can be anything): ")
# building the blocks
block = []
for row in range(5):
    line = ""
    for col in range(10):
        if row == 2 and col == 3 and random.random() > 0.5 and name:
            letter = random.choice(name)
            line += letter
        else:
            line += symbol
    block.append(line)
print("\n🎨 Generating your custom ASCII pattern...\n")

for y in range(height):
    for i in range(len(block)):
        for x in range(width):
            print(block[i], end='  ')
        print()
    time.sleep(0.5)
