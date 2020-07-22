from django.view.generic import ListView
from shop.models import Item

item_list = ListView.as_view(model=Item)

from django.urls import path

urlpatterns = [
    path('items/', item_list, name='item_list')
]

#----------------------------------------------
from django.view.generic import ListView
from shop.models import Item

class ItemListView(ListView):
    model = Item

item_list = ItemListView.as_view()

from django.urls import path

urlpatterns = [
    paht('items/', item_list, name='item_list')
]