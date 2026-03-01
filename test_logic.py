import pytest
from unittest.mock import patch
import logic

#1
def test_length():
    with patch("logic.random.randint", return_value=3) as mock_rand:
        result = logic.RNGenerator()

        # checking length
        assert len(result) == 5

        # call count
        assert mock_rand.call_count == 5


def test_RNGenerator_value_range():
    # checking randomness
    result = logic.RNGenerator()

    # checking 1 <= x <= 6
    for value in result:
        assert 1 <= value <= 6


#2
# checking if list is non-empty
def test_empty_list():
    assert logic.validity([]) is False


# checking validity
def test_valid_input():
    assert logic.validity([0, 1, 3, 5]) is True


# value greater than 5 should fail
def test_validity_out_of_range_high():
    assert logic.validity([1, 2, 6]) is False


# Negative value should fail
def test_validity_out_of_range_low():
    assert logic.validity([-1, 2, 3]) is False


# 0 and 5 are allowed
def test_validity_boundary_values():
    assert logic.validity([0, 5]) is True



#3
def test_userIN_valid():
    # user types 123
    with patch("builtins.input", return_value="123"):
        result = logic.userIN()
        assert result == [1, 2, 3]


def test_userIN_empty():
    # user presses enter
    with patch("builtins.input", return_value=""):
        result = logic.userIN()
        assert result == []


def test_userIN_invalid():
    # contains other character
    with patch("builtins.input", return_value="1a3"):
        result = logic.userIN()
        assert result == []


# hexcomp

def test_replace():
    pos = [1]  # keep position 1
    RNG = [6, 6, 6, 6, 6]
    copybar = [1, 2, 3, 4, 5]

    result = logic.hexcomp(pos, RNG, copybar)

    # position 1 remains unchanged
    assert result[0] == 1

    # other positions replaced by RNG
    assert result[1:] == [6, 6, 6, 6]


def test_all_positions():
    pos = [1, 2, 3, 4, 5]  # keep everything
    RNG = [6, 6, 6, 6, 6]
    copybar = [1, 2, 3, 4, 5]

    result = logic.hexcomp(pos, RNG, copybar)

    # nothing should change
    assert result == [1, 2, 3, 4, 5]


def test_keep_none():
    pos = []  # keep nothing
    RNG = [6, 6, 6, 6, 6]
    copybar = [1, 2, 3, 4, 5]

    result = logic.hexcomp(pos, RNG, copybar)

    # everything replaced
    assert result == [6, 6, 6, 6, 6]


# SingleRound
import logic
from unittest.mock import patch


def test_SingleRound_basic_flow():

    # fake dice rolls for 3 rounds
    fake_rolls = [
        [1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3]
    ]

    with patch("logic.RNGenerator", side_effect=fake_rolls), \
         patch("logic.userIN", return_value=[1]), \
         patch("logic.validity", return_value=True), \
         patch("logic.ndice") as mock_display:

        result = logic.SingleRound()

        # return last computed dice state
        assert isinstance(result, list)
        assert len(result) == 5

        # RNGenerator should be called 3 times
        assert logic.RNGenerator.call_count == 3

        # ndice should be called 3 times
        assert mock_display.call_count == 3


def test_SRvalidity():
    with patch("logic.RNGenerator", return_value=[1,1,1,1,1]), \
         patch("logic.userIN", side_effect=[[], [1], [1]]), \
         patch("logic.validity", side_effect=[False, True, True]), \
         patch("logic.ndice"), \
         patch("builtins.print") as mock_print:

        result = logic.SingleRound()

        assert isinstance(result, list)
        assert len(result) == 5

        mock_print.assert_any_call("Invalid. Try again.")
