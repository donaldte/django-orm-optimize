
from django.contrib import admin
from django.urls import path
from app.views import generate_random_data, view_test_without_and_with, mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', generate_random_data, name='generate'),
    path('performance/', view_test_without_and_with, name='perfomance'),
    path('', mainpage, name='mainpage')
]
