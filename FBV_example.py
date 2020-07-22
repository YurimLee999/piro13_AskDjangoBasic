from django.shortcuts import render
from shop.medels import Item

def item_list(request):
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html'),{
        'item_list':qs,
    })
from django.urls import path

urlpatterns =[
    path('items/', item_list, name='item_list')
]