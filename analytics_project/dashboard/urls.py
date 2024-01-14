from django.urls import path
from . import views

urlpatterns = [
# path('', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),  # New path for the home view
    path('gdp-table/', views.gdp_dashboard, name='dashboard'),
    path('gni-table/', views.gni_dashboard, name='gni-dashboard'),
    path('low_income_countries/', views.low_income_countries, name='low_income_countries-dashboard'),
    path('low_middle_income_countries/', views.low_middle_income, name='low_middle_income_countries-dashboard'),
    path('upper_middle_income_countries/', views.upper_middle_income, name='upper_middle_income_countries-dashboard'),
    path('high_income_countries/', views.high_income, name='high_income_countries-dashboard'),

]