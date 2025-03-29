import pytest
from can_safety_project.safety_logic import assess_situation

@pytest.mark.parametrize("speed, distance, expected", [
    (100, 30, "BRAKE"),     # daleko ispod sigurnog
    (100, 45, "WARNING"),   # ispod sigurne, ali nije kritično
    (100, 60, "SAFE"),      # iznad sigurne udaljenosti
    (50, 24, "WARNING"),
    (50, 10, "BRAKE"),
    (50, 30, "SAFE"),
])
def test_assess_situation(speed, distance, expected):
    assert assess_situation(speed, distance) == expected
