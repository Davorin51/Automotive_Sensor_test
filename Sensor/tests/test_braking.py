import pytest
from sensor_project.braking import should_brake, braking_logic

def test_should_brake():
    # distance < threshold -> True
    assert should_brake(10, threshold=20) == True
    # distance >= threshold -> False
    assert should_brake(20, threshold=20) == False

@pytest.mark.parametrize("distance,speed,expected", [
    (10, 60, "BRAKE_HARD"),    # distance < 20 -> brake
    (30, 60, "SLOW_DOWN"),     # distance < 2*20=40 & speed>50 -> slow
    (40, 40, "KEEP_SPEED"),    # distance=40, speed=40 -> keep
    (80, 10, "SPEED_UP"),
])
def test_braking_logic(distance, speed, expected):
    assert braking_logic(distance, speed) == expected
