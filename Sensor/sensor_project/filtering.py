import statistics

def remove_outliers(data, m=2):
    """
    Uklanja vrijednosti iz list 'data' koje su izvan mean ± m*std.
    """
    if not data:
        return data
    
    mean_val = statistics.mean(data)
    stdev = statistics.pstdev(data)  # sample stdev (ili pstdev za populaciju)

    filtered = []
    for val in data:
        if abs(val - mean_val) <= m * stdev:
            filtered.append(val)
    return filtered
