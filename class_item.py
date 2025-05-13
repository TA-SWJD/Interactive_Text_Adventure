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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: The name of the item
        - start_position: The initial coordinates of the item
        - target_position: The coordinates where the item need to be deposited
        - target_points: The number of points awarded for depositing the item at target position
        - current_position: After players first discovered the item at the start_position, if they want to
                            drop the item. The new location of the item will be the current_position
        - pick_up_state: Indicate whether the item can be picked up or not at the moment

    Representation Invariants:
        - self.target_points >= 0
    """
    name: str
    start_position: int
    target_position: int
    target_points: int
    current_position: int
    pick_up_state: bool

    def __init__(self, name: str, start: int, target: int, target_points: int, curr: int, ) -> None:
        """Initialize a new item.
        """
        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.current_position = curr
        self.pick_up_state = True


class PuzzleItem(Item):
    """ An item that is associate with puzzles

    Instance Attribute:
        - hint: A little bit of hint of the puzzle for players who are attempting to solve it
        - puzzle_type: The type of puzzle that item associate with

    """
    hint: str
    puzzle_type: str

    def __init__(self, name: str, start: int, target: int, target_points: int, curr: int, hint: str, puzzle_type: str) \
            -> None:
        super().__init__(name, start, target, target_points, curr)
        self.hint = hint
        self.puzzle_type = puzzle_type


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'max-line-length': 120
#     })
