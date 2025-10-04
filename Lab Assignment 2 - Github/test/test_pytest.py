import pytest
from src import temp_converter

def test_to_celsius():
    assert round(temp_converter.to_celsius(32), 2) == 0
    assert round(temp_converter.to_celsius(212), 2) == 100
    assert round(temp_converter.to_celsius(98.6), 1) == 37.0
    with pytest.raises(ValueError):
        temp_converter.to_celsius("abc")

def test_to_fahrenheit():
    assert round(temp_converter.to_fahrenheit(0), 1) == 32.0
    assert round(temp_converter.to_fahrenheit(100), 1) == 212.0
    assert round(temp_converter.to_fahrenheit(37), 1) == 98.6
    with pytest.raises(ValueError):
        temp_converter.to_fahrenheit(None)

def test_avg_temp_converter():
    assert temp_converter.avg_temp_converter([0, 10, 20]) == 10
    assert round(temp_converter.avg_temp_converter([32, 212]), 1) == 122.0
    with pytest.raises(ValueError):
        temp_converter.avg_temp_converter([30, "hot", 50])
    
