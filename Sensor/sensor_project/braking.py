def should_brake(distance, threshold=20.0):
    """
    Vrati True ako treba odmah zakočiti jer je udaljenost < threshold.
    """
    return distance < threshold

def braking_logic(distance, speed, threshold=20.0):
    """
    Prošireni primjer “braking logic”:
      - Ako je distance < threshold -> “BRAKE_HARD”
      - Ako je distance < 2*threshold i speed > 50 -> “SLOW_DOWN”
      - Inače -> “KEEP_SPEED”
    """
    if distance < threshold:
        return "BRAKE_HARD"
    elif distance < 2 * threshold and speed > 50:
        return "SLOW_DOWN"
    elif distance > 2 * threshold and speed > 9:
        return "SPEED_UP"
    else:
        return "KEEP_SPEED"
