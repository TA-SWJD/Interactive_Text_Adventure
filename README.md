# 🧭 CampusQuest: The Final Exam Adventure Game

**CampusQuest** is a text-based Python adventure game where you, a lone student, must explore a strange and magical version of the University of Toronto campus — navigating libraries, labs, gardens, clock towers, and even subway stations — in a desperate attempt to reach the Exam Centre. Along the way, you’ll collect strange items, encounter mysterious characters, solve puzzles, and uncover hidden locations.

> This was my first full Python project built during my first year of university. It combines object-oriented design, file-based world loading, and a bit of narrative world-building.

---

## ✨ Features

- 🏫 Explore over 20 custom-designed locations across a fictionalized UofT campus
- 🗺️ Move through a 5x5 grid map using a parser-based interface
- 🧩 Solve puzzles with hints, item combinations, and trades
- 🎒 Inventory system with item pickup, drop, use, and trade logic
- 📦 Puzzle and item logic stored in external text files (`items.txt`, `map.txt`, etc.)
- 🧠 Simple but extensible object-oriented structure (`Player`, `World`, `Item`, `Puzzle`, etc.)

---

## 🧠 How It Works

- Game logic starts in `adventure.py`
- World is built from:
  - `locations.txt`: rich location descriptions
  - `map.txt`: 5x5 world grid
  - `items.txt`: collectible, combinable, and tradable items
- Core components are defined in:
  - `class_player.py`, `class_location.py`, `class_item.py`, `class_puzzle.py`, `class_world.py`

---

## 🕹️ How to Play

Run adventure.py
