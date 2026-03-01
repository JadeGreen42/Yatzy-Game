from scoring import scoring
import pytest

# 1 to 6
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([2,3,4,5,6], 0),      # none
        ([1,2,3,4,6], 1),      # one of 1
#        ([1,2,3,4,6], 6),      # one of 6
        ([1,1,1,1,1], 5),      # yatzy
    ],
)

# 1 to 6
def test_category_1to6(dice,expected):
    assert scoring(1, dice)[0] == expected


# 3 of a kind
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,2,3], 8),      # exactly 3
        ([1,2,3,4,6], 0),      # none
        ([6,6,6,2,2], 22),     # full house
        ([3,3,3,3,4], 16),     # four of a kind
    ],
)
def test_3_of_a_kind(dice, expected):
    assert scoring(7, dice)[0] == expected


# 4 of a kind
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,2,3], 0),      # < 4
        ([1,1,1,1,3], 7),      # exactly 4
        ([6,6,6,6,6], 30),     # yatzy
    ],
)

def test_4_of_a_kind(dice, expected):
    assert scoring(8, dice)[0] == expected


# full house
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,2,3,4,5], 0),      # none
        ([1,1,1,2,2], 25),     # full house
        ([3,3,3,3,4], 0),      # four of a kind
        ([6,6,6,6,6], 0),      # yatzy
    ],
)

def test_fullhouse(dice, expected):
        assert scoring(9, dice)[0] == expected


# small
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,1,1], 0),      # none
        ([1,1,1,2,3], 0),      # near miss
        ([1,2,3,4,6], 30),     # small
        ([1,2,3,4,5], 30),     # large
    ],
)

def test_small(dice, expected):
        assert scoring(10, dice)[0] == expected


# large
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,1,1], 0),      # none
        ([1,2,3,4,6], 0),     # near miss
        ([1,2,3,4,5], 40),     # large
    ],
)

def test_large(dice, expected):
        assert scoring(11, dice)[0] == expected


# yatzy
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,1,5], 0),     # near miss
        ([1,1,1,1,1], 50),    # yatzy
        ([1,2,3,4,5], 0),     # ranodm
    ],
)

def test_yatzy(dice, expected):
        assert scoring(12, dice)[0] == expected


# chance
@pytest.mark.parametrize(
    "dice, expected",
    [
        ([1,1,1,1,1], 5),      # min
        ([1,2,3,4,5], 15),     # random
        ([6,6,6,6,6], 30),     # max
    ],
)

def test_chance(dice, expected):
        assert scoring(13, dice)[0] == expected


# ordering
def test_order():
    dice = [3,3,3,4,5]
    shuffled = [5,3,4,3,3]

    for category in range(1, 14):
        assert scoring(category, dice)[0] == scoring(category, shuffled)[0]