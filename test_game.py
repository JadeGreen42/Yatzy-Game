from unittest.mock import patch
import game

def test_run_game():

    fake_dice = [1,1,1,1,1]

    # return same dice
    with patch('game.SingleRound', return_value=fake_dice):

        # return score 5, and flag True for minisum
        with patch('game.scoring', return_value=(5, True)):

            # provide 13 valid choices
            with patch('builtins.input', side_effect=[1,2,3,4,5,6,7,8,9,10,11,12,13]):

                # select slots in order
                game.slots = {i: f"slot{i}" for i in range(1,14)}

                total = game.run_game()

                # 13 rounds * 5 points each = 65 + bonus 35 = 100
                assert total == 100