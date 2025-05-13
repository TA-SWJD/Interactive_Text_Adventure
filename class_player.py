"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
import class_item
import class_location


# def move_tracker() -> None:
#     """
#     This is a helper function that help count the number of moves
#     """
#     command = input("Which direction do you want to go: ")
#     if command.lower() in ["north", "south", "west", "east"]:
#         Player.move_increment()


def helper_output(location: class_location.Location) -> str:
    """
    This helper function helps go_direction where return long description if the location
    is not visited and brief description otherwise.
    """
    if location.visited is False:  # first time to this location
        return location.long_desc
    else:
        location.visited = True
        return location.brief_desc


# def quit_game():
#     """
#     Game Over and quit game
#
#     """
#     print("Game Over")
#     exit()


class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x: The player's x coordinates
        - y: The player's y coordinates
        - inventory: The player's inventory
        - victory: A boolean whether showing whether the player had won or not.
        - move_limit: The maximum number of moves players can take
        - current_move: Keep track of the number of moves players have
        - score: Player's score

    Representation Invariants:
        - self.x >= 0
        - self.y >= 0
        - self.move_limit >= 0

    """
    x: int
    y: int
    inventory: list
    victory: bool
    move_limit: int
    current_move: int
    score: int

    def __init__(self, x: int, y: int, move_limit: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.move_limit = move_limit
        self.current_move = 0
        self.score = 0

    def go_direction(self, direction: str, map_data: list[list[int]], locations: list[class_location.Location]) -> None:
        """
        The action Go.
        If Go[direction] is called, go_direction(direction, map_data, locations) will be excuted
        """
        x = self.x
        y = self.y
        if direction.lower() == "north":
            if x - 1 >= 0 and map_data[x - 1][y] != -1:
                # check if the x after changed will be out of bound and the location exist.
                self.x -= 1
                print(helper_output(locations[map_data[self.x][self.y]]))
            else:
                print("How about we explore the area ahead of us later?")
        elif direction.lower() == "south":
            if len(map_data) > x + 1 and map_data[x + 1][y] != -1:
                # check if the x after changed will be out of bound and the location exist.
                self.x += 1
                print(helper_output(locations[map_data[self.x][self.y]]))
            else:
                print("How about we explore the area ahead of us later?")
        elif direction.lower() == "east":
            if 0 <= y + 1 < len(map_data[0]) and map_data[x][y + 1] != -1:
                # check if the y after changed will be out of bound and the location exist.
                self.y += 1
                print(helper_output(locations[map_data[self.x][self.y]]))
            else:
                print("How about we explore the area ahead of us later?")
        elif direction.lower() == "west":
            if 0 <= y - 1 < len(map_data[0]) and map_data[x][y - 1] != -1:
                # check if the y after changed will be out of bound and the location exist.
                self.y -= 1
                print(helper_output(locations[map_data[self.x][self.y]]))
            else:
                print("How about we explore the area ahead of us later?")
        elif (direction.lower() != "west"
              and direction.lower() != "east"
              and direction.lower() != "south"
              and direction.lower() != "north"):
            print("INVALID INPUT")

    def player_look(self, map_data: list[list[int]], locations: list[class_location.Location], ) -> str:
        """
        This is return when the Look action is taken.
        It returns the long_description of the player's current location.
        """
        return locations[map_data[self.x][self.y]].long_desc

    def pick_up_item(self, item: class_item.Item) -> None:
        """
        Allow players to pick up items if they are at the item's location.

        """
        if item.pick_up_state:
            self.inventory.append(item.name)
            item.current_position = None
            # Item's start position is unique, and the purpose of current location is that if the player dropped the
            # item, they will be dropped at the current location, where the player currently standing, and waiting to
            # be collect again if intended.
            item.pick_up_state = False
            print(f"Wow! you discovered a {item.name}")
        elif not item.pick_up_state:
            self.inventory.append(item.name)
            item.current_position = None
            item.pick_up_state = False
            print(f"You picked up {item.name} again. (What you dropped before)")

    def drop_item(self, item: class_item.Item, loc: int) -> None:
        """
        Allow players to drop items in their inventory anytime they want.

        """
        self.inventory.remove(item.name)
        item.current_position = loc
        print(f"You successfully dropped {item.name} here!")

        # print(f"{item.name} is not in your inventory.")

    def get_inventory(self) -> list or str:
        """
        Allow players to get items

        """
        if not self.inventory:
            return "Your inventory is empty"
        else:
            inventory_list = [item for item in self.inventory]

        return inventory_list

    # def move_increment(self) -> None:
    #     """
    #     A helper function that count the number of moves, if moves >= move limit
    #     game ended immediately
    #     """
    #     self.current_move += 1
    #     if self.current_move >= self.move_limit:
    #         quit_game()

    def score_increment(self, points: int) -> None:
        """
        Update the player's score by a given amount.

        """
        self.score += points

    def get_score(self) -> str:
        """
        Showing player's current score

        """
        return f"Your current score is {self.score}"

    def menu_actions(self, action: str, world_map: list[list[int]], adv_location: list[[class_location.Location]]) \
            -> None:
        """
        Execute menu action as given.

        """
        menu = ["look", "inventory", "score", "quit", "back"]
        while action in menu:
            if action == "look":
                print(self.player_look(world_map, adv_location))
                return
            elif action == "inventory":
                print(self.get_inventory())
                return
            elif action == "score":
                print(self.get_score())
                return
            elif action == "quit":
                break

    def menu_actions_2(self, action: str, world_map: list[list[int]], adv_location: list[[class_location.Location]]):
        """
        Execute menu action as given.

        """
        menu = ["look", "inventory", "score", "quit", "back"]
        while action in menu:
            if action == "look":
                return self.player_look(world_map, adv_location)
            elif action == "inventory":
                return self.get_inventory()
            elif action == "score":
                return self.get_score()
            elif action == "quit":
                break

    # if __name__ == '__main__':
    #     import python_ta
    #     python_ta.check_all(config={
    #         'max-line-length': 120
    #     })
