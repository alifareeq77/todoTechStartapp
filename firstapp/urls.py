from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_items, name='get_all_items'),
    path('get_item/<item_id>', views.get_item, name='get_item'),
    path('delete_item/<item_id>', views.delete_item, name='delete_item'),
    path('add_item', views.add_item, name='add_item'),
    path('edit_item/<item_id>', views.edit_item, name='edit_item'),
]
