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
import class_player
import class_world


class Puzzle:
    """ A puzzle in our text adventure game world.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - solved: the status showing whether this puzzle have been solved or not

    """
    hint: str
    solved: bool

    def __init__(self, hint: str) -> None:
        """ Initialize a new puzzle
        """
        self.hint = hint
        self.solved = False


class CombineItem(Puzzle):
    """ Part of the puzzle that require players to combine items that will be needed.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - required_material: the required material for players to combine
        - combined_item: the combined item
        - solved: the status showing whether this puzzle have been solved or not

    """
    hint: str
    required_material: list[str]
    combined_item: str
    solved: bool

    def __init__(self, hint: str, required_material: list[str], combined_item: str) -> None:
        """ Initialize the item combination part of the puzzle

        """
        super().__init__(hint)
        self.hint = hint
        self.required_material = required_material
        self.combined_item = combined_item
        self.solved = False

    def combine_item(self, player: class_player.Player, item1: str, item2: str) -> bool:
        """ Verify if players are eligible for combining items

        """
        if (("Stone" in player.inventory and "Abrasive_tool" in player.inventory)
                and (item1 == "stone" or item2 == "stone") and (item1 == "abrasive_tool" or item2 == "abrasive_tool")):
            for item in self.required_material:
                player.inventory.remove(item)
            player.inventory.append(self.combined_item)
            self.solved = True
        return self.solved

    def hint_combine(self) -> None:
        """ Provide a hint for combining if player cannot solve
        """
        if not self.solved:
            print(self.hint)


class OpenChest(Puzzle):
    """ Part of the puzzle that require players to use to the combined item to open the locked chest.

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - combined_item: the combined item
        - final_item: the item received after solving the puzzle
        - chest_location: the location of the chest that's waiting to be unlocked
        - solved: the status showing whether this puzzle have been solved or not

    """
    hint: str
    combined_item: str
    final_item: str
    chest_location: int

    def __init__(self, hint: str, combined_item: str, final_item: str, chest_location: int) -> None:
        """ Initialize the use combined item to open the chest part of the puzzle
        """
        super().__init__(hint)
        self.hint = hint
        self.combined_item = combined_item
        self.final_item = final_item
        self.chest_location = chest_location
        self.solved = False

    def open_chest(self, player: class_player.Player, world: class_world.World) -> bool:
        """
        Open the chest that exist
        """
        curr = world.get_location(player.x, player.y)
        if curr.loc_number == self.chest_location and self.combined_item in player.inventory:
            player.inventory.append(self.final_item)
            self.solved = True
        return self.solved

    def chest_hint(self) -> None:
        """
        Provide a hint for how to open the chest

        """
        if not self.solved:
            print(self.hint)


class MissileLaunch(Puzzle):
    """ Another puzzle that requires players to use the missile launch pad and password to destroy
    a place called super castle and get the things they needed to win the game.

    Instance Attributes:
        - password: the password required to activate the missile launch pad
        - launch_pad: an item that allows you to type password
        - sealed_item: the item that is hidden in campus
        - target_loc: the location where the item is hidden
        - solved: the status showing whether this puzzle have been solved or not

    """
    password: int
    launch_pad: str
    sealed_item: str
    target_loc: int
    solved: bool

    def __init__(self, hint: str, password: int, launch_pad: str, sealed_item: str, target_loc: int) -> None:
        super().__init__(hint)
        self.password = password
        self.launch_pad = launch_pad
        self.sealed_item = sealed_item
        self.target_loc = target_loc
        self.solved = False

    def check_password(self, player_input: int) -> bool:
        """ Check if players input the correct password
        """
        return player_input == self.password

    def use_launch_pad(self, player: class_player.Player, player_input: int, world: class_world.World) -> bool:
        """ Launch the missile if players discovered the launch as well as input the correct the password
        """
        if self.check_password(player_input):
            target_loc = world.locations[self.target_loc]
            world.destroy_location(target_loc)
            player.inventory.append(self.sealed_item)
            self.solved = True
        return self.solved


class BusinessmanTrading(Puzzle):
    """ Part of the puzzle that players need to trade an item with a businessman to get the item they need

    Instance Attributes:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - exchange_item: item that players exchange with the businessman
        - business_location: the location of the businessman
        - crucial_item: a list of special items that if players trade them will result in losing the game directly
        - trade_or_not: determine whether the player have traded with the businessman once or not

    """
    exchange_item: str
    crucial_item: list[str]
    business_location: int
    traded_or_not: bool

    def __init__(self, hint: str, exchange_item: str, crucial_item: list[str], business_location: int) -> None:
        super().__init__(hint)
        self.exchange_item = exchange_item
        self.crucial_item = crucial_item
        self.business_location = business_location
        self.traded_or_not = False

    def trade(self, player: class_player.Player, item_to_trade):
        """
        Notice that if you give the businessman something you need in order to win the game, you lose the game
        directly! So be careful with what you choose to trade, the businessman is going to give you something you need!
        Notice that you can only trade with him once, once you trade with him successfully, and you go back to the same
        location, you won't be able to trade with him again! However, if you didn't trade with him upon first visit, you
        can still trade with him later.

        """
        if self.traded_or_not:
            print("You already trade with me comrade! I have nothing left to give you.")
        if item_to_trade in self.crucial_item:
            print("Oh, you trade this precious thing with me! You won't be able to attend your test! HAHA!")
            print("You lose the game haha!")
            player.victory = False
        else:
            print("Good stuff! However, you are still teenager so I won't actually take this thing from you. "
                  "I will give you your lucky pen, just happened to find it somewhere in the campus.")
            player.inventory.append(self.exchange_item)
            self.traded_or_not = True
        return self.traded_or_not


def available_action(player: class_player.Player, world: class_world.World, business: BusinessmanTrading) -> list[str]:
    """
    Return a list of special available action
    """
    actions = []
    if all(item in player.inventory for item in ['Stone', 'Abrasive_tool']):
        actions.append("combine")

    curr = world.get_location(player.x, player.y)

    if all(item in player.inventory for item in ['Stone_Key']) and curr.loc_number == 19:
        actions.append("open_chest")

    for item in player.get_inventory():
        if item == "launch_pad":
            actions.append("type_password")

    if business.traded_or_not is False and curr.loc_number == 17:
        actions.append("trade")

    if not actions == []:
        print(actions)

    return actions


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 120
#     })
