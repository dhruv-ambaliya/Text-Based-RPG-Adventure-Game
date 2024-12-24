## Text-Based RPG Adventure ⚔️️

**Embark on a thrilling journey in this classic text-based RPG!**

This project lets you create a character, explore a fantasy world, battle enemies, and gain experience to grow stronger.

**What's Included:**

* Character creation with customizable names ✍️
* Exciting enemy encounters with Goblins! 🧌
* Turn-based combat system where you attack and defend ⚔️️
* Experience points for defeating enemies 🏆
* Level-up system to increase health, attack, and defense ⬆️
* Simple and intuitive gameplay ️🎮

**How to Play:**

1. Run the project: `python project.py`
2. Enter your character's name ✍️
3. Choose your action:
    * **Explore:** Encounter enemies and gain experience ⚔️
    * **Rest:** Recover health points 💖
    * **Check Stats:** See your current health, experience, and level 🔰
4. Battle enemies using turn-based combat ⚔️️
5. Level up and become a stronger adventurer! 💪

**Example Gameplay:**

```
Enter your character's name: Dhruv

Your health: 100
Your experience: 0
Your level: 1

What do you want to do? (explore, rest, check stats) explore

You encountered a Goblin!

Dhruv attacks Goblin for 8 damage. ️
Goblin attacks Dhruv for 5 damage. ️

Your health: 95
Your experience: 10

What do you want to do? (explore, rest, check stats) explore

You encountered a Goblin!

Dhruv attacks Goblin for 8 damage. ️
Goblin attacks Dhruv for 5 damage. ️

You defeated the Goblin!
You gained 15 experience!

Your health: 90
Your experience: 25

... (Continue exploring and defeating enemies)

Congratulations! You leveled up to level 2!

Your health: 110  (Increased because of level up)
Your attack: 12  (Increased because of level up)
Your defense: 6  (Increased because of level up)
Your experience: 25
```

**Code Functionality:**

* `Character` class: Represents the player character with attributes like health, attack, defense, experience, and level. It also includes methods for attacking enemies and leveling up.
* `Enemy` class: Represents enemies with predetermined stats and an attack method.
* `encounter_enemy` function: Handles combat between the player and an enemy, implementing turn-based attacks and experience gain.
* `play_game` function: Controls the main game loop, allowing the player to explore, rest, check stats, and encounter enemies.
