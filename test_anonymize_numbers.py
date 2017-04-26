import unittest
import anonymize as ano

class TestAnonymizeNumbers(unittest.TestCase): 

	def test_number_1(self):
		self.help_test_number("1111", "[Number (4)]",
			"Should anonymize the number-only text.")

	def test_number_2(self):
		self.help_test_number("1111 1244", "[Number (4)] [Number (4)]",
			"Should anonymize multiple number sequences in a row.")

	def test_number_3(self):
		self.help_test_number("My pin: 1234", "My pin: [Number (4)]",
			"Should anonymize numbers after some text.")

	def test_number_4(self):
		self.help_test_number("2017 is a good year.", "[Number (4)] is a good year.")

	def help_test_number(self, old_text, correct_text, description=None):
		new_text = ano.anonymize_numbers(old_text) 
		self.assertEqual(new_text, correct_text, description)



if __name__ == '__main__':
	unittest.main()
