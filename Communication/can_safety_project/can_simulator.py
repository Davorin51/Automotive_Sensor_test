import random

def generate_can_message():
    """
    Simulira primanje CAN poruke s dva signala:
    - brzina vozila [km/h]
    - udaljenost do prepreke [m]
    """
    speed = random.randint(0, 120)        # npr. 0 - 120 km/h
    distance = random.uniform(5.0, 100.0)  # npr. 5 - 100 m
    return {
        "speed_kmh": speed,
        "distance_m": round(distance, 2)
    }
