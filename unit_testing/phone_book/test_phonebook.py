from unittest import TestCase
from phonebook import PhoneBook


class TestPhoneBook(TestCase):
    def setUp(self):
        # Begining of every test
        self.phonebook = PhoneBook()

    def tearDown(self):
        # End of every test
        pass

    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_entry_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_enteries_is_consistent(self):
        self.phonebook.add("Bob", "123456")
        self.phonebook.add("Marry", "986780")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_enteries_is_not_consistent(self):
        self.phonebook.add("Bob", "123456")
        self.phonebook.add("Marry", "123456")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_similar_prefix_is_not_consistent(self):
        self.phonebook.add("Bob", "123456")
        self.phonebook.add("Marry", "123")
        self.assertFalse(self.phonebook.is_consistent())
