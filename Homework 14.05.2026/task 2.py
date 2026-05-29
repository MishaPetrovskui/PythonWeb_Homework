from math import gcd

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator   = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Numerator must be an integer")
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("Denominator must be an integer")
        if value == 0:
            raise ValueError("Denominator cannot be zero")
        self._denominator = value

    def reduce(self):
        common = gcd(abs(self._numerator), abs(self._denominator))
        return Fraction(self._numerator // common, self._denominator // common)

    def input_data(self):
        self.numerator   = int(input("Чисельник: "))
        self.denominator = int(input("Знаменник: "))

    def display(self):
        reduced = self.reduce()
        print(f"  Дріб: {self}  →  {reduced} (скорочений)")

    def __add__(self, other):
        n = self._numerator * other._denominator + other._numerator * self._denominator
        d = self._denominator * other._denominator
        return Fraction(n, d).reduce()

    def __sub__(self, other):
        n = self._numerator * other._denominator - other._numerator * self._denominator
        d = self._denominator * other._denominator
        return Fraction(n, d).reduce()

    def __mul__(self, other):
        return Fraction(self._numerator * other._numerator,
                        self._denominator * other._denominator).reduce()

    def __truediv__(self, other):
        if other._numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        return Fraction(self._numerator * other._denominator,
                        self._denominator * other._numerator).reduce()

    def __eq__(self, other):
        a, b = self.reduce(), other.reduce()
        return a._numerator == b._numerator and a._denominator == b._denominator

    def __lt__(self, other):
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"


a = Fraction()
print("=== Дріб A ===")
a.input_data()
a.display()

b = Fraction()
print("=== Дріб B ===")
b.input_data()
b.display()

print(f"\nA + B = {a + b}")
print(f"A - B = {a - b}")
print(f"A * B = {a * b}")
print(f"A / B = {a / b}")
print(f"A == B: {a == b}")
print(f"A < B:  {a < b}")