class Money:
    def __init__(self, units=0, cents=0):
        self.units = units
        self.cents = cents

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Units must be a non-negative integer")
        self._units = value

    @property
    def cents(self):
        return self._cents

    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or not (0 <= value <= 99):
            raise ValueError("Cents must be an integer between 0 and 99")
        self._cents = value

    def to_cents(self):
        return self._units * 100 + self._cents

    def input_data(self):
        self.units = int(input("Гривні: "))
        self.cents = int(input("Копійки (0-99): "))

    def display(self):
        print(f"  Сума: {self._units} грн {self._cents:02d} коп")

    def __add__(self, other):
        total = self.to_cents() + other.to_cents()
        return Money(total // 100, total % 100)

    def __sub__(self, other):
        total = self.to_cents() - other.to_cents()
        if total < 0:
            raise ValueError("Result cannot be negative")
        return Money(total // 100, total % 100)

    def __eq__(self, other):
        return self.to_cents() == other.to_cents()

    def __lt__(self, other):
        return self.to_cents() < other.to_cents()

    def __str__(self):
        return f"{self._units} грн {self._cents:02d} коп"

    def __repr__(self):
        return f"Money({self._units}, {self._cents})"


class Product(Money):
    def __init__(self, name="Item", units=0, cents=0):
        super().__init__(units, cents)
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    def discount(self, amount):
        if not isinstance(amount, Money):
            raise TypeError("Discount must be a Money instance")
        if amount.to_cents() > self.to_cents():
            raise ValueError("Discount cannot exceed the price")
        total = self.to_cents() - amount.to_cents()
        self.units = total // 100
        self.cents = total % 100

    def input_data(self):
        self.name = input("Назва товару: ")
        super().input_data()

    def display(self):
        print("=" * 35)
        print(f"  Товар: {self._name}")
        print(f"  Ціна:  {self._units} грн {self._cents:02d} коп")
        print("=" * 35)

    def __str__(self):
        return f"{self._name}: {self._units} грн {self._cents:02d} коп"

    def __repr__(self):
        return f"Product('{self._name}', {self._units}, {self._cents})"


product = Product()
product.input_data()
product.display()

discount = Money()
print("--- Знижка ---")
discount.input_data()

product.discount(discount)
print("Після знижки:")
product.display()