from django.urls import path
from .views import home, contacto, login, quienessomos, sismos, tarjetaNoticia

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('sismos', sismos, name="sismos"),
    path('tarjetaNoticia', tarjetaNoticia, name="tarjetaNoticia"),
]