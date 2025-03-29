import pytest
from sensor_project.sensors import MockSensor, read_sensor_batch

def test_mock_sensor_basic():
    sensor = MockSensor(noise_level=0, base_value=25.0)
    val = sensor.read_distance()
    # Bez noise-a, očekivana vrijednost je 25.0
    assert val == 25.0

def test_read_sensor_batch_length():
    sensor = MockSensor()
    data = read_sensor_batch(sensor, count=5)
    assert len(data) == 5
