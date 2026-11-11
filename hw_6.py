from collections import UserDict

class Field:
    """Base class for record fields."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for storing the contact name. Mandatory field."""
    pass


class Phone(Field):
    """Class for storing a phone number with validation (must be 10 digits)."""
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    """Class for storing contact information, including name and a list of phones."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """Adds a phone number to the record."""
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """Removes a phone number from the record."""
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        """Edits an existing phone number, raises ValueError if validation fails or old phone is not found."""
        phone_obj = self.find_phone(old_phone)
        if not phone_obj:
            raise ValueError("Old phone number not found.")
        # Validate and update using Phone class logic
        new_phone_obj = Phone(new_phone)
        phone_obj.value = new_phone_obj.value

    def find_phone(self, phone_number):
        """Finds and returns a Phone object if it exists in the record, otherwise None."""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class for storing and managing records."""
    def add_record(self, record):
        """Adds a record to self.data using record.name.value as the key."""
        self.data[record.name.value] = record

    def find(self, name):
        """Finds and returns a Record object by name, or None if not found."""
        return self.data.get(name)

    def delete(self, name):
        """Deletes a record by name from the address book."""
        if name in self.data:
            del self.data[name]

    def __str__(self):
        """Returns a string representation of all records in the address book."""
        return "\n".join(str(record) for record in self.values())



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane") 

# Виведення всіх записів у книзі
print(book)

