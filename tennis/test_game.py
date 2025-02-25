import pytest
from tennis.player import Player
from tennis.game import Game

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# print("Current sys.path:", sys.path)


# Test for valid cases
@pytest.mark.parametrize(
    "player1_score, player2_score, expected_result",
    [
        (4, 4, "Deuce"),  
        (3, 3, "Deuce"), 
        (9, 9, "Deuce"), 
        (6, 4, "Win for Player1"),  
        (3, 5, "Win for Player2"), 
        (4, 3, "Advantage for Player1"),  
        (3, 4, "Advantage for Player2"),  
        (3, 0, "Forty-Love"),
        (2, 1, "Thirty-Fifteen"),
        (1, 4, "Win for Player2"),
        (5, 4, "Advantage for Player1")
    ]
)
def test_valid_cases(player1_score, player2_score, expected_result):

    # mock players
    player1 = Player(name="Player1", score=player1_score)
    player2 = Player(name="Player2", score=player2_score)

    # the game object
    game = Game(player1, player2)

    result = game.calculate_score()
    assert result == expected_result


# Test for invalid cases
@pytest.mark.parametrize(
    "player1_score, player2_score, expected_exception",
    [
        (5, 0, ValueError),  
        (6, 2, ValueError), 
        (4, 7, ValueError), 
        (4, None, Exception),   
    ]
)

def test_invalid_cases(player1_score, player2_score, expected_exception):

    player1 = Player(name="Player1", score=player1_score)
    player2 = Player(name="Player2", score=player2_score)


    game = Game(player1, player2)

    with pytest.raises(expected_exception):
        game.calculate_score()