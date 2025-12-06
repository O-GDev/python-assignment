import unittest
import temperature_threshold
from redigestion import  check_vowel

class test_temperature_threshold(unittest.TestCase):
#    def test_check_if_function_exist(self):
#        temperature_threshold.temperature_converter(-10, "c", 200)
#
#    def test_check_if_threshold_less_than_zero(self):
#        expected = "Hot alert"
#        actual = temperature_threshold.temperature_converter(40, "c", -100)
#        self.assertEqual(actual,expected)
#
#    def test_check_if_temperature_less_than_zero(self):
#        expected = "Cold advisory"
#        actual = temperature_threshold.temperature_converter(40, "c", 100)
#        self.assertEqual(actual,expected)
#
#    def test_check_if_threshold_less_than_zero_and_temperature(self):
#        expected = "Cold advisory"
#        actual = temperature_threshold.temperature_converter(-40, "c", -100)
#        self.assertEqual(actual,expected)
#
#    def test_check_if_threshold_less_than_zero_and_temperature(self):
#        expected = "Cold advisory"
#        actual = temperature_threshold.temperature_converter(40, "c", -100)
#        self.assertEqual(actual,expected)
#
#    def test_check_if_threshold_less_than_zero_and_temperature(self):
#        expected = "Cold advisory"
#        actual = temperature_threshold.temperature_converter(40, "c", -100)
#        self.assertEqual(actual,expected)


    def test_count_the_number_of_vowels_in_word(self):
        given = "Papaya"
        when = check_vowel(given)
        expected = 1
        self.assertEqual(expected, when)
    
    def test_

        
