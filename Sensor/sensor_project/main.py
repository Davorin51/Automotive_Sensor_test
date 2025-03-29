from sensor_project.sensors import MockSensor, read_sensor_batch
from sensor_project.filtering import remove_outliers
from sensor_project.braking import braking_logic

def main():
    # 1. Inicijaliziramo mock senzor (npr. distance sensor).
    sensor = MockSensor(noise_level=1.0, base_value=25.0)

    # 2. Uzmimo batch podataka
    data = read_sensor_batch(sensor, count=10)
    print("Raw sensor data:", data)

    # 3. Filtriraj outliere
    filtered_data = remove_outliers(data, m=2)
    print("Filtered data:", filtered_data)

    # 4. Pretpostavimo da uzmemo zadnju izmjeru distance
    current_distance = filtered_data[-1] if filtered_data else 100.0

    # 5. Zamisli da je trenutna brzina 60 km/h
    speed = 60
    action = braking_logic(current_distance, speed)
    print(f"Distance={current_distance:.2f}, Speed={speed}, Action={action}")

if __name__ == "__main__":
    main()
