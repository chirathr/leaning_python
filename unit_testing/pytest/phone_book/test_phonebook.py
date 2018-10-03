from phonebook import PhoneBook


def test_add_and_lookup_entry():
    phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")

def test_phonebook_gives_access_to_names_and_numbers():
    phonebook = PhoneBook()
    phonebook.add("Alice", "67890")
    assert "Alice" in phonebook.names()
    assert "67890" in phonebook.numbers()
