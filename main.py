from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if int(value) and len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        print(str(phone))

    def remove_phone(self, phone):
        print(type(self.phones))
        print(type(phone))
        print(self.phones)
        print(list(self.phones))
        print(phone)

        try:
            for p in self.phones:
                if str(p) == phone:
                    print('сработало')
                    self.phones.remove(p)
        except:
            pass
    def edit_phone(self, phone_old, phone_new):

        for p in self.phones:
            
            if phone_old == str(p):
                self.phones[self.phones.index(p)] = Phone(phone_new)

                return None

        raise ValueError

    def find_phone(self, phone):

        for p in self.phones:
            if str(p) == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
# а нащо взагалі потрібен був p.value???
class AddressBook(UserDict):
    # def add_record(self, n_and_c):
    #     self.data[str(n_and_c.name)] = n_and_c.phones
    #     print(n_and_c.name, 'penis')

    def add_record(self, n_and_c):
        self.data[str(n_and_c.name.value)] = n_and_c

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            pass

    def delete(self, name):
        try:
            del self.data[name]
        except:
            pass

# Створення нової адресної книги

# book = AddressBook()
#
# # Створення запису для John
# john_record = Record("John")
# print(john_record, 'qweqweqweqweqweqwe')
# print(type(john_record))
# john_record.add_phone("12345")
# john_record.add_phone("5555555555")
#
# # Додавання запису John до адресної книги
# book.add_record(john_record)
# print(book)
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
# for name, record in book.data.items():
#     print(record)
#
#
# john = book.find("John")
#
# john.edit_phone("1234567890", "1112223333")
# print(john, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
