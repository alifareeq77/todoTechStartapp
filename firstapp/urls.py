from django.urls import path

from . import views
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request, name="world"):
    return f"Hello {name}"

urlpatterns = [
    path("api/", api.urls),
]
