from math import gcd

class Person:
    def __init__(self):
        self._full_name = ""
        self._birth_date = ""
        self._phone = ""
        self._city = ""
        self._country = ""
        self._address = ""

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not value.strip():
            raise ValueError("Full name cannot be empty")
        self._full_name = value.strip()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def input_data(self):
        self.full_name  = input("ПІБ: ")
        self.birth_date = input("Дата народження (дд.мм.рррр): ")
        self.phone      = input("Телефон: ")
        self.city       = input("Місто: ")
        self.country    = input("Країна: ")
        self.address    = input("Адреса: ")

    def display(self):
        print("=" * 35)
        print(f"  ПІБ:      {self.full_name}")
        print(f"  Дата:     {self.birth_date}")
        print(f"  Телефон:  {self.phone}")
        print(f"  Місто:    {self.city}")
        print(f"  Країна:   {self.country}")
        print(f"  Адреса:   {self.address}")
        print("=" * 35)

    def __str__(self):
        return f"Person({self.full_name}, {self.city}, {self.country})"

person = Person()
person.input_data()
person.display()
print(person)