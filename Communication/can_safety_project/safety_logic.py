def calculate_safe_distance(speed_kmh):
    """
    Na temelju brzine, izračunaj minimalnu sigurnu udaljenost:
    - Koristimo jednostavni model: safe_dist = speed / 2 (u metrima)
    """
    return speed_kmh / 2.0

def assess_situation(speed_kmh, distance_m):
    """
    Vrati:
    - "BRAKE" ako je opasno blizu
    - "WARNING" ako je na granici
    - "SAFE" ako je sigurno
    """
    safe_distance = calculate_safe_distance(speed_kmh)

    if distance_m < safe_distance * 0.8:
        return "BRAKE"
    elif distance_m < safe_distance:
        return "WARNING"
    else:
        return "SAFE"
