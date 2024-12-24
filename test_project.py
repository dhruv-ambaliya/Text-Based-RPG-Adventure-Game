import pytest
from project import Character, Enemy, create_character, create_enemy, encounter_enemy

def test_character_creation():
    character = create_character("Test Character")
    assert character.name == "Test Character"
    assert character.health == character.max_health  # Check for max_health addition
    assert character.attack == 10
    assert character.defense == 5
    assert character.experience == 0
    assert character.level == 1  # Check for level addition

def test_enemy_creation():
    enemy = create_enemy("Test Enemy")
    assert enemy.name == "Test Enemy"
    assert enemy.health > 0
    assert enemy.attack > 0
    assert enemy.defense > 0
    assert enemy.experience > 0

def test_encounter_enemy(mocker):
    player = create_character("Test Player")
    enemy = create_enemy("Test Enemy")
    # Ensure player wins for testing (modify as needed)
    mocker.patch('project.random.randint', side_effect=[100, 10])  # Player attacks first and deals high damage

    encounter_enemy(player, enemy)

    assert player.health > 0
    assert enemy.health == 0
    assert player.experience > 0  # Player gains experience

def test_level_up():
    # Simulate gaining enough experience to level up
    character = create_character("Test Character")
    initial_level = character.level
    initial_stats = (character.max_health, character.attack, character.defense)
    character.experience = character.level * 100  # Set experience for level up

    character.level_up()

    assert character.level == initial_level + 1
    assert character.max_health > initial_stats[0]
    assert character.health == character.max_health  # Health resets to max after level up
    assert character.attack > initial_stats[1]
    assert character.defense > initial_stats[2]
