from can_safety_project.can_simulator import generate_can_message
from can_safety_project.safety_logic import assess_situation

def main():
    for i in range(10):
        msg = generate_can_message()
        action = assess_situation(msg["speed_kmh"], msg["distance_m"])
        print(f"[{i}] Speed={msg['speed_kmh']} km/h | Distance={msg['distance_m']} m → Action: {action}")

if __name__ == "__main__":
    main()
