from project import computer_choice , player_choice, determine_winner
import pytest

def test_computer_choice():
    assert computer_choice() in ["rock", "paper", "scissors"]

def test_player_choice():
    assert player_choice("rock") == "rock"
    assert player_choice("paper") =="paper"
    assert player_choice("scissors") =="scissors"
    with pytest.raises(ValueError):
         player_choice("54487845")
    with pytest.raises(ValueError):
         player_choice("✌")

def test_determine_winner():
    assert determine_winner("rock","rock") == "draw"
    assert determine_winner("rock","scissors") == "player"
    assert determine_winner("rock","paper") == "computer"


