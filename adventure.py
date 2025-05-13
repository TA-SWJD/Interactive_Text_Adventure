"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
import class_player
import class_world
import class_puzzle

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    win_need_score = 30
    # the score needs to win
    have_move = 30
    # the moves you have
    current_moves = 0
    # starting moves
    # with (open("map.txt", "r") as map_file, open("locations.txt", "r") as locations_file,
    #       open("items.txt", "r") as items_file):
    #     w = class_world.World(map_file, locations_file, items_file)
    #     p = class_player.Player(0, 0, 30)
    #     world_map = w.load_map(map_file)
    #     adv_location = w.load_location(locations_file)
    #     world_items = w.load_items(items_file)
    w = class_world.World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = class_player.Player(0, 0, 30)
    world_map = w.load_map(open("map.txt"))
    adv_location = w.load_location(open("locations.txt"))
    world_items = w.load_items(open("items.txt"))
    #
    menu = ["look", "inventory", "score", "quit", "back"]

    combine_item_puzzle = class_puzzle.CombineItem(hint="What two items can be combined to get what you want?",
                                                   required_material=['Stone', 'Abrasive_tool'],
                                                   combined_item='Stone_Key')
    open_chest_puzzle = class_puzzle.OpenChest(hint="What item can you use to open the chest?",
                                               combined_item="Stone_Key", chest_location=19, final_item="T_card")
    missile_launch_puzzle = class_puzzle.MissileLaunch(hint="Walk around the campus to see if you can find "
                                                            "any hint for the password?", launch_pad="launch_pad",
                                                       password=1890169, sealed_item="Cheat_Sheet",
                                                       target_loc=13)
    businessman_trading_puzzle = class_puzzle.BusinessmanTrading(hint="Trade wisely, some items are "
                                                                      "crucial for your success.", business_location=17,
                                                                 crucial_item=["Cheat_Sheet", "T_Card", "Stone",
                                                                               "Abrasive_tool", "Stone_Key",
                                                                               "launch_pad"], exchange_item="Lucky_Pen")

    print("Welcome to the Text Adventure Game(UofT version)")
    name = input("Please enter your name to continue: ")
    print("hi, " + name + ". You can now choose to enter the game by entering enter, "
                          "the rules will show up immediately, enter quit to quit the game ")
    print("Your starting location will be ROBERTS LIBRARY   ")
    choice = input("\nEnter action: ").lower()
    if choice == "enter":
        print("RULES AND PROMPT")
        # ----------------------------------------------------------------------------
        print("# ----------------------------------------------------------------------------#")
        print("You've got an important exam coming up this evening, and you've been studying for weeks. \n"
              "Last night was a particularly late night on campus. You had difficulty focusing, so rather\n "
              "than staying in one place, you studied in various places throughout campus as the night progressed.\n "
              "Unfortunately, when you woke up this morning, you were missing some important exam-related items.\n "
              "You cannot find your T_card, and you're nervous they won't let you into tonight's exam without it.\n "
              "Also, you seem to have misplaced your lucky exam pen -- even if they let you in, you can't possibly\n "
              "write with another pen! Finally, your instructor for the course lets you bring a cheat sheet - \n"
              "a handwritten page of information in the exam. Last night, you painstakingly crammed as much \n"
              "material onto a single page as humanly possible, but that's missing, too! All of this stuff must\n "
              "be around campus somewhere! Can you find all of it before your exam starts tonight?\n")
        print("# ----------------------------------------------------------------------------#")
        print("Following items are hidden in the 5 * 5 map"
              "there are 23 locations in total")
        print("Your starting location will be  ROBERTS LIBRARY   ")
        p.menu_actions("look", world_map, adv_location)
        # ----------------------------------------------------------------------------
        print("Loading...")
        print("You have started the game, Good Luck!")
        while not p.victory:
            location = w.get_location(p.x, p.y)
            actions = []
            location_actions = []
            special_a = []
            print("Above is what you just done! What to do next? \n")
            print("You can choose to call [menu]")
            print("and these are the list of actions you can perform at this location: ")
            if location is not None:
                for action in w.available_actions(p):
                    actions.append(action)
                print("   Available movements: " + " ,".join(actions))
                for location_action in location.available_actions():
                    location_actions.append(location_action)
                print("   Other actions: " + ", ".join(location_actions))

                print("   Special actions is shown below")

                special_actions = class_puzzle.available_action(p, w, businessman_trading_puzzle)
                for s in special_actions:
                    special_a.append(s)
                # print("   ".join(special_actions))

            choice = input("\nEnter action: ").lower()
            if choice in ["north", "south", "west", "east"]:
                p.go_direction(choice, w.map, w.locations)
                current_moves += 1

            elif choice == "pick up":
                i = 0
                for items in world_items:
                    if location.loc_number == items.current_position:
                        p.pick_up_item(items)
                    else:
                        i += 1
                if i == len(world_items):
                    print("You can pick up the air on the floor, will you?")

            elif choice == "drop item":
                lst = p.menu_actions_2("inventory", world_map, adv_location)
                p.menu_actions("inventory", world_map, adv_location)
                if lst == "Your inventory is empty":
                    continue
                else:
                    print("You have the above items")
                    choice = input("\nDrop Which One?")
                    i = 0
                    for items in world_items:
                        if choice == items.name:
                            p.drop_item(items, location.loc_number)
                            if location.loc_number == items.target_position:
                                p.score += items.target_points
                                print("You successfully drop one item at the correct place \n")
                                print("You have received ")
                                print(items.target_points)
                                print("points")
                        else:
                            i += 1
                    if i == len(world_items):
                        print(choice + " is not in your inventory.")

            elif choice == "combine":
                if not p.inventory:
                    print("You have nothing to combine.")
                else:
                    print("You have the following items: ")
                    p.menu_actions("inventory", w.world_map, w.adv_location)
                    item1 = input("Choose the first item to combine: ").lower()
                    item2 = input("Choose the second item to combine: ").lower()
                    if item1 != item2 and combine_item_puzzle.combine_item(p, item1, item2):
                        print("You have successfully combined to create Stone_Key.")
                    else:
                        print("These items cannot be combined.")

            elif choice == "open_chest":
                inventory_items = p.get_inventory()
                if any(item == "T_card" for item in inventory_items):
                    print("You already obtain the item in the chest!")
                elif open_chest_puzzle.open_chest(p, w):
                    print("You have successfully opened the chest and found T_card.")
                elif open_chest_puzzle.combined_item not in p.inventory:
                    print("You don't have the required item to open the chest.")

            elif choice == "type_password":
                inventory_items = p.get_inventory()
                launch_pad_present = any(item == "launch_pad" for item in inventory_items)
                if any(item == "Cheat_Sheet" for item in inventory_items):
                    print("The missile pad is already used, it is not responding")
                elif launch_pad_present:
                    player_input = int(input("Enter the password: "))
                    if missile_launch_puzzle.use_launch_pad(p, player_input, w):
                        print("Correct password! Super_Castle has been destroyed by the missile you just launched,\n"
                              " and you suddenly see Cheat_Sheet fly to your hands due to the explosion.")
                    else:
                        print("Incorrect password. Try again.")

            elif choice == "trade":
                curr_location = w.get_location(p.x, p.y).loc_number
                if curr_location == 17 and not businessman_trading_puzzle.traded_or_not and p.inventory != []:
                    print("Available items to trade: " + ", ".join(p.inventory))
                    item_to_trade = input("Which item would you like to trade? ")
                    businessman_trading_puzzle.trade(p, item_to_trade)
                    if not businessman_trading_puzzle.trade(p, item_to_trade):
                        break
                else:
                    print("There is nothing for you to trade!")

            if current_moves >= have_move:
                # move have been reached
                print("You have walked too much... It is too late... You failed... You are destine to fail.")
                print("You can restart the game to go back to this morning")
                break

            if choice == "[menu]":
                print("Menu Options: \n")
                for option in menu:
                    print(option)
                choice = input("\nChoose action: ").lower()
                if choice == "quit":
                    print("The world will be unsaved, quiting game now...")
                    print("You can exit whenever you want")
                    break
                else:
                    p.menu_actions(choice, world_map, adv_location)

            if p.score >= win_need_score:
                # score have been reached
                print("You have achieve the necessary score to have 100% on the time! Are you continuing?")
                choice = input("\nEnter Yes or No: ").lower()
                if choice == "yes":
                    p.victory = True
                    print("Congratulation on Achieve 100 on the exam!")
                else:
                    continue
    else:
        print("The world will be unsaved, quiting game now...")
        print("You can exit whenever you want")

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120
    # })
