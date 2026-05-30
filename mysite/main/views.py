import random
from datetime import datetime
from django.shortcuts import render

QUOTES = [
    "The only way to do great work is to love what you do. — Steve Jobs",
    "In the middle of every difficulty lies opportunity. — Albert Einstein",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "Life is what happens when you're busy making other plans. — John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
]

def hello_world(request):
    return render(request, "main/index.html")

def day_of_week(request):
    days = {
        0: "Понеділок", 1: "Вівторок", 2: "Середа",
        3: "Четвер",    4: "П'ятниця", 5: "Субота", 6: "Неділя",
    }
    context = {"day": days[datetime.today().weekday()]}
    return render(request, "main/day.html", context)

def random_quote(request):
    context = {"quote": random.choice(QUOTES)}
    return render(request, "main/quote.html", context)