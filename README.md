# 🚗 ADAS Mini Projects – Sensor & Communication Safety Logic

Ovaj repozitorij sadrži dva mini Python projekta razvijena u kontekstu **automotive inženjerstva**, posebno za **ADAS (Advanced Driver Assistance Systems)** i **real-time obradu podataka**.

Cilj ovih projekata je demonstrirati:
- Rad sa simuliranim senzorima
- Obradu i filtriranje podataka
- Jednostavne sigurnosne algoritme
- Simulaciju CAN komunikacije
- Testiranje pomoću `pytest`

---

## 📁 Struktura repozitorija

```bash
Projekt_Test/
├── Sensor/             ← Projekt za obradu senzorskih podataka i logiku kočenja
│   ├── sensor_project/
│   ├── tests/
│   ├── README.md
│   ├── setup.py
│   └── requirements.txt
│
├── Communication/      ← Projekt za simulaciju CAN poruka i sigurnosnu procjenu
│   ├── can_safety_project/
│   ├── tests/
│   └── README.md (dodati)
🔍 Projekti
🧪 Sensor Project – Outlier Filtering & Braking Logic
📍 Lokacija: Sensor/sensor_project/

Opis:

Simulira rad senzora udaljenosti

Filtrira ekstremne vrijednosti (remove_outliers)

Odluka o kočenju na temelju filtriranih podataka (braking_logic)

Pokriveno pytest testovima

🔧 Pokretanje:

bash
Copy
Edit
python3 sensor_project/main.py
pytest
📡 Communication Project – CAN Safety Logic
📍 Lokacija: Communication/can_safety_project/

Opis:

Simulira CAN poruke (brzina i udaljenost)

Odluka: SAFE, WARNING, BRAKE

Utemeljeno na jednostavnoj formuli sigurne udaljenosti

Testirano s pytest

🔧 Pokretanje:

bash
Copy
Edit
python3 can_safety_project/main.py
pytest
🛠 Tehnologije
Python 3.9+

Pytest

Modularna struktura (projekti + testovi)

Jednostavne simulacije stvarnih situacija u vozilima
