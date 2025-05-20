# Watch what you eat!
## this games treats inventory as what do you have in your house and what you eat. Keep yourself healthy!
### AI Tool ChatGPT helped be debugging and understand my mistakes.


# --- Game settings
import time
inventory = []
items_in_room = [
    {"name": "American Burger", "type": "food", "description": "Yummy, but a very big intake of calories. -10 health", "health": -10},
    {"name": "Fruits", "type": "food", "description": "Healthy and good!. +2 health", "health": +2},
    {"name": "legumes", "type": "food", "description": "big intake of proteins. +4 health", "health": +4},
    {"name": "Pizza", "type": "food", "description":
        "A delicious pizza. Suitable for a special day of the week. -7 health", "health": -7},
    {"name": "Bread", "type": "food", "description": "A delicious bread. Suitable for breakfast. +1 health", "health": +1},
    {"name": "Water", "type": "drink", "description": "A basic and healthy drink. Suitable for a long walk. +3 health", "health": +3},
    {"name": "Coffee", "type": "drink", "description": "A basic and energetic drink. Boosts your energy level. +1 health", "health": +1},
    {"name": "Energy Drink", "type": "drink",
     "description": "A big intake of energy. Boosts your energy level big time with a risk. -3 health", "health": -3},

] # length shall be larger than max inventory size if there is only one room

MAX_INVENTORY_SIZE = 5
MAX_HEALTH = 100
MIN_HEALTH = 0
starting_health = 50
WAITING_TIME = 1.5
win_condition = 100
lose_condition = 0
health = starting_health

# --- Functions ---

def intro():
    print("Welcome to the Healthy Meal Game!")
    time.sleep(WAITING_TIME)
    print("Your goal is to reach 100 health by choosing healthy foods and drinks.")
    time.sleep(WAITING_TIME)
    print("Start by typing 'look' to see the available items.")
    print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit, check")
    time.sleep(WAITING_TIME)
    print(f"Starting health: {starting_health}")

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if not inventory:
        print("You don't have any items in your inventory.")
    else:
        print("You have:")
        for item in inventory:
            print(f"- {item['name']}")

def show_room_items():
    # list all items in current room
    if not items_in_room:
        print("There are no items left in the room.")
        return

    print("\nItems in the room:")
    for item in items_in_room:
        print(f"- {item['name']} ({item['type']}): {item['description']}")
    print("\nTip: Use 'pickup [item name]' to add it to your inventory.")

def pickup(item_name):
    # pick up an item from the room if inventory limit is not met yet
        global inventory, items_in_room  # Modify existing inventory
        for item in items_in_room:
            if item["name"].lower() == item_name.lower():
                if len(inventory) < MAX_INVENTORY_SIZE:
                    inventory.append(item)
                    items_in_room.remove(item)
                    print(f"You picked up {item['name']}.")
                    return
                else:
                    print("Your inventory is full. You can't pick up any more items.")
                    return
        print(f"{item_name} not found in the room.")

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped {item['name']}.")
            return
    print("Item not found in inventory.")

def use(item_name):
    # Ex: use the item differently depends on the type
    global health
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            health += item["health"]
            health = max(0, min(health, MAX_HEALTH))  # Make it between 0 (MIN_HEALTH) and 100 (MAX_HEALTH)
            print(f"You used {item['name']}. {item['description']}")
            print(f"Current health: {health}")
            inventory.remove(item)
            items_in_room.append(item)
            return
    print("You don't have that item in your inventory.")

def examine(item_name):
    description = inventory.get(item_name.lower())
    if description:
        print(f"{item_name.capitalize()}: {description}")
    else:
        print(f"You don't have an item called '{item_name}'.")

def check_health():
    global health
    if health <= MIN_HEALTH:
        print("You lost! Your health dropped to 0.")
        return "lose"
    elif health >= MAX_HEALTH:
        print("Congratulations! You reached maximum health and won the game!")
        return "win"
    return "continue"

# --- Game Loop ---

def game_loop():
    print("Welcome to the Healthy Inventory Game!")
    print("Type 'help' for a list of commands.")
    intro()

    while True:
        command = input("\n> ").strip().lower()

        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit, check")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:].strip()
            pickup(item_name)
        elif command.startswith("drop "):
            item_name = command[5:].strip()
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:].strip()
            use(item_name)
            check = check_health()
            if check in ["win", "lose"]:
                break
        elif command.startswith("examine "):
            item_name = command[8:].strip()
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()

