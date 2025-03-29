import pytest
from sensor_project.filtering import remove_outliers

def test_remove_outliers_empty():
    assert remove_outliers([]) == []

def test_remove_outliers_simple():
    data = [10, 11, 12, 100, 11]
    filtered = remove_outliers(data, m=1.5)  # stroži prag
    assert 100 not in filtered
    assert len(filtered) < len(data)

