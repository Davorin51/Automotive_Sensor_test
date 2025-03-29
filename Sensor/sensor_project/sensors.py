import random

class MockSensor:
    """
    Klasa koja simulira senzor – npr. mjeri udaljenost u metrima.
    U realnom slučaju, ovdje bi bio driver ili serial komunikacija.
    """

    def __init__(self, noise_level=0.5, base_value=25.0):
        self.noise_level = noise_level
        self.base_value = base_value

    def read_distance(self):
        """
        Vraća 'izmjerenu' udaljenost – base_value +/- nasumični šum.
        """
        noise = (random.random() - 0.5) * 2 * self.noise_level
        return self.base_value + noise

def read_sensor_batch(sensor, count=10):
    """
    Napravi batch očitanja s danog senzora.
    """
    data = []
    for _ in range(count):
        data.append(sensor.read_distance())
    return data
