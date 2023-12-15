'''
Created on 2023/10/27

@author: t21cs062x
'''
from django.urls import path
from .views import ItemList

app_name='shoppinglist'
urlpatterns = [
    path('list/', ItemList.as_view(),name='list'),
]