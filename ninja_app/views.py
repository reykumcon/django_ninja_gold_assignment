from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if not "gold" in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def reset_gold(request):
    request.session.flush()
    return redirect('/')

def process_farm(request):
    amount = random.randint(10, 20)
    request.session['gold'] += amount
    alert = f"Earned {amount} golds from the farm - {datetime.now().strftime('%Y/%m/%d %I:%M %p')}"
    request.session['activities'].append(alert)
    return redirect('/')

def process_cave(request):
    amount = random.randint(5, 10)
    request.session['gold'] += amount
    alert = f"Earned {amount} golds from the cave - {datetime.now().strftime('%Y/%m/%d %I:%M %p')}"
    request.session['activities'].append(alert)
    return redirect('/')

def process_house(request):
    amount = random.randint(2, 5)
    request.session['gold'] += amount
    alert = f"Earned {amount} golds from the house - {datetime.now().strftime('%Y/%m/%d %I:%M %p')}"
    request.session['activities'].append(alert)
    return redirect('/')

def process_casino(request):
    amount = random.randint(0, 50)
    if random.randint(0,1) == 0:
        request.session['gold'] -= amount
        alert = f"Lost {amount} golds from the casino - {datetime.now().strftime('%Y/%m/%d %I:%M %p')}"
    else:
        request.session['gold'] += amount
        alert = f"Earned {amount} golds from the casino - {datetime.now().strftime('%Y/%m/%d %I:%M %p')}"
    request.session['activities'].append(alert)
    return redirect('/')