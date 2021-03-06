import pytest


@pytest.mark.parametrize("input, output", [(20, 20 * 100), (2, 2 * 100), (3, 3 * 100), (45, 45 * 100), (35, 35 * 100)])
def test_length_meter_to_centimeter_conversion(input, output, instance_of_main_class):
    result = instance_of_main_class.length_meter_to_centimeter_conversion(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(10, 10 * .001), (2000, 2000 * .001), (6000, 6), (5000, 5)])
def test_length_meter_to_kilometer_conversion(input, output, instance_of_main_class):
    result = instance_of_main_class.length_meter_to_kilometer_conversion(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(5000, 5), (2000, 2), (56000, 56), (8658, 8.66)])
def test_weight_grams_to_kilograms_conversion(input, output, instance_of_main_class):
    result = instance_of_main_class.weight_grams_to_kilograms_conversion(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(2, 2000), (8, 8000), (63, 63000), (8.963, 8963)])
def test_weight_grams_to_milligrams_conversion(input, output, instance_of_main_class):
    result = instance_of_main_class.weight_grams_to_milligrams_conversion(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(37, 98.6), (48, 118.4), (52, 125.6), (14, 57.2)])
def test_temperature_celsius_to_farenheit(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_celsius_to_fareheit(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(102, 38.89), (887, 475), (63, 17.22), (145, 62.78)])
def test_temperature_farenheit_to_celsius(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_farenheit_to_celsius(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(6, 6 + 273.15), (80, 80 + 273.15), (63, 63 + 273.15), (29, 29 + 273.15)])
def test_temperature_celsius_to_kelvin(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_celsius_to_kelvin(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(8 + 273.15, 8), (5 + 273.15, 5), (89 + 273.15, 89), (24 + 273.15, 24)])
def test_temperature_celsius_to_kelvin(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_kelvin_to_celsius(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(11, 261.48), (96, 308.71), (75, 297.04), (35, 274.82)])
def test_temperature_fahrenheit_to_kelvin(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_fahrenheit_to_kelvin(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(85, -306.67), (415, 287.33), (91, -295.87), (214, -74.47)])
def test_temperature_kelvin_to_fahrenheit(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_kelvin_to_fahrenheit(input)
    assert result == output
