from django.shortcuts import render
from django.db import connection

def home(request):
    return render(request, 'home.html')

def gdp_dashboard(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM gdp_data;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'dash.html', context)

def gni_dashboard(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM gni_data;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'gni_dash.html', context)

def low_income_countries(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM low_income;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'low_income_countries_dash.html', context)

def low_middle_income(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM low_middle_income;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'low_middle_income.html', context)

def upper_middle_income(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM upper_middle_income;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'upper_middle_income.html', context)

def high_income(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM high_income;")
        rows = cursor.fetchall()

    context = {'data': rows}
    return render(request, 'high_income.html', context)