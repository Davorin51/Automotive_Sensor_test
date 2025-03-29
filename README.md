# Automotive_Sensor_test
Small testing scripts for Automotive sensor place testing # 🛡️ CAN Safety Project – ADAS Safety Logic Simulation

Ovaj projekt demonstrira osnovnu **ADAS sigurnosnu logiku** temeljem simuliranih CAN podataka, napisanu u **Pythonu**.  
Simulira se rad sustava koji prima podatke o brzini i udaljenosti do prepreke te donosi odluku: **BRAKE**, **WARNING** ili **SAFE**.

---

## 🚗 Kontekst

U stvarnim vozilima, sustavi poput **Forward Collision Warning (FCW)** ili **Autonomous Emergency Braking (AEB)** koriste podatke sa senzora (npr. radar, LIDAR) kako bi detektirali opasnosti i reagirali u stvarnom vremenu.  
Ovaj mini-projekt ilustrira sličan koncept koristeći simulirane podatke preko CAN-like formata.

---

## 📁 Struktura projekta

can_safety_project/ ├── can_safety_project/ │ ├── can_simulator.py # Simulacija CAN poruka │ ├── safety_logic.py # Logika detekcije opasnosti │ ├── init.py │ └── main.py # Demo pokretanje sustava ├── tests/ │ ├── test_safety_logic.py # Pytest testovi logike │ └── init.py ├── README.md

yaml
Copy
Edit

---

## ⚙️ Kako pokrenuti

### 1. Kloniraj repozitorij

```bash
git clone https://github.com/korisnicki-naziv/can_safety_project.git
cd can_safety_project
2. Pokreni demo
bash
Copy
Edit
python3 can_safety_project/main.py
Ispis će pokazati nasumične simulacije brzine, udaljenosti i odluka sustava:

ini
Copy
Edit
[0] Speed=84 km/h | Distance=25.67 m → Action: BRAKE
[1] Speed=42 km/h | Distance=30.22 m → Action: SAFE
🧪 Testiranje
Projekt koristi pytest za testiranje logike odlučivanja.

Pokreni testove:
bash
Copy
Edit
pytest
Pokriveno:
Različite kombinacije brzine i udaljenosti

Očekivano ponašanje sustava: BRAKE, WARNING, SAFE

🧠 Što se može proširiti
Zamijeniti can_simulator.py stvarnim CAN podacima (npr. python-can)

Logirati odluke u .csv za analizu

Integrirati vizualizaciju (npr. matplotlib)

Dodati Dockerfile i CI (npr. GitHub Actions)

🛠️ Tehnologije
Python 3.9+

Pytest (jedini vanjski dependency)

Random modul (za simulaciju senzora)

👨‍💻 Autor
Davorin, FPGA i Automotive inženjer
🔗 LinkedIn | GitHub | Portfolio (dodaj linkove)


