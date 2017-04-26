import unittest
import anonymize as ano

class TestAnonymizeEmails(unittest.TestCase): 

	def test_email_1(self):
		self.help_test_email("kinoue@syr.edu", "[Email (14)]",
			"Should anonymize the email-only text.")

	def test_email_2(self):
		self.help_test_email("k.inoue@ashisuto.co.jp kinoue@syr.edu", "[Email (22)] [Email (14)]",
			"Should anonymize multiple email sequences in a row.")

	def test_email_3(self):
		self.help_test_email("My email: k.inoue@ashisuto.co.jp", "My email: [Email (22)]",
			"Should anonymize emails after some text.")

	def test_email_4(self):
		self.help_test_email("k.inoue@ashisuto.co.jp is my email.", "[Email (22)] is my email.")

	def help_test_email(self, old_text, correct_text, description=None):
		new_text = ano.anonymize_emails(old_text) 
		self.assertEqual(new_text, correct_text, description)


if __name__ == '__main__':
	unittest.main()
