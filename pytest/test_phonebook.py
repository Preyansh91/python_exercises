import unittest
import phonebook
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

	def setUp(self):
		self.phonebook = Phonebook()

	def test_lookup_entry_by_name(self):
		self.phonebook.add("Bob","12345")
		self.assertEqual("12345",self.phonebook.lookup("Bob"))

	def test_missing_entry_raises_KeyError(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup("missing")				
	
							                     #work in progress"
	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())			
		
	
	def test_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("Bob","12345")
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("Mary","012345")
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("Sue","123")
		self.assertTrue(self.phonebook.is_consistent())	
		self.phonebook.add("Sue","123")
                self.assertTrue(self.phonebook.is_consistent())
