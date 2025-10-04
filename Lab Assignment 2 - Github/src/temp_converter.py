def to_celsius(fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
    Returns:
        float: Temperature in Celsius.
    Raises:
        ValueError: If input is not a number.
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5 / 9



def to_fahrenheit(celsius):
    """
    Converts temperature from Celsius to Fahrenheit.
    Args:
        celsius (float): Temperature in Celsius.
    Returns:
        float: Temperature in Fahrenheit.
        Raises:
        ValueError: If input is not a number.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return (celsius * 9 / 5) + 32


def avg_temperature(temps):
    """
    Computes average temperature from a list.
    Args:
        temps (list[float]): List of temperature values.
    Returns:
        float: Average temperature.
    Raises:
        ValueError: If any element is not a number.
    """
    if not all(isinstance(t, (int, float)) for t in temps):
        raise ValueError("All elements must be numbers.")
    return sum(temps) / len(temps)

print(avg_temperature((100,120)))
