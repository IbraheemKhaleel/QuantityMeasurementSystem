import logging

from main_quantity_measurement_system.Iquantity_measurement_system import IQuantityMeasurementSystem

logging.basicConfig(filename='quantity_measurement_system.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')


class QuantityMeasurementSystem(IQuantityMeasurementSystem):
    """
    Created a class to compute quantity measurement of length, weight and temperature
    IQuantityMeasurementSystem is the interface
    """

    def length_meter_to_centimeter_conversion(self, input_length):
        """
        :param input_length: The length to be converted which is given by user
        :return: converted centimeter length
        """
        try:
            centi_meter_length = round((input_length * 100), 2)
            logging.debug("centimeter length is {}".format(centi_meter_length))
            return centi_meter_length
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def length_meter_to_kilometer_conversion(self, input_length):
        """
        :param input_length: The length to be converted which is given by user
        :return: converted kilometer length
        """
        try:
            kilo_meter_length = round((input_length * .001), 2)
            logging.debug("kilometer length is {}".format(kilo_meter_length))
            return kilo_meter_length
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def weight_grams_to_kilograms_conversion(self, input_weight):
        """
        :param input_weight: The weight to be converted which is given by user
        :return: converted kilogram weight
        """
        try:
            kilo_gram_weight = round((input_weight * .001), 2)
            logging.debug("kilogram weight is {}".format(kilo_gram_weight))
            return kilo_gram_weight
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')


    def weight_grams_to_milligrams_conversion(self, input_weight):
        """
        :param input_weight: the weight to be converted which is given by user
        :return: converted milligram weight
        """
        try:
            milli_gram_weight = round((input_weight * 1000), 2)
            logging.debug("milli gram weight is {}".format(milli_gram_weight))
            return milli_gram_weight
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_celsius_to_fareheit(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted fahrenheit temperature
        """
        try:
            fahrenheit_temperature = round((((9 / 5) * input_temperature) + 32), 2)
            logging.debug("fahrenheit temperature is {}".format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_farenheit_to_celsius(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted celsius temperature
        """
        try:
            celsius_temperature = round(((input_temperature - 32) * (5 / 9)), 2)
            logging.debug("celsius temperature is {}".format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_celsius_to_kelvin(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted kelvin temperature
        """
        try:
            kelvin_temperature = round((input_temperature + 273.15), 2)
            logging.debug("kelvin temperature is {}".format(kelvin_temperature))
            return kelvin_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_kelvin_to_celsius(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted celsius temperature
        """
        try:
            celsius_temperature = round((input_temperature - 273.15), 2)
            logging.debug("celsius temperature is {}".format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_fahrenheit_to_kelvin(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted kelvin temperature
        """
        try:
            kelvin_temperature = round(((input_temperature - 32) * (5 / 9)) + 273.15, 2)
            logging.debug("kelvin temperature is {}".format(kelvin_temperature))
            return kelvin_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_kelvin_to_fahrenheit(self, input_temperature):
        """
         :param input_temperature: The temperature to be converted which is given by user
        :return: converted fahrenheit temperature
        """
        try:
            fahrenheit_temperature = round(((input_temperature - 273.15) * (9 / 5)) + 32, 2)
            logging.debug("fahrenheit temperature is {}".format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')