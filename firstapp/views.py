from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Item


def get_all_items(request):
    items = Item.objects.all()
    return HttpResponse(items[0].title)


def get_item(request, item_id):
    items = Item.objects.filter(id=item_id)
    return HttpResponse(items)


def add_item(request):
    data = {
        "title": 'get out of my laptop', "description": "im a programmer i hate getting out", "group": 'life'
    }
    item = Item.objects.create(title=data['title'], description=data['description'], group=data['group'])
    return JsonResponse(
        [{'code': 200, 'description': 'successfully created raw'}, data], content_type="application/json",
        safe=False)


def delete_item(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return JsonResponse(
        [{'code': 200, 'description': 'successfully deleted raw'}], content_type="application/json",
        safe=False)


def edit_item(request, item_id):
    data = {
        "title": 'get out of my laptop', "description": "im a programmer i love getting out", "group": 'life'
    }
    item = Item.objects.filter(id=item_id)
    item.update(title=data['title'], description=data['description'], group=data['group']).save()
    JsonResponse(
        [{'code': 200, 'description': 'successfully updated raw'}, data], content_type="application/json",
        safe=False)