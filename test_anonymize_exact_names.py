import unittest
import anonymize as ano

class TestAnonymizeNames(unittest.TestCase): 

	def test_name_1(self):
		self.help_test_name("Jennifer", "[Name (8)]",
			"Should anonymize the name-only text.")

	def test_name_2(self):
		self.help_test_name("Mike, Scott, Eddie", "[Name (4)], [Name (5)], [Name (5)]",
			"Should anonymize multiple name sequences in a row.")

	def test_name_3(self):
		self.help_test_name("My name is Sarah Inoue", "My name is [Name (5)] Inoue",
			"Should anonymize names after some text.")

	def test_name_4(self):
		self.help_test_name("Alex is my name.", "[Name (4)] is my name.")

	def test_name_5(self):
		self.help_test_name("My name is sarah", "My name is [Name (5)]",
			"Should anonymize lower-cased names after some text.")

	def help_test_name(self, old_text, correct_text, description=None):
		new_text = ano.anonymize_exact_names(old_text) 
		self.assertEqual(new_text, correct_text, description)


if __name__ == '__main__':
	unittest.main()
