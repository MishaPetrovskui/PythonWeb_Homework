# Завдання 1

strings = ["  hello ", "WORLD", " PyThOn  "]

normalized = list(map(lambda s: s.strip().lower(), strings))

print(normalized)


# Завдання 2

users = [
    {"name": "Іван", "age": 25},
    {"name": "Оля", "age": 17},
    {"name": "Петро", "age": 30}
]

result = sorted(
    map(lambda u: u["name"].upper(),
        filter(lambda u: u["age"] >= 18, users)),
    key=lambda name: len(name)
)

print(result)