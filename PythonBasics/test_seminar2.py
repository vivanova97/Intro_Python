import seminar2 
import unittest
import fractions

class Seminar2TestCase(unittest.TestCase):
    def test_number_to_hex(self):
        result = '0x'+ seminar2.convert_number_to_hex()
        self.assertEqual(result, hex(seminar2.number_input()))
    def test_sum_fractions(self):
        result = seminar2.sum_fractions()
        first_fraction_numerator, first_fraction_denominator, second_fraction_numerator, \
        second_fraction_denominator = seminar2.fraction_input()
        self.assertEqual(fractions.Fraction(result), fractions.Fraction(first_fraction_numerator,first_fraction_denominator) \
        + fractions.Fraction(second_fraction_numerator, second_fraction_denominator))

if __name__ == "__main__":
    unittest.main()

