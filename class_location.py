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
# from typing import Optional, TextIO
import class_item


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - name: the name of the item
        - loc_number: location number on the map.txt, 1 2 3 so on
        - loc_item: the item at the current location, will be nothing is no items
        - brief_desc: brief description of the location read from location.txt
        - long_desc: long description of the location read from location.txt
        - visited: whether the location is visited or not

    """

    def __init__(self, name: str, loc_number: int, loc_item: class_item.Item, brief_desc: str, long_desc: str) -> None:
        """
        Initialize a new location.

        """
        self.name = name
        self.loc_number = loc_number
        self.loc_item = loc_item
        self.brief_desc = brief_desc
        self.long_desc = long_desc
        self.visited = False

    def get_full_description(self):
        """
        Return the full description of the location upon first visit

        """
        return f"LOCATION {self.loc_number}\n\n{self.long_desc}"

    def get_brief_description(self):
        """
        Return a brief description of the location if not player's first visit

        """
        return f"LOCATION {self.loc_number}\n\n{self.brief_desc}"

    def available_actions(self):
        """
        Return a list of available actions at this location.
        """
        actions = []
        if self.loc_item and self.loc_item.pick_up_state:
            actions.append(f"Pick up {self.loc_item.name}")
        return actions
