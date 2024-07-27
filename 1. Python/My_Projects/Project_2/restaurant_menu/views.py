from django.shortcuts import render
from django.views import generic
from .models import Item
# Create your views here.

# ListView class from django.views.generic is used to display a list of objects from a model
class MenuList(generic.ListView):
    # Item.objects: This is a query manager that provides access to all the Item objects in the database.
    # order_by('date_created'): This method orders the query results by the date_created field of the Item model.
    queryset = Item.objects.order_by('date_created')
    template_name = 'index.html'

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'