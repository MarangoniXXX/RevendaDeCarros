from django.urls import path
from . import views  


app_name = 'cars'

urlpatterns = [
    # A URL '' (raiz) DENTRO DESTE APP apontará para a view 'home'.
    path('', views.home, name='home'),
    
    # A URL '/carro/1/' DENTRO DESTE APP apontará para a view 'car_detail'.
    path('carro/<int:car_id>/', views.car_detail, name='car_detail'),
]
