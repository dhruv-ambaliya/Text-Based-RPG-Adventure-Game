import random
from collections import defaultdict

### Character Class Definition ###
# This class defines a character in the game with attributes like name, health, attack, defense, experience, and level.
class Character:
    def __init__(self, name, health, attack, defense, experience=0, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
        self.level = level

    # This method reduces the character's health when they take damage.
    def take_damage(self, damage):
        self.health -= damage

    # This method allows the character to attack an enemy.
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage <= 0:
            damage = 1
        enemy.take_damage(damage)
        print(f"** {self.name} attacks {enemy.name} for {damage} damage. **")

    # This method handles the character leveling up.
    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack += 2
        self.defense += 1
        print(f"** Congratulations! You leveled up to level {self.level}. **")

### Enemy Class Definition ###
# This class defines an enemy in the game with attributes like name, health, attack, defense, and experience.
class Enemy:
    def __init__(self, name, health, attack, defense, experience):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience

    # This method reduces the enemy's health when they take damage.
    def take_damage(self, damage):
        self.health -= damage

    # This method allows the enemy to attack a player.
    def attack_enemy(self, player):
        damage = self.attack - player.defense
        if damage <= 0:
            damage = 1
        player.take_damage(damage)
        print(f"** {self.name} attacks {player.name} for {damage} damage. **")

### Item Class Definition ###
# This class defines an item in the game with attributes like name, description, and stats.
class Item:
    def __init__(self, name, description, stats):
        self.name = name
        self.description = description
        self.stats = stats

### Character and Enemy Creation Functions ###
# This function creates a new character with default stats.
def create_character(name):
    return Character(name, 100, 10, 5)

# This function creates a new enemy with random stats.
def create_enemy(name):
    return Enemy(name, random.randint(50, 100), random.randint(5, 15), random.randint(2, 8), random.randint(10, 20))

### Encounter Function ###
# This function handles the encounter between a player and an enemy.
def encounter_enemy(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player.attack_enemy(enemy)
        if enemy.health <= 0:
            print(f"** You defeated {enemy.name}! **")
            player.experience += enemy.experience
            if player.experience >= player.level * 30:  # Adjust the experience threshold as needed
                player.level_up()
            break
        enemy.attack_enemy(player)
        if player.health <= 0:
            print("** You were defeated! **")
            break

### Game Play Function ###
# This function starts the game and handles the main game loop.
def play_game():
    player_name = input("Enter your character's name: ")
    player = create_character(player_name)

    while player.health > 0:
        print(f"\n** Your health: {player.health} **")
        print(f"** Your experience: {player.experience} **")
        print(f"** Your level: {player.level} **")

        user_input = input("\nWhat do you want to do? (explore, rest, check stats, quit) ").lower()

        if user_input == "explore":
            enemy = create_enemy("Goblin")
            print(f"** You encountered a {enemy.name}! **")
            encounter_enemy(player, enemy)
        elif user_input == "rest":
            player.health += 10
            print("** You rested and recovered 10 health points. **")
        elif user_input == "check stats":
            print(f"** Health: {player.health} **")
            print(f"** Attack: {player.attack} **")
            print(f"** Defense: {player.defense} **")
            print(f"** Experience: {player.experience} **")
            print(f"** Level: {player.level} **")
        elif user_input == "quit":
            quit = input("Are you sure? You are gonna lose your progress!! ").lower()
            if quit == "yes" or quit == "y":
                exit()
            elif quit == "no" or quit == "n":
                continue
            else:
                print("** Invalid command. **")
        else:
            print("** Invalid command. **")

### Main Execution ###
if __name__ == "__main__":
    play_game()
