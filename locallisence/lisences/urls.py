
from django.urls import path
from .views import ClientView, UserCheckView
from .views import ProductView
from .views import LisencesView
from .views import UsersView
from .views import UserCheckView

urlpatterns=[
    path('clients/',ClientView.as_view(),name='clients_list'),
    #Para buscar un solo cliente dependiendo del id
    path('clients/<int:id>',ClientView.as_view(),name='clients_detailed'),


    path('products/',ProductView.as_view(),name='products_list'),
     #Para buscar un solo producto dependiendo del id
    path('products/<int:id>',ProductView.as_view(),name='products_detailed'),

    path('lisences/',LisencesView.as_view(),name='lisences_list'),
    #Para buscar una sola lisencia dependiendo del id
    path('lisences/<int:id>',LisencesView.as_view(),name='isences_detailed'),

    path('users/',UsersView.as_view(),name='users_list'),


    path('check/',UserCheckView.as_view(),name='lisences_list'),
    #Para buscar una sola lisencia dependiendo del id
    path('check/<int:id>',UserCheckView.as_view(),name='isences_detailed')

]