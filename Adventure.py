class Game:
    def __init__(self):
        # Dictionary of rooms

        #SP23-BAI-023
        self.rooms = {
    "Entrance": {
        "description": "You stand before the towering gates of the ancient castle, its dark stone walls looming above. The grand hall lies to the north, waiting beyond the dimly lit corridor.",
        "exits": {"north": "Grand Hall"},
        "items": {}
    },
    "Grand Hall": {
        "description": "You have entered the Grand Hall, a vast space with towering pillars. To the north, a majestic throne gleams under faint light. An ornate tapestry hangs on the eastern wall along a sword mounted, and to the west, a dark corridor leads to other rooms.",
        "exits": {"south": "Entrance", "west": "Corridor"},
        "items": {
            "north": {"name": "Throne", "can_be_taken": False, "usable": False, "description": "An intricately carved throne, glinting with gold and jewels, it emanates authority."},
            "south": None,
            "east": [
                {"name": "Tapestry", "can_be_taken": False, "usable": True, "description": "The ornate tapestry hides a small lever behind its intricate folds, awaiting discovery."},
                {"name": "Sword", "can_be_taken": True, "usable": False, "description": "A gleaming sword mounted on the wall, its sharp blade catching the faint light. It looks ready to be taken."}
            ],
            "west": None
        }
    },
    "Corridor": {
        "description": "You have entered the dimly lit corridor, flickering torches illuminate the stone walls. To the west lies the Council Room, to the east the Library, while ahead leads to the basement on the right and a staircase spirals up on the left, inviting you to explore the castle's secrets.",
        "exits": {"south": "Grand Hall", "east": "Library", "west": "Council Room", "northeast": "Basement", "northwest" : "Upstairs"},
        "items": {}
    },
    "Council Room": {
        "description": "You have entered the Council Room. At the center lies a large oak table with a strategy board carefully placed on top, suggesting plans of conquest or defense. The fireplace to the west crackles softly, casting a warm glow over the room. To the east, a bronze statue of a knight stands, frozen in a heroic pose, its eyes seemingly watching over the room",
        "exits": {"south": "Corridor"},
        "items": {
            "north": [
                {"name": "Conference table", "can_be_taken": False, "usable": False, "description": "The large conference table holds a detailed strategy board, hinting at past discussions and battles planned."},
                {"name": "Board game", "can_be_taken": False, "usable": True, "description": "The board lies open on the table, but a few metal pieces are missing from the set."}
            ],
            "south": None,
            "east": {"name": "Bronze statue", "can_be_taken": False, "usable": False, "description": "A bronze statue of a knight stands silently, offering no further use."},
            "west": {"name": "Fireplace", "can_be_taken": False, "usable": False,"description": "A warm but otherwise ordinary fireplace crackles softly."}
        }
    },
    "Library": {
        "description": "You have entered the library. A dusty haven filled with ancient tomes, an open book glows invitingly on a table to the north, accompanied by an old letter beside it. A ladder leans against the west shelf, and a stunning landscape painting adorns the east wall.",
        "exits": {"south": "Corridor"},
        "items": {
            "north": [
            {"name": "Table", "can_be_taken": False, "usable": False, "description": "A sturdy table holds an ancient, glowing book."},
            {"name": "Book", "can_be_taken": True, "usable": True, "description": "An old book lies open, its pages glowing with mysterious light."},
            {"name": "Letter", "can_be_taken": False, "usable": True, "description":  "A crumpled letter rests beside the glowing book."}
        ],
        "south": None,
            "east": {"name": "Painting", "can_be_taken": False, "usable": False},
            "west": [
                {"name": "Shelf", "can_be_taken": False, "usable": False, "description": "A tall, dusty shelf filled with ancient books."},
                {"name": "Ladder", "can_be_taken": False, "usable": True, "description": "A sturdy wooden ladder leans against the tall west shelf."}
            ]
        }
    },
    "Basement": {
        "description": "You are in basement. A shadowy space with stone walls; the armory lies to the west, brimming with weapons, while the kitchen to the east fills the air with savory aromas. To the north, a heavy door conceals a locked dungeon, shrouded in mystery.",
        "exits": {"south": "Corridor", "east": "Kitchen", "west": "Armory"},
        "items": {}
    },
    "Kitchen": {
        "description": "A lively space filled with the scent of spices, featuring a shelf of three glowing potions to the north, a tall fridge to the east, and a simmering cauldron over an open flame to the west.",
        "exits": {"south": "Basement"},
        "items": {
            "north": {"name": "Potions", "can_be_taken": True, "usable": True, "description": "Three glowing potions sit on a high shelf, each radiating a faint light."},
            "south": None,
            "east": {"name": "Fridge", "can_be_taken": False, "usable": False, "description": "A tall, old-fashioned fridge hums quietly in the corner."},
            "west": {"name": "Cauldron", "can_be_taken": False, "usable": False, "description": "A large cauldron simmers over an open flame, bubbling with a mysterious brew."}
        }
    },
     "Armory":{
    "description":  "This stone-walled armory features a weapon rack filled with gleaming swords to the north, a locked chest to the west, and an exit leading to the storage room to the east.",
    "exits": {"east": "Storage", "south" : "Basement"},
    "items": {
        "north": {"name": "Weapon rack", "can_be_taken": False, "usable": True, "description": "A sturdy rack holds several gleaming swords, their blades polished to perfection."},
        "south": None,
        "west": {"name": "Chest", "can_be_taken": False, "usable": True, "description": "A large chest with a heavy lock, hinting at treasure within."},
        "south": {"name": "Sword rack", "can_be_taken": False, "usable": True, "description": "A rack specifically for swords, each one finely crafted and battle-ready."}
    }
},
    "Storage": {
        "description": "This dimly lit storage room is filled with the scent of aged wood and dust, featuring shelves stacked with scrolls and armor. To the north, a rusted dagger rests on a rickety table, while a locked chest sits to the east, hiding its secrets amidst barrels to the west.",
        "exits": {"south": "Armory"},
        "items": {
            "north": {"name": "Dagger", "can_be_taken": False, "usable": False, "description": "A rusted dagger rests on a rickety table, its blade dulled by time."},
            "south": None,
            "east": [
                {"name": "Chest", "can_be_taken": False, "usable": True, "description": "A locked chest sits quietly, holding untold secrets."},
                {"name": "Needles", "can_be_taken": True, "usable": True, "description": "A small bundle of sewing needles lies beside the chest."}
            ]
        }
    },
    "Upstairs Lobby": {
        "description": "You are in the lobby of upstairs level of the castle. The cozy bedroom to the west invites you with soft linens, while the clock room to the east ticks away time with its grand antique clocks. A warm glow emanates from the hallway, beckoning you to explore further.",
        "exits": {"south": "Corridor", "east": "Clock Room", "west": "Bedroom"},
        "items": {}
    },
    "Bedroom": {
        "description": "This luxurious bedroom features a plush four-poster bed draped in velvet, rich tapestries on the stone walls, and a pair of elegant sofas on west inviting relaxation. Exit on East leads to study room.",
        "exits": {"east": "Study Room", "south": "Upstairs Lobby"},
        "items": {
            "north": {"name": "Bed", "can_be_taken": False, "usable": False, "description": "A plush four-poster bed draped in luxurious velvet."},
            "south": None,
            "east": None,
            "west": {"name": "Sofas", "can_be_taken": False, "usable": True, "description": "A pair of elegant sofas invites you to relax in comfort."}
        }
    },
    "Study Room": {
        "description": "This tranquil study room is lined with dark wooden shelves filled with leather-bound books. A sturdy oak desk sits in the center, adorned with quills and parchment, inviting creativity. To the west, a comfortable armchair provides a cozy spot for reading, while a globe stands to the east, offering a glimpse of distant lands. A window to the west lets in soft sunlight, illuminating the space.",
        "exits": {"south": "Bedroom"},
        "items": {
            "north": {"name": "Table", "can_be_taken": False, "usable": False},
            "east": {"name": "Globe", "can_be_taken": True, "usable": False},
            "south": None,
            "west": {"name": "Armchair", "can_be_taken": False, "usable": True}
        }
    },
    "Clock Room": {
        "description": "This intriguing clock room is filled with ornate timepieces. A large antique clock stands frozen at midnight, its needles mysteriously missing. Shelves of smaller clocks line the walls, and a plush armchair in the corner invites contemplation.",
        "exits": {"south": "Upstairs Lobby"},
        "items": {
            "north": {"name": "Armchair", "can_be_taken": False, "usable": True, "description": "A plush armchair in the corner, perfect for contemplation."},
            "south": None,
            "east": {"name": "globe", "can_be_taken": True, "usable": False, "description": "A globe depicting the world, inviting exploration."},
            "west": {"name": "Large Clock", "can_be_taken": False, "usable": True, "description": "A large antique clock, frozen at midnight, with missing hands."}
        }
    }
}
        #SP23-BAI-016
        self.current_room = 'Entrance'
        self.puzzles_solved = 0
        self.tokens_collected = 0
        self.inventory = []
        self.required_puzzles = 2
        self.required_tokens = 2

    #SP23-BAI-016
    def main_game_loop(self, player_actions):
        print("Welcome to the Mysterious Castle Adventure!")
        print("You are standing at the entrance of a mysterious castle.")
        print("Your goal is to explore the castle, solve puzzles, and find a way out.")
        
        load_prompt = input("Do you want to load the last saved game? (yes/no): ").lower()
        if load_prompt == "yes" and self.load_game():
            player_actions.look(self.current_room)
        else:
            print("\nStarting a new game.")
            player_actions.look(self.current_room, self.rooms)

        item_usage = ItemUsage(self)

        while True:
            command = input("\nEnter a command (type 'help' for options): ").lower()

            if command.startswith("go "):
                parts = command.split()
                if len(parts) < 2:
                  print("You need to specify a direction (north, south, east, west, northeast, northwest).")
                  continue
                direction = parts[1]
                self.current_room = player_actions.move_player(direction, self.current_room, self.rooms)
                player_actions.look(self.current_room, self.rooms)
            #SP23-BAI-016
            elif command == "look":
                player_actions.look(self.current_room, self.rooms)

            elif command == "help":
                player_actions.show_help()

            elif command == "save":
                player_actions.save_game(self.current_room, self.inventory, self.tokens_collected, self.puzzles_solved)

            elif command == "load":
                if player_actions.load_game(self.current_room, self.inventory, self.tokens_collected, self.puzzles_solved):
                    player_actions.look(self.current_room)

            #SP23-BAI-023
            elif command == "inventory":
                player_actions.show_inventory(self.inventory)

            elif command.startswith("take "):
                item_name = ' '.join(command.split()[1:])
                player_actions.take(item_name, self.current_room, self.inventory, self.rooms)

            elif command.startswith("drop "):
                item_name = ' '.join(command.split()[1:])
                player_actions.drop(item_name, self.inventory)

            # Examine an item in the current room
            elif command.startswith("examine "):
                item_name = command[8:].strip()  # Extract the item name
                if item_name:
                  player_actions.examine(item_name, self.current_room, self.rooms)
                else:
                  print("You need to specify an item to examine.")

            
            elif command.startswith("use "):
              parts = command.split()
              if len(parts) < 2:
               print("You need to specify an item to use.")
               continue
              item_name = parts[1]
              item_usage.use_item(item_name, self.current_room, self.inventory)
  
            #SP23-BAI-016
            elif command == "quit":
                if player_actions.quit_game():
                    break
            else:
                print("Invalid command. Type 'help' to see available commands.")

            # Check if the user has met the conditions to escape the castle
            if self.current_room == "Council Room" and "Key to Council Room" in inventory and metal_token_counter >= 2 and puzzle_counter >= 2:
               print("You have reached the final puzzle! Place the metal tokens on the strategy board to escape the castle.")
               if item_usage.solve_strategy_board_puzzle():
                 print("You have escaped the castle!")
                 print("Congratulations, you have won the game!")
                 
                 break
                

            

class PlayerActions:

    #SP23-BAI-016
    def move_player(self, direction, current_room, rooms):
     direction = direction.lower()
     exits = rooms[current_room].get('exits', {})

     if direction in exits:
        next_room = exits[direction]
        
        if next_room == "Council Room":
            if "Key" in [item["name"] for item in self.inventory]:
                print(f"Moving {direction} to {next_room}.")
                return next_room
            else:
                print("The Council Room is locked. You need a key to enter.")
                return current_room
        else:
            print(f"Moving {direction} to {next_room}.")
            return next_room
     else:
        # Check if the direction points to an item instead of an exit
        items = rooms[current_room].get('items', {})
        if direction in items:
            item_info = items[direction]
            # Only display the names of the items
            if isinstance(item_info, list):
                item_names = [item['name'] for item in item_info]
                print(f"You see the following items in the {direction}: {', '.join(item_names)}.")
            else:
                print(f"You see {item_info['name']} in the {direction}.")
            return current_room 
        else:
            print(f"There is no exit or item in the {direction}.")
            return current_room

    #SP23-BAI-023

    def show_inventory(self, inventory):
        if inventory:
            print("You are carrying:")
            for item in inventory:
                print(f'- {item["name"]}')
        else:
            print("Your inventory is empty.")

    #SP23-BAI-023

    def take(self, item_name, current_room, inventory, rooms):
        room_items = rooms[current_room]["items"]
        item_found = None

        for direction, items in room_items.items():
            if isinstance(items, list):
                for item in items:
                    if item["name"].lower() == item_name.lower() and item["can_be_taken"]:
                        item_found = item
                        break
            elif isinstance(items, dict):
                if items and items["name"].lower() == item_name.lower() and items["can_be_taken"]:
                    item_found = items
                    break
        
        if item_found:
            inventory.append(item_found)
            print(f'You have taken the {item_name}.')
            
            if isinstance(room_items[direction], list):
                room_items[direction].remove(item_found)
            else:
                rooms[current_room]["items"][direction] = None
        else:
            print(f'You cannot take it.')

    #SP23-BAI-023

    def drop(self, item_name, inventory):
        item_found = None
        for item in inventory:
            if item["name"].lower() == item_name.lower():
                item_found = item
                break
        
        if item_found:
            confirmation = input(f"Are you sure you want to drop the {item_name}? (yes/no): ").lower()
            
            if confirmation == 'yes':
                inventory.remove(item_found)
                print(f'You have dropped the {item_name}.')
        else:
            print(f'You do not have {item_name} in your inventory.')

    #SP23-BAI-023

    def examine(self, item_name, current_room, rooms):
        room_items = rooms[current_room]["items"]

        for direction, items in room_items.items():
           if isinstance(items, list):  # If items is a list
              for item in items:
                 if item["name"].lower() == item_name.lower():  # Case insensitive comparison
                    print(item["description"])
                    return
           elif isinstance(items, dict):  # Single item
              if items["name"].lower() == item_name.lower():
                print(items["description"])
                return

        # If item is not found
        print(f"There is no item named '{item_name}' to examine in this room.")


    
    #SP23-BAI-016
    def look(self, current_room, rooms):
      """Display the room description and list visible items."""
    
      if current_room in rooms:
        print(f"\n{rooms[current_room]['description']}\n")
      else:
        print(f"Error: Room '{current_room}' not found.")
    
      items = rooms[current_room].get('items', {})
    
      for position, item_info in items.items():
        if isinstance(item_info, list):
            for item in item_info:
                name = item.get('name', 'Unknown item')
                print(f"At the {position}, you see {name}")
        elif item_info:
            name = item_info.get('name', 'Unknown item')
            print(f"At the {position}, you see {name}")

    #SP23-BAI-016
    def show_help(self):
        print("""
        Available commands:
        - go [direction] (north, south, east, west)
        - look
        - inventory
        - take [item]
        - drop [item]
        - quit
        """)

    #SP23-BAI-016
    def quit_game(self):
     quit_confirmation = input("Are you sure you want to quit? (yes/no): ").lower()
     if quit_confirmation == "yes":
        print("Thanks for playing!")
        return True
     return False
    
    #SP23-BAI-016
    def save_game(self, current_room, inventory, metal_token_counter, puzzle_counter):
    
     try:
        with open('savefile.txt', 'w') as f:
            f.write(f"current_room={current_room}\n")
            f.write(f"inventory={','.join([item['name'] for item in inventory])}\n")
            f.write(f"metal_token_counter={metal_token_counter}\n")
            f.write(f"puzzle_counter={puzzle_counter}\n")
        print("Game saved successfully.")
     except Exception as e:
        print(f"An error occurred while saving the game: {e}")

    #SP23-BAI-016
    def load_game(self, current_room, inventory, metal_token_counter, puzzle_counter):
    
     try:
        with open("savefile.txt", "r") as f:
            current_room = f.readline().strip().split('=')[1]
            inventory_line = f.readline().strip()
            inventory = [{'name': item} for item in inventory_line.split('=')[1].split(",")] if inventory_line else []
            metal_token_counter = int(f.readline().strip().split('=')[1])
            puzzle_counter = int(f.readline().strip().split('=')[1])

        # Display the current room's description and items
        player_actions.look(current_room)

        print("Game loaded successfully.")
        return True
     except FileNotFoundError:
        print("No saved game found.")
        return False
     except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        return False

#SP23-BAI-023
class ItemUsage:
    
    def __init__(self, game):
        self.game = game

    #SP23-BAI-023
    def use_item(self, item_name, current_room, inventory):
      try:

        current_room = self.game.current_room
        inventory = self.game.inventory
        
        # Get the current room's items
        room_items = self.game.rooms[current_room]["items"]

        # Check if the item is in the inventory by its name
        inventory_item = item_name if item_name in inventory else None

        # Function to find the item in the current room
        def find_item_in_room():
            for direction, items in room_items.items():
                if isinstance(items, list):  # Handle lists of items
                    for item in items:
                        if item["name"].lower() == item_name.lower():
                            return item
                elif isinstance(items, dict):  # Handle single item dictionary
                    if items["name"].lower() == item_name.lower():
                        return items
            return None

        # Find the item in the current room or in the inventory
        item_to_use = find_item_in_room() or ({"name": inventory_item, "usable": True} if inventory_item else None)

        if item_to_use:
            if item_to_use.get("usable", False) or isinstance(item_to_use, str):
                # Call the new function
                self.handle_item_usage(item_to_use["name"] if isinstance(item_to_use, dict) else item_to_use)
            else:
                print(f"The {item_name} is not usable.")
        else:
            print(f"The {item_name} is not found in your inventory or the current room.")
      except ValueError as e:
            print(e)
      except Exception as e:
            print("A mysterious force disrupts your actions. Perhaps you should try again later.")

    #SP23-BAI-023
    def handle_item_usage(self, item_name):
        """Handle the usage of an item based on its name."""
        item_name_lower = item_name.lower()
        
        if item_name_lower == "letter":
            self.use_letter()
        elif item_name_lower == "tapestry":
            self.use_tapestry()
        elif item_name_lower == "ladder":
            self.use_ladder()
        elif item_name_lower == "weapon rack":
            self.use_weaponrack()
        elif item_name_lower == "needles":
            self.use_clock_needles
        elif item_name_lower == "potion on chest":
            self.use_acid_potion_on_chest
        elif item_name_lower == "strategy board":
            self.solve_strategy_board_puzzle()
        elif item_name_lower == "key":
            self.use_key_on_council_room()
        elif item_name_lower == "potion":
            self.use_acid_potion()
        else:
            print(f"You cannot use the {item_name}.")

    #SP23-BAI-023
    def use_letter(self):
        # The coded word with missing letters represented by underscores
        coded_word = "T__O__E"  # Coded word: "T H R O N E"
        correct_word = "THRONE"  # The correct word to decode
        attempts = 3  # Number of attempts allowed

        print("The coded word is:", coded_word)
        print("You have to guess the missing letters!")

        for attempt in range(attempts):
            user_input = input(f"Attempt {attempt + 1}/{attempts}: Enter a letter: ").upper()

            if user_input in correct_word:
                print(f"Good job! '{user_input}' is in the word.")
                coded_word = coded_word.replace("_", user_input, 1)  # Replace the first underscore with the guessed letter
                print("Current progress:", coded_word)
            else:
                print(f"Sorry, '{user_input}' is not in the word.")
            
            # Check if the coded word has been fully decoded
            if "_" not in coded_word:
                print("You've decoded the word!")
                print("The letter reveals a riddle:")
                print('"Join them together, and the path will unfold,\nA way to escape, as the tale is told."')
                return

        print("You ran out of attempts. The word remains undecoded.")

    #SP23-BAI-023
    def use_tapestry(self):
        print("You have approached the tapestry and notice something odd about it.")
        print("There's a hidden lever behind the tapestry. Do you want to pull it? (yes/no)")

        choice = input("> ").lower()

        if choice == "yes":
            print("You have pulled the lever, and the room trembles slightly.")
            print("A hidden compartment opens, and a riddle is revealed:")
            print("""
            Two treasures scattered, each a part,
            On the table of strategy, they'll play their part.
            """)
        elif choice == "no":
            print("You have stepped away from the tapestry, leaving the lever untouched.")

    #SP23-BAI-023
    def use_ladder(self):
        global metal_token_counter, puzzle_counter, inventory
        
        print("You climb the ladder and discover a hidden compartment.")
        print("Inside, there is a small piece of parchment with a riddle.")
        
        # The riddle: Numbers representing letters of the alphabet
        print("Riddle: Convert these numbers to letters to form a word.")
        numbers = [19, 5, 3, 18, 5, 20]  # These correspond to the word 'SECRET'
        print("Numbers:", numbers)
        
        # Correct word (manually assigned, no need to convert)
        correct_word = "SECRET"
        
        # Ask the user to solve the riddle by entering the correct word
        user_answer = input("What is the word? ").strip().upper()

        if user_answer == correct_word:
            print("The compartment opens, and you find a metal token!")
            metal_token_counter += 1
            puzzle_counter += 1
            inventory.append("Metal Token")
            print(f"Metal token added to your inventory. You now have {metal_token_counter} metal token(s).")
            print(f"Puzzle solved! Total puzzles solved: {puzzle_counter}")
        else:
            print("That's not correct. The compartment remains closed.")
     

     #SP23-BAI-023
    def use_weaponrack(self):
        global metal_token_counter, puzzle_counter, inventory

        attempts = 3  # Number of attempts allowed
        print("You have 3 swords to place: Excalibur, Katana, and Rapier.")
        
        # Create a list to hold placed swords
        placed_swords = []

        for attempt in range(attempts):
            sword = input(f"Attempt {attempt + 1}/{attempts}: Enter the sword you want to place (Excalibur/Katana/Rapier): ").strip()
            position = input("Enter the position to place the sword (1, 2, or 3): ").strip()

            # Validate input
            if position not in ['1', '2', '3']:
                print("Invalid position! Choose from 1, 2, or 3.")
                continue

            # Check if the position is already filled
            if len(placed_swords) >= int(position):
                print(f"There's already a sword in position {position}! Choose another position.")
                continue
            
            # Place the sword
            placed_swords.append(sword)
            print(f"{sword} placed in position {position}.")

            # Check if all swords are placed correctly
            if self.check_swords_placed(placed_swords):
                metal_token_counter += 1
                puzzle_counter += 1
                inventory.append("Metal Token")
                print("Congratulations! You've placed all swords correctly and received a Metal Token.")
                break
        else:
            print("You've used all your attempts. Please try again.")

    #SP23-BAI-023
    def check_swords_placed(self, placed_swords):
        """Check if the placed swords are correct."""
        correct_swords = ['Excalibur', 'Katana', 'Rapier']  # Correct order
        return placed_swords == correct_swords
    
    #SP23-BAI-016
    def use_acid_potion_on_chest(self):
      print("You want to pour the Acid Potion into the chest. Do you have the Acid Potion?")
      user_input = input("Do you have the Acid Potion? (yes/no): ")
    
      if user_input.lower() == "yes":
        if "Acid Potion" in [item["name"] for item in inventory]:
            print("You have poured the Acid Potion into the chest and locked it!")
            global metal_token_counter, puzzle_counter
            metal_token_counter += 1
            puzzle_counter += 1
            inventory.append({"name": "Metal Token", "can_be_taken": True, "usable": True})
        else:
            print("You don't have the Acid Potion.")
      else:
        print("You don't have the Acid Potion.")

    #SP23-BAI-016
    def use_clock_needles(self):
      print("You want to place the clock needles in the Large Clock. Do you have the clock needles?")
      user_input = input("Do you have the clock needles? (yes/no): ")
    
      if user_input.lower() == "yes":
        if "Needles" in [item["name"] for item in inventory]:
            print("You have placed the clock needles in the Large Clock!")
            print("You need to set the time according to the clue.")
            time_clue = "3:15"  # Replace with the actual clue
            user_input = input(f"Enter the time ({time_clue}): ")
            
            if user_input == time_clue:
                print("You have set the time correctly!")
                global metal_token_counter, puzzle_counter
                metal_token_counter += 1
                puzzle_counter += 1
                inventory.append({"name": "Metal Token", "can_be_taken": True, "usable": True})
            else:
                print("You have set the time incorrectly.")
        else:
            print("You don't have the clock needles.")
      else:
        print("You don't have the clock needles.")

    #SP23-BAI-016
    def use_acid_potion(self):
      print("You want to create the Acid Potion. Do you have the required items?")
      print("You need a Potion and a Recipe.")
      user_input = input("Do you have these items? (yes/no): ")
    
      if user_input.lower() == "yes":
        if "Potion" in [item["name"] for item in inventory] and "Recipe" in [item["name"] for item in inventory]:
            print("You have created the Acid Potion!")
            inventory.append({"name": "Acid Potion", "can_be_taken": True, "usable": True})
        else:
            print("You don't have the required items to create the Acid Potion.")
      else:
        print("You don't have the required items to create the Acid Potion.")

    #SP23-BAI-016
    def use_key_on_council_room(self):
    
      print("You want to use the key to unlock the Council Room. Do you have the key?")
      user_input = input("Do you have the key? (yes/no): ")
    
      if user_input.lower() == "yes":
        if "Council Room Key" in [item["name"] for item in inventory]:  # Check for the specific key
            print("You have unlocked the Council Room!")
            current_room = "Council Room"  # Update the current room
            print("You are now in the Council Room.")
            print("You see a strategy board with several slots for tokens.")
            if self.solve_strategy_board_puzzle():  # Check if the puzzle is solved
                print("Congratulations! You have successfully solved the puzzle!")
                print("A hidden staircase is revealed, leading to your escape!")
                escaped = True  # Set the escape flag to True
                print("You have escaped the castle!")  # Final message
            else:
                print("You did not solve the puzzle correctly. Try again!")
        else:
            print("You don't have the key.")
      else:
        print("You don't have the key.")

    #SP23-BAI-016
    def solve_strategy_board_puzzle(self):
      print("You see a strategy board with several squares on it. You need to place the metal tokens on the correct squares to solve the puzzle.")
      print("The board looks like this:")
      print(" 1 | 2 | 3")
      print("---------")
      print(" 4 | 5 | 6")
      print("---------")
      print(" 7 | 8 | 9")

    # Get the user's moves
      moves = []
      for i in range(metal_token_counter):
        move = input(f"Enter the square where you want to place metal token {i+1} (1-9): ")
        while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid move. Please try again.")
            move = input(f"Enter the square where you want to place metal token {i+1} (1-9): ")
        moves.append(move)

    # Create a dictionary to store the number of metal tokens on each square
      token_counts = {}
      for move in moves:
        if move in token_counts:
            token_counts[move] += 1
        else:
            token_counts[move] = 1

    # Check the user's moves
      if metal_token_counter >= 2 and token_counts.get("5", 0) >= 1 and token_counts.get("2", 0) >= 1 and token_counts.get("8", 0) >= 1:
        return True
      else:
        print("Sorry, that's not correct. Try again!")
        return False
    

#SP23-BAI-023

if __name__ == "__main__":
    game = Game()
    player_actions = PlayerActions()
    game.main_game_loop(player_actions)
