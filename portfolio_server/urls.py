from django.urls import path,include
from . import views
app_name="portfolio_server"
urlpatterns = [
    path('',views.portfolio_page,name="portfolio")
]
