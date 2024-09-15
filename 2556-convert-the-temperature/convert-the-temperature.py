class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        num_to_kelvin = celsius + 273.15
        num_to_fahrenheit = celsius * 1.80 + 32.00
        res = [num_to_kelvin, num_to_fahrenheit]
        return res