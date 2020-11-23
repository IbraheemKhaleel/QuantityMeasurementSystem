
from abc import abstractmethod, ABC


class IQuantityMeasurementSystem(ABC):
    """
    Creating an interface to declare the methods defined in QuantityMeasurementSystem class
    """
    @abstractmethod
    def length_meter_to_centimeter_conversion(self, input_length):
        pass

    @abstractmethod
    def length_meter_to_kilometer_conversion(self, input_length):
        pass

    @abstractmethod
    def weight_grams_to_kilograms_conversion(self, input_weight):
        pass

    @abstractmethod
    def weight_grams_to_milligrams_conversion(self, input_weight):
        pass

    @abstractmethod
    def temperature_celsius_to_fareheit(self, input_temperature):
        pass

    @abstractmethod
    def temperature_farenheit_to_celsius(self, input_temperature):
        pass

    @abstractmethod
    def temperature_celsius_to_kelvin(self, input_temperature):
        pass

    @abstractmethod
    def temperature_kelvin_to_celsius(self, input_temperature):
        pass

    @abstractmethod
    def temperature_fahrenheit_to_kelvin(self, input_temperature):
        pass

    @abstractmethod
    def temperature_kelvin_to_fahrenheit(self, input_temperature):
        pass
